from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Group

from app.bot.states import MenuSG

from .handlers import go_to_settings

menu = Dialog(
    Window(
        Const(text='🏠Меню🏠'),
        Group(
            Button(
                text=Const(text='⚙️Настройки🔧'),
                id='settings',
                on_click=go_to_settings
            ),
        ),
        state=MenuSG.menu
    )
)