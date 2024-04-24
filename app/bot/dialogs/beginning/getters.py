from aiogram.types import User
from aiogram_dialog import DialogManager


async def get_user_name(event_from_user: User, **kwargs):
    return {'name': event_from_user.full_name}