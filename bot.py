from aiogram import Dispatcher, Router, Bot
from aiogram.types import Message
import asyncio


bot = Bot(token="...")
dp = Dispatcher()
router = Router()

dp.include_router(router)


async def start(message: Message):
    message.answer(message.text)


async def main():
    try:
        dp.start_polling(bot)

    except KeyboardInterrupt:
        print("exit(1)")
        exit(1)


if __name__ == "__main__":
    asyncio.run(main())
