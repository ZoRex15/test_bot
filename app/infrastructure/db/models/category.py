from .base import Base

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, VARCHAR

from app.core import dto



class Category(Base):
    __tablename__ = 'Categories'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(VARCHAR(50), nullable=False)

    user_selected_categories = relationship(
        'UserSelectedCategory',
        uselist=True,
        back_populates='category'
    )

    def __repr__(self):
        return f'CategoryModel(id={self.id}, name={self.name})'
    
    def to_dto(self) -> dto.Category:
        return dto.Category(
            id=self.id,
            name=self.name
        )