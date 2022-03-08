from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold
from loader import dp
from keyboards.default import menuMain,menuSearch
from states import StateBot
from utils.scraping import getVideos,getPopularVideos


@dp.message_handler(state=StateBot.S1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1 = answer)
    await message.answer(f"Количество видео: {hbold(answer)}",reply_markup=menuMain)
    await message.answer("Выберите действие с меню:")
    await state.reset_state(with_data=False)


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menuMain)


@dp.message_handler(content_types=['text'])
async def get_back(message: types.Message,state: FSMContext):
    if message.text == "Назад":
        await message.answer(text="",reply_markup=menuMain)

    elif message.text == "Найти Видео с YouTube":
        await message.answer("Введите название видео", reply_markup=menuSearch)
        await StateBot.S2.set()

    elif message.text == "Популярные видео":
        data = await state.get_data()
        count = data.get("answer1")
        if count == None:
            count = 10
        await message.answer("Поиск \U0001F504")

        allVideos = getPopularVideos(count)

        for i in allVideos:
            await message.answer(text=i)

        await message.answer("Готово \U00002705")

    elif message.text == "Сменить количество":
        await message.answer("Введите количество: ")
        await state.update_data(answer1 = message.text)
        await StateBot.S1.set()


@dp.message_handler(state=StateBot.S2)
async def get_videos_from_youtube(message: types.Message, state: FSMContext):
    await state.update_data(answer2=message.text)
    if message.text == "Назад":
        await state.reset_state(with_data=False)
        await message.answer(text="Вы в основном меню", reply_markup=menuMain)
    else:
        data = await state.get_data()
        count  = data.get("answer1")
        await message.answer("Поиск \U0001F504")
        allVideos = getVideos(message.text,count)

        for i in allVideos:
            await message.answer(text=i)

        await message.answer("Готово \U00002705")