from app.core import dto
from app.infrastructure.db.repository.user import UserRepository


async def upsert_user(user: dto.User, user_repo: UserRepository) -> dto.User:
    saved_user = await user_repo.upsert_user(user=user)
    await user_repo.commit()
    return saved_user

async def get_user(user_id: int, user_repo: UserRepository) -> dto.User:
    return await user_repo.get_by_id(id=user_id)