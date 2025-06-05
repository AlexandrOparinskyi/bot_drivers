import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import load_config
from handlers.garage_handlers import garage_router
from handlers.user_handlers import user_router
from keyboards.main_menu_keyboard import create_main_menu
from middlewares.user_middlewares import IsUserRegisterMiddleware

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG)

    config = load_config()

    bot: Bot = Bot(config.telegram_bot.token,
                   default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp: Dispatcher = Dispatcher()

    garage_router.message.middleware(IsUserRegisterMiddleware())
    garage_router.callback_query.middleware(IsUserRegisterMiddleware())

    dp.include_router(user_router)
    dp.include_router(garage_router)

    await create_main_menu(bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Bot not started: {e}")


asyncio.run(main())
