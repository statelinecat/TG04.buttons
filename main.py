import asyncio
import requests
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN, POGODA, URL, URL_FORECAST
import random
from datetime import datetime, timedelta
from gtts import gTTS
import os
import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiohttp
import logging
import keyboards as kb

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
API_KEY = POGODA
WEATHER_URL = URL
WEATHER_URL_FORECAST = URL_FORECAST





@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(reply_markup=kb.main)

@dp.message(F.text == 'Привет!')
async def hitext(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=kb.main)

@dp.message(F.text == 'Пока!')
async def goodbyetext(message: Message):
    await message.answer(f"До свидания, {message.from_user.full_name}!", reply_markup=kb.main)

# @dp.message(Command('links'))
# async def cmd_start(message: Message, state: FSMContext):
#     await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=kb.main)
#
# @dp.message(Command('dynamic'))
# async def cmd_start(message: Message, state: FSMContext):
#     await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=kb.main)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())