from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_enter_garage_keyboard(prem: bool) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
            text="🚙 Мои машины",
            callback_data="get_my_cars"
        ),
        InlineKeyboardButton(
            text="➕ Добавить авто",
            callback_data="add_new_car"
        ),
        width=2
    )
    kb_builder.row(
        InlineKeyboardButton(
            text="📓 Мои ремонтные работы 📓",
            callback_data="get_my_service_work"
        ),
        InlineKeyboardButton(
            text="✏ Добавить работу над авто 🔧",
            callback_data="add_service_work"
        ),
        width=1
    )

    if not prem:
        kb_builder.row(
            InlineKeyboardButton(
                text="✔ Подключить premium аккаунт ✔",
                callback_data="connect_premium"
            )
        )

    kb_builder.row(
        InlineKeyboardButton(
            text="◄◄◄ Вернуться на главную",
            callback_data="back_to_main"
        )
    )

    return kb_builder.as_markup()
