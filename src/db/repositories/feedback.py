"""User repository file."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.role import Role

from ..models import Feedback
from .abstract import Repository


class FeedbackRepo(Repository[Feedback]):
    """Feedback repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        super().__init__(type_model=Feedback, session=session)

    async def new(
        self,
        user_id: int,
        category: str | None = None,
        type_of_feedback: str | None = None,
        feedback: str | None = None
    ) -> None:
        await self.session.merge(
            Feedback(
                user_id=user_id,
                category=category,
                type_of_feedback=type_of_feedback,
                feedback=feedback,
            )
        )
        await self.session.commit()

