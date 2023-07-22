# -*- coding: utf-8 -*-
from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder

import database as db

router = Router()


# Оставлю пока для процесса заказа
# builder.row(types.InlineKeyboardButton(text="Запросить геолокацию", request_location=True))


# Хэндлер на команду /order
@router.message(Command("order"))
async def cmd_order(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="🥟 Пельмени", callback_data="dumpling_1"))
    builder.add(types.InlineKeyboardButton(
        text="🍲 Супы", callback_data="soups"))
    builder.row(types.InlineKeyboardButton(
        text="🥗 Салаты", callback_data="salads"))
    builder.row(types.InlineKeyboardButton(
        text="🫙 Соусы", callback_data="sauces"))
    builder.adjust(1)
    await message.answer("У нас вы можете заказать следующие позиции Ваших любимых продуктов",
                         reply_markup=builder.as_markup())


# Хэндлер на команду /delivery
@router.message(Command("delivery"))
async def cmd_delivery(message: types.Message):
    file_ids = []

    delivery_text = "<b>Самовывоз и доставка:</b>\n\n" \
                    "Доставка по Детелинаре (район подсвечен красным) и самовывоз - бесплатно\n\n" \
                    "Доставка по Нови Саду - 200 динар\n\n"

    image = types.FSInputFile("pics/detelinara_map.jpeg")
    result = await message.answer_photo(image, caption=delivery_text)
    file_ids.append(result.photo[-1].file_id)

    # Кнопки со ссылками на карты
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Yandex.Карты", url="https://yandex.ru/maps/org/173930265463"))
    builder.row(types.InlineKeyboardButton(
        text="Google Maps", url="https://maps.app.goo.gl/TD69ejkLtFyQ39Ms9?g_st=ic"))
    await message.answer("<b>Самовывоз производится по адресу:</b>\n\n"
                         "Нови Сад, Илиje Бирчанина, 31", reply_markup=builder.as_markup())


# Хэндлер на команду /information
@router.message(Command("information"))
async def cmd_information(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Ссылка на Instagram", url="https://instagram.com/leningrad_kitchen"))
    await message.answer("Душещипательный текст про дворы и Leningrad Kitchen\n\n"
                         "И подписывайтесь на <b>наш Instagram</b>. Там всё красиво и по акции",
                         reply_markup=builder.as_markup())


# Хэндлер на callback-команду dumplings
@router.callback_query(Text("dumpling_1"))
async def dumplings(callback: types.CallbackQuery):
    file_ids = []

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_2"))
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
