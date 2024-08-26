from fastapi import Request
from sqladmin import ModelView

from src.db.models import User, Feedback

# Your views here (for more information: https://aminalaee.dev/sqladmin/#quickstart)
class UserAdmin(ModelView, model=User):
    column_list = [User.user_id, User.user_name, User.first_name, User.second_name]
    can_create = False
    can_edit = True
    can_delete = True
    icon = "fa-solid fa-users"
    name_plural = "Users"
    page_size = 100
    
    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True
    
class FeedbackAdmin(ModelView, model=Feedback):
    column_list = [Feedback.category, Feedback.type_of_feedback, Feedback.feedback]
    column_details_list = [Feedback.category, Feedback.type_of_feedback, Feedback.feedback]
    can_create = False
    can_edit = False
    can_delete = True
    icon = "fa-solid fa-comment"
    name_plural = "Feedbacks"
    page_size = 100
    
    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True