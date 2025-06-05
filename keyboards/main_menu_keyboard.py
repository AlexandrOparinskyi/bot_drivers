from aiogram import Bot
from aiogram.types import BotCommand


async def create_main_menu(bot: Bot):
    await bot.set_my_commands([
        BotCommand(
            command="/start",
            description="♻ Перезапустить бота"
        )
    ])
