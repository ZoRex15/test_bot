import operator

from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, Group, Back, Multiselect

from app.bot.states import SettingsSG, ExchangeSettingSG

from .handlers import (
    go_to_categories,
    back_to_main_menu,
    back_to_settings_menu,
    set_user_category
    
)
from .getters import (
    get_all_categories,
)


settings = Dialog(
    Window(
        Const(text='🔧Настройки⚙️'),
        Group(
            Button(
                text=Const(text='Категории'),
                id='categories',
                on_click=go_to_categories
            ),
            Back(text=Const('⬅️Назад'),
                 id='back_to_main_menu',
                 on_click=back_to_main_menu),
        ),
        state=SettingsSG.settings_menu
    ), 
)        

exchange_setting = Dialog(
    Window(
        Const(text='Категории'),
        Multiselect(
            checked_text=Format('🟢 {item[0]}'),
            unchecked_text=Format('🔴 {item[0]}'),
            id='category',
            item_id_getter=operator.itemgetter(1),
            items='categories',
            on_click=set_user_category
        ),
        Back(text=Const('⬅️Назад'),
             id='back_to_settings_menu',
             on_click=back_to_settings_menu),
        state=ExchangeSettingSG.exchanges,
        getter=get_all_categories
    )
)