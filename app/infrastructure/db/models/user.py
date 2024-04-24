from .base import Base

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Date, Integer

from app.core import dto


class User(Base):
    __tablename__ = 'Users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    join_date = mapped_column(Date, nullable=False)

    user_selected_categories = relationship(
        'UserSelectedCategory',
        back_populates='user',
        cascade='delete, delete-orphan',
        uselist=True
    )

    def __repr__(self) -> str:
        return f'UserModel(id={self.id}, join_date={self.join_date})'
    
    def to_dto(self) -> dto.User:
        return dto.User(
            id=self.id,
            join_date=self.join_date
        )
  