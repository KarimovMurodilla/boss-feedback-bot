from aiogram import types


def show_category():
    kb = [
        [
            types.KeyboardButton(text="SMM"),
            types.KeyboardButton(text="Sales")
        ],

        [
            types.KeyboardButton(text="Brending"),
            types.KeyboardButton(text="Web")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard


def show_types_of_feedback():
    kb = [
        [
            types.KeyboardButton(text="Fikr"),
            types.KeyboardButton(text="Shikoyat")
        ],
        [types.KeyboardButton(text="Taklif")],
        [types.KeyboardButton(text="Orqaga")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard
