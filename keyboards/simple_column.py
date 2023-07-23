# -*- coding: utf-8 -*-

from aiogram.types import InlineKeyboardMarkup, KeyboardButton


def make_column_keyboard(items: list[str]) -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру с кнопками в один столбец;
    :param items: список текстов для кнопок;
    :return: объект инлайн-клавиатуры.
    """

    column = [KeyboardButton(text=item) for item in items]
    return InlineKeyboardMarkup(keyboard=[column], resize_keyboard=True)
