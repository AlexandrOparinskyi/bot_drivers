from dataclasses import dataclass
from environs import env


@dataclass
class TelegramBot:
    token: str
    admin_id: int


@dataclass
class Database:
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str


@dataclass
class Config:
    telegram_bot: TelegramBot
    database: Database


def load_config(path: str | None = None) -> Config:
    env.read_env(path)

    return Config(
        telegram_bot=TelegramBot(
            token=env("TOKEN"),
            admin_id=int(env("ADMIN_ID"))
        ),
        database=Database(
            db_host=env("DB_HOST"),
            db_port=env("DB_PORT"),
            db_name=env("DB_NAME"),
            db_user=env("DB_USER"),
            db_pass=env("DB_PASS")
        )
    )
