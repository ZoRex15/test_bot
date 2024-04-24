from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.kbd import Button

from app.bot.states import BeginningSG

from .getters import get_user_name
from .handlers import go_to_menu



begin = Dialog(
    Window(
        Format(text='Привет {name}!\n'),
        Const(
            text='Этот бот создан для того, чтобы вы могли получать уведомления о новых проектах на  '
            'фриланс-биржах.\n'
            ),
        Const(text='Вы можете настроить бота, перейдя в меню и выбрав интересующие вас биржи и категории.'),
        Button(
            text=Const('🏠Меню🏠'),
            id='menu',
            on_click=go_to_menu
        ),
        getter=get_user_name,
        state=BeginningSG.begin
    )
    
)