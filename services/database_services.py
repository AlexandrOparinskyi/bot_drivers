import logging

from sqlalchemy import insert, select

from database.connect import get_async_session
from database.models import User


async def create_user(name: str | None, surname: str | None,
                      username: str | None, chat_id: int) -> None:
    async with get_async_session() as session:
        try:
            user_query = insert(User).values(
                name=name,
                surname=surname,
                username=username,
                chat_id=chat_id
            )
            await session.execute(user_query)
            await session.commit()
        except Exception as e:
            logging.error(f"User not created: {e}")


async def exists_user(chat_id: int) -> User:
    async with get_async_session() as session:
        try:
            user_query = select(User).where(
                User.chat_id == chat_id
            )
            user = await session.scalar(user_query)

            if user.is_active is False:
                user.is_active = True

            return user
        except Exception as e:
            logging.error(f"User exists error: {e}")
