from aiogram import types, Dispatcher
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text ='Добро пожаловать!')

async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Приветсвуем вас в онлайн магазине одежды: "Мери". Этот бот нужен для упрощения вашей жизни.')




def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands="start")
    dp.register_message_handler(info_handler, commands="info")
