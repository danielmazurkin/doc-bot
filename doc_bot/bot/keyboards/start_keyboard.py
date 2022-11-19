from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_keyboard(user_id) -> InlineKeyboardMarkup:
    """Формирует панель из кнопки Загрузить документы для печати"""

    buttons = [
        InlineKeyboardButton(
            text="Загрузить документы для печати",
            callback_data=f"start_user_id:{user_id}",
        ),
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
    return reply_markup
