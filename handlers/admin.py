# -*- coding: utf-8 -*-
from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text

from keyboards import admin_kb
from keyboards import client_kb

from config_reader import config

router = Router()


class FSMMenu(StatesGroup):
    type = State()
    name = State()
    by_weight = State()
    description = State()
    price = State()
    photo = State()


# TODO сделать заглушки на админскую панель

# Вход в админ панель по нажатию кнопки
@router.message(Text(admin_kb.ADMIN_BUTTON_TEXT))
async def to_admin_panel(message: types.Message):
    admin_panel = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_kb.admin_panel_kb)
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await message.answer(text='Вы вошли в админ-панель!', reply_markup=admin_panel)


# Вернуться из админ-панели
@router.message(Text("Назад к заказам"))
async def back_to_orders(message: types.Message):
    admin_panel_button = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_kb.admin_buttons)
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await message.answer(text='Посмотрим, что заказали?', reply_markup=admin_panel_button)


# Загрузка нового пункта меню
@router.message(Text("Добавить товар"))
async def add_item(message: types.Message, state: FSMContext):
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await state.set_state(FSMMenu.type)
        await message.answer(text="Надо выбрать тип продукта:", reply_markup=client_kb.calalog_list.as_markup())
    else:
        await message.answer("Я тебя не понимаю")


@router.callback_query(FSMMenu.type)
async def add_item_type(call: types.callback_query, state: FSMContext):
    await state.update_data(type=call.data)
    await call.message.answer('Напиши название товара')
    await state.set_state(FSMMenu.name)


@router.message(FSMMenu.name)
async def add_item_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Это на развес (1) или поштучно (0)?')  # TODO сделать обработку кнопками или что
    await state.set_state(FSMMenu.by_weight)


@router.message(FSMMenu.by_weight)
async def add_item_by_weight(message: types.Message, state: FSMContext):
    await state.update_data(by_weight=message.text)
    await message.answer('Напиши описание продукта')
    await state.set_state(FSMMenu.description)


@router.message(FSMMenu.description)
async def add_item_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    if data['by_weight'] == 1:
        _ = "1 кг"
    else:
        _ = "1 порции (шт.)"  # TODO написать нормально ветвление
    await message.answer(f'Напиши цену {_} продукта')
    await state.set_state(FSMMenu.price)


@router.message(FSMMenu.price)
async def add_item_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Добавь фото продукта')
    await state.set_state(FSMMenu.photo)


# Проверка на фотографию
@router.message(lambda message: not message.photo, FSMMenu.photo)
async def add_item_photo_check(message: types.Message):
    await message.answer('Это не фотография!')
#
#
@router.message(FSMMenu.photo, content_types=['photo'])
async def add_item_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await db.add_item(state)
    await message.answer('Товар успешно создан!', reply_markup=admin_kb.admin_buttons)
    print(await state.get_data())
    # await state.
