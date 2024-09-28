import logging
from config import bot, dp, admin
from aiogram import Dispatcher
from aiogram.utils import executor
from handlers import commands



async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот включен')

commands.register_commands(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
