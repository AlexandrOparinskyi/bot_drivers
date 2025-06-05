from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.menu_keyboard import create_menu
from services.database_services import get_user_by_id, create_user

user_router = Router()


@user_router.message(Command(commands="start"))
async def process_start_command(message: Message):
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        await create_user(message.from_user.first_name,
                          message.from_user.last_name,
                          message.from_user.username,
                          message.from_user.id)

    keyboard = create_menu()
    await message.answer("Здесь будет текст для старта",
                         reply_markup=keyboard)

