# -*- coding: utf-8 -*-
from aiogram import types

# Кнопка админской клавиатуры (админ-панель)
ADMIN_BUTTON_TEXT = "Админ-панель"
admin_buttons = [
    [types.KeyboardButton(text="Посмотреть заказы")],
    [types.KeyboardButton(text=ADMIN_BUTTON_TEXT)],
]

# Админ-панель
admin_panel_kb = [
    [types.KeyboardButton(text="Изменить товар")],
    [types.KeyboardButton(text="Добавить товар")],
    [types.KeyboardButton(text="Удалить товар")],
    [types.KeyboardButton(text="Назад к заказам")],
]
