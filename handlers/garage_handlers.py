from aiogram import Router, F
from aiogram.types import Message

from keyboards.garage_keyboards import create_enter_garage_keyboard
from services.database_services import get_user_by_id

garage_router = Router()


@garage_router.message(F.text == "🍺 Гараж | Работа с машинами 🚗")
async def process_enter_garage(message: Message):
    """
    Хендлер отрабатывает после нажатия на кнопку
    "🍺 Гараж | Работа с машинами 🚗".
    Открывает меню управления машинами
    """
    user = await get_user_by_id(message.from_user.id)

    username = user.name if user.name else user.username
    premium = "✔ Активен" if user.is_premium else "✖ Не активен"
    text = (f"Ты в гараже, {username} 🚩\n\n"
            f"Количество добавленных машин: {len(user.cars)}\n"
            f"Премиум аккаунт: {premium}\n\n"
            f"Твои последние ремонтные работы")
    keyboard = create_enter_garage_keyboard(user.is_premium)
    await message.answer(text, reply_markup=keyboard)
