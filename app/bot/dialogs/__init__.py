from aiogram import Router
from .beginning import beginning_router
from .menu import menu_router
from .settings import settings_router

master_router = Router()

master_router.include_routers(
    beginning_router,
    menu_router,
    settings_router
)