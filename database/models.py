from uuid import uuid4

from slugify import slugify
from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey
from sqlalchemy.event import listens_for
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


class User(Base):
    """Модель пользователей"""
    __tablename__ = "users"

    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    username = Column(String, nullable=True, unique=True)
    chat_id = Column(BigInteger, nullable=False, unique=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_premium = Column(Boolean, default=False, nullable=False)

    cars = relationship("Car", back_populates="user", lazy="selectin")


class Car(Base):
    """Модель машин"""
    __tablename__ = "cars"

    name = Column(String(155), nullable=False)
    slug = Column(String(155), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="cars")


@listens_for(Car, "before_insert")
def generate_slug(mapper, connection, target):
    """Автоматическая генерация поля slug для модели Car"""
    if not target.slug:
        target.slug = slugify(f"{target.name[:30]}-{str(uuid4())[:4]}")
