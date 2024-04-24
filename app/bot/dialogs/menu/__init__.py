from aiogram import Router
from .dialogs import menu
from .handlers import router


menu_router = Router()
menu_router.include_routers(
    menu,
    router
)

__all__ = [
    'menu_router'
]