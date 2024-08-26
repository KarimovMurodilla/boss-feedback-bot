"""This file represents a start logic."""

from sqlalchemy.exc import IntegrityError
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart

from src.configuration import conf
from src.db.database import Database
from src.language.translator import LocalizedTranslator
from src.bot.structures.keyboards import common
from src.bot.structures.fsm.feedback import FeedbackGroup

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start_handler(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    """Start command handler."""
    await state.clear()

    user = await db.user.get_me(message.from_user.id)

    if not user:
        await db.user.new(
            user_id=message.from_user.id,
            user_name=message.from_user.username,
            first_name=message.from_user.first_name,
            second_name=message.from_user.last_name,
            is_premium=bool(message.from_user.is_premium)
        )

    await message.answer(
        "Assalomu alaykum, salomatmisiz?\n\n"
        "Bizning anonim botimizga xush kelibsiz! Pastdan kerakli boʻlimni tanlashingiz mumkin.",
        reply_markup=common.show_category()
    )
    await state.set_state(FeedbackGroup.category)

@start_router.message(F.text.in_(['SMM', 'Sales', 'Brending', 'Web']), FeedbackGroup.category)
async def process_category(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    await message.answer(
        "Javobingiz uchun tashakkur!"
    )
    await message.answer(
        "Aynan qanday fikr bildirmoqchisiz?",
        reply_markup=common.show_types_of_feedback()
    )
    await state.update_data(category=message.text)
    await state.set_state(FeedbackGroup.type_of_feedback)

@start_router.message(F.text.in_(['Fikr', 'Shikoyat', 'Taklif', 'Orqaga']))
async def process_type_of_feedback(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    type_of_feedback = message.text.lower()

    if type_of_feedback == 'orqaga':
        await state.set_state(FeedbackGroup.category)
        return await message.answer(
            "Kerakli bo'limni tanlang.",
            reply_markup=common.show_category()
        )

    await message.answer(
        f"Iltimos {type_of_feedback}ingizni yozib qoldiring",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.update_data(type_of_feedback=type_of_feedback)
    await state.set_state(FeedbackGroup.feedback)

@start_router.message(FeedbackGroup.feedback)
async def process_feedback(message: types.Message, db: Database, translator: LocalizedTranslator, state: FSMContext):
    data = await state.get_data()
    category: str = data.get('category')
    type_of_feedback: str = data.get('type_of_feedback')
    feedback: str = message.text

    await db.feedback.new(
        user_id=message.from_user.id,
        category=category,
        type_of_feedback=type_of_feedback.title(),
        feedback=feedback
    )
    await message.answer(
        f"Rahmat, sizning {type_of_feedback}ingizni koʻrib chiqamiz."
    )

    for user_id in conf.ADMINS:
        await message.bot.send_message(user_id, 
            f"Mavzu: {type_of_feedback.title()}\n"
            f"Kategoriya: {category}\n\n"
            f"{feedback}"
        )
