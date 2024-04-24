from .base import Base

from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import ForeignKey, Integer, BigInteger

from app.core import dto


class UserSelectedCategory(Base):
    __tablename__ = 'UserSelectedCategories'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(BigInteger, ForeignKey('Users.id'), nullable=False)
    category_id = mapped_column(Integer, ForeignKey('Categories.id'), nullable=False)

    user = relationship(
        'User',
        foreign_keys=user_id,
        uselist=False,
        back_populates='user_selected_categories'
    )

    category = relationship(
        'Category',
        foreign_keys=category_id,
        uselist=False,
        back_populates='user_selected_categories'
    )

    def __repr__(self):
        return f'UserSelectedCategoryModel(id={self.id}, user_id={self.user_id}, category_id={self.category_id})'

    def to_dto(self) -> dto:
        return dto.UserSelectedCategory(
            id=self.id,
            user_id=self.user_id,
            category_id=self.category_id
        )
