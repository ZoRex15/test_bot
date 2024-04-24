
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import Redis, RedisStorage, DefaultKeyBuilder
from aiogram_dialog import setup_dialogs

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import load_config, Config
from app.bot.middlewares.db import DatabaseMiddleware
from app.bot.dialogs import master_router


async def main():
    config: Config = load_config()
    engine = create_async_engine(url=config.db.url, echo=True)
    session = async_sessionmaker(engine)
    bot = Bot(token=config.tg_bot.token)
    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis, key_builder=DefaultKeyBuilder(with_destiny=True))
    dp = Dispatcher(storage=storage)
    dp.update.middleware.register(DatabaseMiddleware(session))
    dp.include_router(master_router)
    setup_dialogs(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
