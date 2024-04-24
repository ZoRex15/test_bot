from app.core import dto

from typing import Sequence

from sqlalchemy import ScalarResult, select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.interfaces import ORMOption

from app.infrastructure.db.models import UserSelectedCategory

from .base import BaseRepository


class UserSelectedCategoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(UserSelectedCategory, session)

    async def get_by_id(self, id) -> dto.UserSelectedCategory:
        return (await self._get_by_id(id)).to_dto()
    
    async def get_selected_category_by_id(self, user: dto.User, category: dto.Category) -> dto.UserSelectedCategory:
        result: ScalarResult[UserSelectedCategory] = await self.session.scalars(
            select(UserSelectedCategory).where(
                and_(
                    UserSelectedCategory.category_id == category.id,
                    UserSelectedCategory.user_id == user.id
                )
            )
        )
        return result.one().to_dto()
    
    async def get_all(self, options: Sequence[ORMOption] = ()) -> Sequence[dto.UserSelectedCategory]:
        r: ScalarResult[UserSelectedCategory] = await self._get_all()
        return [i.to_dto() for i in r]
    
    async def delete(self, user_selected_category: dto.UserSelectedCategory) -> None:
        user_exchange = await self._get_by_id(id=user_selected_category.id)
        await self.session.delete(user_exchange)

    async def create(self, user: dto.User, category: dto.Category) -> dto.UserSelectedCategory:
        user_selected_category = UserSelectedCategory(
            user_id=user.id,
            category_id=category.id
        )
        self.session.add(user_selected_category)
        await self._flush(user_selected_category)
        return dto.UserSelectedCategory(
            id=user_selected_category.id,
            user_id=user.id,
            category_id=category.id
        )