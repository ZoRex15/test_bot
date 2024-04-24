from .base import Base

from datetime import date


class User(Base):
    id: int
    join_date: date