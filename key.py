from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Steam')],
    [KeyboardButton(text='Epic Games')],
    [KeyboardButton(text='Discord Nitro')],
],  
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...')

steam = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Перейти на страницу оплаты', url='https://kupikod.com/')],                   
])

epic = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Перейти на страницу оплаты', url='https://kupikod.com/')],                   
])

discord = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='Перейти на страницу оплаты', url='https://kupikod.com/')],                   
])

