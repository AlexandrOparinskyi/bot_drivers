import logging
from uuid import uuid4

from slugify import slugify
from sqlalchemy import insert, select

from database.connect import get_async_session
from database.models import User, Car


async def create_user(name: str | None, surname: str | None,
                      username: str | None, user_id: int) -> None:
    async with get_async_session() as session:
        try:
            user_query = insert(User).values(
                name=name,
                surname=surname,
                username=username,
                chat_id=user_id
            )
            await session.execute(user_query)
            await session.commit()
        except Exception as e:
            logging.error(f"User not created: {e}")


async def get_user_by_id(user_id: int) -> User:
    async with get_async_session() as session:
        try:
            user_query = select(User).where(
                User.chat_id == user_id
            )
            user = await session.scalar(user_query)

            if user and user.is_active is False:
                user.is_active = True

            return user
        except Exception as e:
            logging.error(f"User exists error: {e}")


async def create_car(car_name: str, user_id: int) -> None:
    user = await get_user_by_id(user_id)
    slug = slugify(f"{car_name}_{str(uuid4())[:4]}")

    try:
        async with get_async_session() as session:
            car_query = insert(Car).values(
                name=car_name,
                user_id=user.id,
                slug=slug
            )
            await session.execute(car_query)
            await session.commit()
    except Exception as e:
        logging.error(f"Car not created: {e}")
