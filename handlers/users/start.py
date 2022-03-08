from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states import StateBot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \n"
                         f"Введите количество роликов которые вы хотите получить: ")

    await StateBot.S1.set()
