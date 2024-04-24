from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str

@dataclass
class Db:
    password: str
    user: str
    name: str
    host: str
    port: int

    def __post_init__(self):
        self.url = f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

@dataclass
class Config:
    tg_bot: TgBot
    db: Db

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        db=Db(
            password=env('POSTGRES_PASSWORD'),
            name=env('POSTGRES_NAME'),
            host=env('POSTGRES_HOST'),
            port=int(env('POSTGRES_PORT')),
            user=env('POSTGRES_USER')
        )
    )


