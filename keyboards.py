# from aiogram.handlers import message
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет!'), KeyboardButton(text='Пока!')]
], resize_keyboard=True)

inline_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Новости', url='https://dzen.ru/news/')],
    [InlineKeyboardButton(text='Музыка', url='https://zaycev.net/')],
    [InlineKeyboardButton(text='Видео', url='https://vk.com/video')]
])

inline_kb2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать больше', callback_data= 'dynamic')],
])

test = ["Опция 1", "Опция 2"]
async def dinamic_kb():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key), callback_data=key)
    keyboard.adjust(2)
    return keyboard.as_markup()
