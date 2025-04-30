from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.database_services import create_car, get_cars_by_user_id

car_router = Router()


@car_router.message(Command(commands="add_new_car"))
async def start_add_new_car(message: Message):
    cars = await get_cars_by_user_id(message.from_user.id)
    if len(cars) >= 1:
        await message.answer("Что бы добавить больше 1 автомобиля необходимо "
                             "приобрести премиум подписку\n\n"
                             "/premium (скоро...)")
        return
    await create_car("New car", message.from_user.id)
    await message.answer("Created")
