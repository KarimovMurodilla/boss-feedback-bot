from aiogram.fsm.state import StatesGroup, State


class FeedbackGroup(StatesGroup):
    """Use this state for registration"""
    
    category = State()
    type_of_feedback = State()
    feedback = State()
