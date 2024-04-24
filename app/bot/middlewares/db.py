from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.infrastructure.db.holder import HolderRepository


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session: async_sessionmaker[AsyncSession]):
        self.session = session

    async def __call__(
    self,
    handler: Callable[[TelegramObject, Dict[str, Any]], 
    Awaitable[Any]], event: TelegramObject,
    data: Dict[str, Any]
    ) -> Any:
        
        async with self.session() as session:
            holder = HolderRepository(session=session)
            data['repo'] = holder
            r = await handler(event, data)
            return r