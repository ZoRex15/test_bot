from aiogram import Router
from .dialogs import (
    begin
)
from .handlers import router as h_router


beginning_router = Router()

beginning_router.include_routers(
    begin,
    h_router
)
