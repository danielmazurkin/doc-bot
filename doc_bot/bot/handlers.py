from bot.keyboards.start_keyboard import get_start_keyboard
from bot.constants.messages import START_MESSAGE
from account.models import User


def start_callback(update, context):
    User(
        telegram_id=update.effective_user['id'],
        username=update.effective_user['username'],
        name=update.effective_user['first_name'],
    ).save()
    update.message.reply_text(text=START_MESSAGE, reply_markup=get_start_keyboard(update.effective_user['id']))


