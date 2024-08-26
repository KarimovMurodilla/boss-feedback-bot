"""User model file."""
import datetime
from typing import Annotated, Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.bot.structures.role import Role

from .base import Base
from ...language.enums import Locales


class Feedback(Base):
    """Feedback model."""

    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('user.user_id', ondelete='CASCADE'),
        unique=False,
        nullable=False,
    )
    user = relationship('User')
    category: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    type_of_feedback: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    feedback: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    created_at: Mapped[Optional[Annotated[datetime.datetime, mapped_column(nullable=False, default=datetime.datetime.utcnow)]]]

    def __str__(self):
        return f"{self.category} - {self.type_of_feedback}"
