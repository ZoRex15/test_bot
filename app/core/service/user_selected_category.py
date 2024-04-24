from app.infrastructure.db.repository.user_selected_category import UserSelectedCategoryRepository

from app.core import dto


async def get_selected_category_by_id(
        user_selected_category_repository: UserSelectedCategoryRepository,
        user: dto.User,
        category: dto.Category
):
    result = await user_selected_category_repository.get_selected_category_by_id(
        user=user,
        category=category
    )
    return result

async def create(
    user_selected_category_repository: UserSelectedCategoryRepository,
    user: dto.User,
    category: dto.Category
):
    await user_selected_category_repository.create(
        user=user,
        category=category
    )
    await user_selected_category_repository.commit()

async def delete(
    user_selected_category_repository: UserSelectedCategoryRepository,
    user: dto.User,
    category: dto.Category
):
    user_selected_category = await user_selected_category_repository.get_selected_category_by_id(
        user=user,
        category=category
    )
    await user_selected_category_repository.delete(
        user_selected_category=user_selected_category
    )
    await user_selected_category_repository.commit()

async def get_all(user_selected_category_repository: UserSelectedCategoryRepository):
    return await user_selected_category_repository.get_all()