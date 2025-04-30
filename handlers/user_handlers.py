from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

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

    text = "Привет"

    if message.from_user.first_name:
        text += f", {message.from_user.first_name}🖐️\n\n"
    else:
        text += "🖐️\n\n"

    text += ("Я буду вести заметки твоего автомобиля 🚗 и напоминать"
             " о заменах разных комплектующих\n\n"
             "Тебе нужно будет только добавлять свои данные📃\n\n"
             "Подробнее ты можешь почитать тут - /help\n\n"
             "Для начала давай добавим машину - /add_new_car")

    await message.answer(text)


@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    user = await get_user_by_id(message.from_user.id)

    if user is None:
        await message.answer("Для начала введите команду /start")
        return

    await message.answer("Здесь будет информацию /help")
