# -*- coding: utf-8 -*-
from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

import dbconnect as db
from handlers.menu import information, delivery
from keyboards import client_kb

router = Router()

image_file_names = [
    "/Users/bisgarik/PycharmProjects/LeningradKitchenBot/pics/detelinara_map.jpeg",
    "/Users/bisgarik/PycharmProjects/LeningradKitchenBot/pics/istockphoto-1392550147-612x612.jpg",
    "/Users/bisgarik/PycharmProjects/LeningradKitchenBot/pics/logo.jpeg"
]

# Список с описаниями для каждой картинки
image_captions = [
    "Карта Детелинары",
    "Картинка с Интернета",
    "Логотип бота"
]

# Оставлю пока для процесса заказа
# builder.row(types.InlineKeyboardButton(text="Запросить геолокацию", request_location=True))

# Роутер на команду /delivery
router.include_router(delivery.router)

# Роутер на команду /information
router.include_router(information.router)


# Хэндлер на команду /order
@router.message(Command("order"))
async def cmd_order(message: types.Message):
    # Клавиатура из client_kb
    await message.answer("У нас вы можете заказать следующие позиции Ваших любимых продуктов",
                         reply_markup=client_kb.calalog_list.as_markup())


# Хэндлер на callback-команду dumplings
@router.callback_query(Text("dumplings"))
async def dumplings(callback: types.CallbackQuery):
    file_ids = []

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_3"))
    builder.add(types.InlineKeyboardButton(text="➡️️", callback_data="dumpling_2"))
    builder.add(types.InlineKeyboardButton(text="Заказать", callback_data="order"))
    builder.add(types.InlineKeyboardButton(text="Назад", callback_data="order"))
    builder.adjust(2)

    await callback.message.answer(text="По пельменям у нас есть вот такие позиции:")

    image = types.FSInputFile("pics/istockphoto-1392550147-612x612.jpg")
    photo = await callback.message.answer_photo(image, caption="Петроградские", reply_markup=builder.as_markup())
    file_ids.append(photo.photo[-1].file_id)


@router.callback_query(Text("dumpling_2"))
async def dumplings(callback: types.CallbackQuery):
    file_ids = []

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_1"))
    builder.add(types.InlineKeyboardButton(text="➡️️", callback_data="dumpling_3"))
    builder.add(types.InlineKeyboardButton(text="Заказать", callback_data="order"))
    builder.add(types.InlineKeyboardButton(text="Назад", callback_data="order"))
    builder.adjust(2)

    await callback.message.answer(text="По пельменям у нас есть вот такие позиции:")

    image = types.FSInputFile("pics/istockphoto-1392550147-612x612.jpg")
    photo = await callback.message.answer_photo(image, caption="Петроградские", reply_markup=builder.as_markup())
    file_ids.append(photo.photo[-1].file_id)


# Хэндлер на callback-команду soups
@router.callback_query(Text("soups"))
async def soups(callback: types.CallbackQuery):
    await callback.message.answer(text="Вы выбрали категорию супы")


# Хэндлер на callback-команду salads
@router.callback_query(Text("salads"))
async def salads(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали категорию салаты")


# Хэндлер на callback-команду sauces
@router.callback_query(Text("sauces"))
async def sauces(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали категорию соусы")
    ss = await db.get_dishes("sauces")
    print(ss)
    await callback.message.answer_photo(ss[0][-1])

