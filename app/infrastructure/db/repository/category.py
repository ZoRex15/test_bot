from typing import Sequence
from sqlalchemy.orm.interfaces import ORMOption
from .base import BaseRepository

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import ScalarResult

from app.infrastructure.db.models import Category
from app.core import dto


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, session: AsyncSession):
        super().__init__(Category, session)

    async def get_by_id(self, id: int) -> dto.Category:
        return (await self._get_by_id(id)).to_dto()
    
    async def get_all(self, options: Sequence[ORMOption] = ()) -> Sequence[dto.Category]:
        categories = await self._get_all(options=options)
        return [i.to_dto() for i in categories]
    
    async def create(self, category: dto.Category) -> dto.Category:
        category = Category(
            name=category.name
        )
        self.session.add(category)
        await self._flush(category)
        return dto.Category(
            id=category.id,
            name=category.name
        )

    async def delete(self, category: dto.Category) -> None:
        category = self._get_by_id(category.id)
        await self.session.delete(category)

    