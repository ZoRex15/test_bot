from aiogram import Router
from .dialogs import settings, exchange_setting


settings_router = Router()

settings_router.include_routers(
    settings,
    exchange_setting,
)

__all__ = [
    'settings_router'
]