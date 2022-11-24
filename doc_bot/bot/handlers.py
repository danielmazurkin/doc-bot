from bot.keyboards.start_keyboard import get_start_keyboard
from bot.constants.messages import START_MESSAGE
from account.models import User
from order.models import Order, Document
from django.conf import settings
from django.core.files import File
from common.use_case_image import UseCaseImage


def start_callback(update, context):
    """Callback для обработки команды /start"""
    user_exists = User.objects.filter(telegram_id=update.effective_user['id']).exists()
    user_id = update.effective_user['id']

    if not user_exists:
        User(
            telegram_id=update.effective_user['id'],
            username=update.effective_user['username'],
            name=update.effective_user['first_name'],
        ).save()

    update.message.reply_text(text=START_MESSAGE, reply_markup=get_start_keyboard(user_id))


def after_enter_button(update, context):
    """Срабатывает после нажатия первой кнопки."""
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Загрузите ваши файлы в бота!",
        disable_web_page_preview=True,
    )


def document_callback(update, context):
    """Срабатывает для загрузки документов."""
    # Если заказ существует is_new=True для пользователя, то добавляем к нему файл
    # Если такого заказа нет, то создаем и добавляем к нему файл
    order = Order.objects.filter(
        user__telegram_id=update.effective_chat.id,
        is_new=True
    ).first()

    with open(f'{settings.MEDIA_ROOT}/{update.message.document.file_name}', 'wb') as file:
        context.bot.get_file(update.message.document).download(out=file)

    file = File(open(f'{settings.MEDIA_ROOT}/{update.message.document.file_name}', "rb"))

    if order:
        Document(file=file, order=order).save()
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Вы загрузили несколько файлов, "
                                                   f"ваш код заказа остался прежним: <b> {order.number} </b>",
            parse_mode='HTML',
        )
    else:
        user = User.objects.filter(
            telegram_id=update.effective_chat.id
        ).first()

        order = Order(
            is_new=True,
            user=user,
            number=Order.get_number()
        )
        order.save()

        Document(file=file, order=order).save()

        image = UseCaseImage().execute(str(order.number))
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Ваш код для документов: <b> {order.number} </b>",
            parse_mode='HTML',
        )
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Ваш проверочный код представлен на картинке ниже",
            parse_mode='HTML',
        )
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=image)
