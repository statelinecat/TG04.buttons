import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import types
from config import TOKEN, POGODA, URL, URL_FORECAST
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import logging
import keyboards as kb

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(F.text == 'Опция 1')
async def op1(message: Message):
    await message.answer("Опция 1", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == 'Опция 2')
async def op2(message: Message):
    await message.answer("Опция 2", reply_markup=types.ReplyKeyboardRemove())

@dp.callback_query(F.data == 'dynamic')
async def callback_dynamic(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Кнопка нажата")
    await callback.message.edit_text(f"{callback.from_user.full_name}, выберите опцию:", reply_markup=await kb.dinamic_kb())


@dp.callback_query(F.data == 'opt1')
async def callback_dynamic(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Опция 1")


@dp.callback_query(F.data == 'opt2')
async def callback_dynamic(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Опция 2")

@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать!', reply_markup=kb.main)

@dp.message(F.text == 'Привет!')
async def hitext(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == 'Пока!')
async def goodbyetext(message: Message):
    await message.answer(f"До свидания, {message.from_user.full_name}!", reply_markup=types.ReplyKeyboardRemove())

@dp.message(Command('links'))
async def cmd_links(message: Message, state: FSMContext):
    await message.answer("Выберете:", reply_markup=kb.inline_kb)

@dp.message(Command('dynamic'))
async def cmd_dynamic(message: Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup= kb.inline_kb2)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())