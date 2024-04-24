from typing import TypeVar, Generic

from collections.abc import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, ScalarResult
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm.interfaces import ORMOption

from app.infrastructure.db.models import Base


Model = TypeVar('Model', bound=Base, covariant=True, contravariant=False)

class BaseRepository(Generic[Model]):
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.session = session
        self.model = model

    async def _get_by_id(self, id: int, options: Sequence[ORMOption] | None = None, populate_existing: bool = False
    ) -> Sequence[Model]:
        r = await self.session.get(
            self.model, id, options=options, populate_existing=populate_existing
        )
        if r is None:
            raise NoResultFound
        return r
    
    async def _delete(self, obj: Base):
        self.session.delete(obj)

    async def delete_all(self):
        await self.session.execute(delete(self.model))

    async def _get_all(self, options: Sequence[ORMOption] = ()) -> Sequence[Model]:
        r: ScalarResult[Model] = await self.session.scalars(
            select(self.model).options(*options)
        )
        return r.all()

    def _save(self, obj: Base):
        self.session.add(obj)

    async def commit(self):
        await self.session.commit()
     
    async def _flush(self, *objects: Base):
        await self.session.flush(objects)
    