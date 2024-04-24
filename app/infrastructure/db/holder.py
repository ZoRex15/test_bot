from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.repository import (
    UserRepository,
    CategoryRepository,
    UserSelectedCategoryRepository   
)


class HolderRepository:
    def __init__(self, session: AsyncSession):
        self.user = UserRepository(session=session)
        self.category = CategoryRepository(session=session)
        self.user_selected_category = UserSelectedCategoryRepository(session=session)