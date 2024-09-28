from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

class FSM_store(StatesGroup):
    name_product = State()
    category = State()
    size = State()
    price = State()
    product_id = State()
    photo = State()
    submit = State()

async def start_fsm_store(message: types.Message):
    await message.answer('Введите название товара: ')
    await FSM_store.name_product.set()

async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text


    await message.answer('Категория товара: ')
    await FSM_store.next()

async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Размер товара: ')
    await FSM_store.next()

async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Цена товара: ')
    await FSM_store.next()

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Артикул товара: ')
    await FSM_store.next()

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Отправьте фото: ')
    await FSM_store.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer('Верные ли данные ?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Верные ли данные?\n\n'
                                       f'Название товара: {data["name_product"]}\n\n'
                                       f'Категория: {data["category"]}\n\n'
                                       f'Размер: {data["size"]}\n\n'
                                       f'Цена: {data["price"]}\n\n'
                                       f'Артикул: {data["product_id"]}\n\n')
    # await FSM_store.next()

async def submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        await message.answer('Отлично. Данные в базе!')

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!')

    else:
        await message.answer('Выберите "Да" или "Нет"')
    await state.finish()


def register_fsm_store(dp: Dispatcher):
    dp.register_message_handler(start_fsm_store, commands=['store'])
    dp.register_message_handler(load_name_product, state=FSM_store.name_product)
    dp.register_message_handler(load_category, state=FSM_store.category)
    dp.register_message_handler(load_size, state=FSM_store.size)
    dp.register_message_handler(load_price, state=FSM_store.price)
    dp.register_message_handler(load_product_id, state=FSM_store.product_id)
    dp.register_message_handler(load_photo, state=FSM_store.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit)
