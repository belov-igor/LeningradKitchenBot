# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Общая клавиатура для каталога
calalog_list = InlineKeyboardBuilder()
calalog_list.row(types.InlineKeyboardButton(text="🥟 Пельмени", callback_data="dumplings"))
calalog_list.row(types.InlineKeyboardButton(text="🍲 Супы", callback_data="soups"))
# calalog_list.row(types.InlineKeyboardButton(text="Котлеты", callback_data="cutlets"))
calalog_list.row(types.InlineKeyboardButton(text="🥗 Салаты", callback_data="salads"))
calalog_list.row(types.InlineKeyboardButton(text="🫙 Соусы", callback_data="sauces"))


# Кл
def get_keyboard(index: int):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(types.InlineKeyboardButton(text="⬅️", callback_data=f"prev_{index}"))
    keyboard.add(types.InlineKeyboardButton(text="➡️", callback_data=f"next_{index}"))
    keyboard.row(types.InlineKeyboardButton(text="Заказать", callback_data="order"),
                 types.InlineKeyboardButton(text="Назад", callback_data="back"))
    return keyboard
