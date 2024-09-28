import logging

from pyexpat.errors import messages

from config import bot, dp, admin
from aiogram import Dispatcher
from aiogram.utils import executor
from handlers import commands, FSM_reg, FSM_zak,send_products
from db import db_main
from handlers.FSM_zak import FSM_zakaz


# async def on_startup(_):
#     for i in admin:
#         await bot.send_message(chat_id=i, text="Бот включен!")

async def on_startup(_):
    await db_main.sql_create()

commands.register_commands(dp)
FSM_reg.register_fsm_store(dp)
# FSM_zakaz.register_fsm_zak(dp)
send_products.register_send_products_handler(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
