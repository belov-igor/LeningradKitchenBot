# -*- coding: utf-8 -*-
# from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton


# Кнопка админской клавиатуры (админ-панель)
ADMIN_BUTTON_TEXT = "Админ-панель"
admin_buttons = [
    [KeyboardButton(text="Посмотреть заказы")],
    [KeyboardButton(text=ADMIN_BUTTON_TEXT)],
]
admin_panel_button = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_buttons)

# Админ-панель
admin_panel_kb = [
    [KeyboardButton(text="Изменить товар")],
    [KeyboardButton(text="Добавить товар")],
    [KeyboardButton(text="Удалить товар")],
    [KeyboardButton(text="Назад к заказам")],
]
admin_panel = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_panel_kb)

#
cancel = ReplyKeyboardBuilder()
cancel.add(KeyboardButton(text="Отмена"))

# TODO добавить клаву в админку
# by_weight_kb = InlineKeyboardBuilder()
#     by_weight_kb.row(types.InlineKeyboardButton(text="На развес", callback_data="1"))
#     by_weight_kb.row(types.InlineKeyboardButton(text="Поштучно (порционно)", callback_data="0"))

