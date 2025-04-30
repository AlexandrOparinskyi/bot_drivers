from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from services.database_services import get_user_by_id


class IsUserRegisterMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler:
            Callable[[TelegramObject, Dict[str, Any]],
                     Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        user = await get_user_by_id(event.chat.id)

        if user is None:
            return

        return await handler(event, data)