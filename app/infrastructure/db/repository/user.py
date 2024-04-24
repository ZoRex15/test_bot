from .base import BaseRepository

from sqlalchemy import ScalarResult
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.models import User

from app.core import dto


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def get_by_id(self, id: int) -> dto.User:
        return (await self._get_by_id(id)).to_dto()
    
    async def _user(self, id: int) -> User:
        user = await self.session.get(User, id)
        if not User:
            raise 
        return user
    
    async def upsert_user(self, user: dto.User) -> dto.User:
        kwargs = {
            'id': user.id,
            'join_date': user.join_date
        }
        saved_user = await self.session.execute(
            insert(User)
            .values(**kwargs)
            .on_conflict_do_update(
            index_elements=(User.id,), set_=kwargs, where=User.id == user.id
            )
            .returning(User)
        )
        return saved_user.scalar_one().to_dto()

    async def commit(self):
        await self.session.commit()

