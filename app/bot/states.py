from aiogram.fsm.state import StatesGroup, State


class BeginningSG(StatesGroup):
    begin = State()

class MenuSG(StatesGroup):
    menu = State()

class SettingsSG(StatesGroup):
    settings_menu = State()

class ExchangeSettingSG(StatesGroup):
    exchanges = State()
    exchange_menu = State()
    categories_menu = State()
    subcategories_menu = State()
    mega_subcategories_menu = State()
