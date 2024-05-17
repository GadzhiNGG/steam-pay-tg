from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config.config import smiles
import key as k

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, я помогу тебе пополнить Steam, Epic, а также купить Discord Nitro')
    await message.answer_photo(photo='AgACAgIAAxkBAANTZkYlOOna2dteSiTsb0Tp7yumvd0AAofaMRv2uTFK_dxowo_mKWcBAAMCAAN5AAM1BA',
                               caption=f'Рекламная вставка {x}',
                               reply_markup=k.main)

@router.message(F.text.lower() == 'steam')
async def steam_cmd(message:Message):
    await message.answer('Пополнить Steam-Кошелек',
                         reply_markup=k.steam)

@router.message(F.text.lower() == 'epic games')
async def steam_cmd(message:Message):
    await message.answer('Пополнить Epic Games',
                         reply_markup=k.epic)
    
@router.message(F.text.lower() == 'Discord Nitro')
async def steam_cmd(message:Message):
    await message.answer('Оплатить Discord Nitro',
                         reply_markup=k.discord)


