from __future__ import annotations

from typing import (
    List,
    Optional,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import (
    ForeignKey,
    String,
    Date,
    Time,
    Column,
)

from . import Base
from .user import User

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    date = Column("date", Date)
    time = Column("time", Time, nullable=True)
    header: Mapped[str] = mapped_column(String(80))
    describe: Mapped[str] = mapped_column(String(250), nullable=True)


    def __repr__(self):
        return f"Event: {self.header}"

    def __str__(self):
        return self.header.capitalize()




