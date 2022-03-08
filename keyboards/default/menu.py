from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuMain = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Найти Видео с YouTube"),
            KeyboardButton(text="Популярные видео"),
        ],
        [
            KeyboardButton(text="Сменить количество")
        ]
    ],
    resize_keyboard=True
)

menuSearch = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ],
    ],
    resize_keyboard=True
)