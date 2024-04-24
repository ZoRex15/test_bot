from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import ManagedMultiselect

from app.infrastructure.db.holder import HolderRepository

from app.core.service import category, user_selected_category


async def get_all_categories(dialog_manager: DialogManager, **kwargs):
    holder_repository: HolderRepository = dialog_manager.middleware_data.get('repo')
    user_selected_categories = await user_selected_category.get_all(
        user_selected_category_repository=holder_repository.user_selected_category
    )
    multiselect: ManagedMultiselect = dialog_manager.find('category')
    for i in user_selected_categories:
        await multiselect.set_checked(
            item_id=i.id,
            checked=True
        )
    categories = await category.get_all_categories(
        category_repository=holder_repository.category
    )
    categories = [(i.name, i.id) for i in categories]
    return {'categories': categories}

