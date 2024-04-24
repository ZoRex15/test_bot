from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram import Router

from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from app.bot.states import MenuSG, SettingsSG


router = Router()

@router.message(Command(commands=['menu']))
async def menu(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MenuSG.menu)

async def go_to_settings(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=SettingsSG.settings_menu)
