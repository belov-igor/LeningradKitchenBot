# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

calalog_list = InlineKeyboardBuilder()
calalog_list.row(types.InlineKeyboardButton(text="🥟 Пельмени", callback_data="dumplings"))
calalog_list.row(types.InlineKeyboardButton(text="🍲 Супы", callback_data="soups"))
calalog_list.row(types.InlineKeyboardButton(text="🥗 Салаты", callback_data="salads"))
calalog_list.row(types.InlineKeyboardButton(text="🫙 Соусы", callback_data="sauces"))

