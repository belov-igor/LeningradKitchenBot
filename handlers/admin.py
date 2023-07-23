# -*- coding: utf-8 -*-
from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text
from keyboards import admin_keyboards

import database as db
from config_reader import config

router = Router()


class FSMMenu(StatesGroup):
    type = State()
    name = State()
    description = State()
    price = State()
    photo = State()


# TODO сделать заглушки на админскую панель

# Вход в админ панель по нажатию кнопки
@router.message(Text(admin_keyboards.ADMIN_BUTTON_TEXT))
async def to_admin_panel(message: types.Message):
    admin_panel = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_keyboards.admin_panel_kb)
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await message.answer(text='Вы вошли в админ-панель!', reply_markup=admin_panel)


# Вернуться из админ-панели
@router.message(Text("Назад к заказам"))
async def back_to_orders(message: types.Message):
    admin_panel_button = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_keyboards.admin_buttons)
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await message.answer(text='Посмотрим, что заказали?', reply_markup=admin_panel_button)


# Загрузка нового пункта меню
# @router.message(Text("Добавить товар"), state=None)
# async def cmd_new_product(message: types.Message):
#     await FSMMenu.
    # pass


# @router.callback_query_handler(state=FSMMenu.type)
# async def add_item_type(call: types.CallbackQuery, state: types.FSMContext):
#     async with state.proxy() as data:
#         data['type'] = call.data
#     await call.message.answer('Напишите название товара', reply_markup=kb.cancel)
#     await FSMMenu.next()
#
#
# @router.message_handler(state=NewOrder.name)
# async def add_item_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await message.answer('Напишите описание товара')
#     await NewOrder.next()
#
#
# @router.message_handler(state=NewOrder.desc)
# async def add_item_desc(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['desc'] = message.text
#     await message.answer('Напишите цену товара')
#     await NewOrder.next()
#
#
# @router.message_handler(state=NewOrder.price)
# async def add_item_desc(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['price'] = message.text
#     await message.answer('Отправьте фотографию товара')
#     await NewOrder.next()
#
#
# @router.message_handler(lambda message: not message.photo, state=NewOrder.photo)
# async def add_item_photo_check(message: types.Message):
#     await message.answer('Это не фотография!')
#
#
# @router.message_handler(content_types=['photo'], state=NewOrder.photo)
# async def add_item_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#     await db.add_item(state)
#     await message.answer('Товар успешно создан!', reply_markup=kb.admin_panel)
#     await state.finish()
