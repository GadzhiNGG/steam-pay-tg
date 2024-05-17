import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.config import token, x 
from app.handlers import router



bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())