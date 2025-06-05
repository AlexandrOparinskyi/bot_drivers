from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey, Text
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

    user = relationship("User", back_populates="cars", lazy="selectin")


# class AddCarAnswer(Base):
#     """Модель ответов при добавлении машин"""
#     __tablename__ = "add_car_answers"
#
#     handler = Column(String, nullable=False, unique=True)
#     text = Column(Text, nullable=False)
