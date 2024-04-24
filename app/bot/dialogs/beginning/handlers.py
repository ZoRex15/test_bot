from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from app.core.service.user import upsert_user
from app.core import dto
from app.bot.states import BeginningSG, MenuSG
from app.infrastructure.db.holder import HolderRepository


router = Router()

@router.message(CommandStart())
async def start(message: Message, repo: HolderRepository, dialog_manager: DialogManager):
    user = dto.User(
        id=message.from_user.id,
        join_date=message.date.date()
    )
    await upsert_user(user=user, user_repo=repo.user)
    await dialog_manager.start(state=BeginningSG.begin, mode=StartMode.RESET_STACK)

async def go_to_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.menu)