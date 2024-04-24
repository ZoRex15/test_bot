from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, ManagedMultiselect

from app.bot.states import ExchangeSettingSG
from app.infrastructure.db.holder import HolderRepository

from app.core.service import user_selected_category, user, category    


async def go_to_categories(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=ExchangeSettingSG.exchanges)

async def set_user_category(
        callback: CallbackQuery,
        multiselect: ManagedMultiselect,
        dialog_manager: DialogManager,
        item_id: str
):
    holder_repository: HolderRepository = dialog_manager.middleware_data.get('repo')
    check = multiselect.is_checked(item_id=item_id)
    u = await user.get_user(
            user_id=callback.from_user.id,
            user_repo=holder_repository.user
        )
    c = await category.get_category_by_id(
        id=int(item_id),
        category_repository=holder_repository.category
    )
    if not check:
        await user_selected_category.create(
           user=u,
           category=c,
           user_selected_category_repository=holder_repository.user_selected_category 
        )
    else:
        await user_selected_category.delete(
            user=u,
            category=c,
            user_selected_category_repository=holder_repository.user_selected_category
        )

async def back_to_main_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()


async def back_to_settings_menu(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.done()



        



    