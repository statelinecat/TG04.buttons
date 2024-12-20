
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import  InlineKeyboardBuilder


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

test = [{"Опция 1": "opt1"}, {"Опция 2": "opt2"}]
async def dinamic_kb():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        for k_text, k_data in key.items():
            keyboard.add(InlineKeyboardButton(text=k_text, callback_data=k_data))
            keyboard.adjust(2)
    return keyboard.as_markup()
