from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from handlers.FSM_reg import FSM_store


class FSM_zakaz(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    phone_number = State()

async def start_fsm_zakaz(message: types.Message):
    await message.answer('Введите артикул товара: ')
    await FSM_store.product_id.set()

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Размер товара: ')
    await FSM_store.next()

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Количество: ')
    await FSM_store.next()

async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await message.answer('Введите свои контактные данные: ')
    await FSM_store.next()

async def load_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text



def register_fsm_zak(dp: Dispatcher):
    dp.register_message_handler(start_fsm_zakaz, commands=['zakaz'])
    dp.register_message_handler(load_product_id, state=FSM_zakaz.product_id)
    dp.register_message_handler(load_size, state=FSM_zakaz.size)
    dp.register_message_handler(load_quantity, state=FSM_zakaz.quantity)
    dp.register_message_handler(load_phone_number, state=FSM_zakaz.phone_number)