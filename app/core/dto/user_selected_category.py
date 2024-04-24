from .base import Base


class UserSelectedCategory(Base):
    id: int
    user_id: int
    category_id: int