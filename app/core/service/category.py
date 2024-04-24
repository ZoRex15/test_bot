from app.infrastructure.db.repository import CategoryRepository

from typing import Sequence

from app.core import dto


async def get_all_categories(category_repository: CategoryRepository) -> Sequence[dto.Category]:
    return await category_repository.get_all()

async def get_category_by_id(category_repository: CategoryRepository, id: int) -> dto.Category:
    return await category_repository.get_by_id(id=id)
   