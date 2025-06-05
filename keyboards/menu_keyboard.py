from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_menu() -> ReplyKeyboardMarkup:
    """
    Основная клавиатура бота
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🍺 Гараж | Работа с машинами 🚗")],
            [KeyboardButton(text="❓ FAQ | Часто задаваемые вопросы ❓"),
             KeyboardButton(text="📃 Инструкции по работе с ботом 📃")],
            [KeyboardButton(text="🌟 Premium | Подключить 🌟")],
            [KeyboardButton(text="💯 Отзывы наших пользователей 💯")],
            [KeyboardButton(text="💠 Поддержать проект 💠")]
        ],
        resize_keyboard=True
    )
