# -*- coding: utf-8 -*-
from aiogram.filters.command import Command
from aiogram import Router, types

import database as db
from config_reader import config

from keyboards import admin_keyboards


router = Router()


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_order(message: types.Message):
    await db.cmd_start_db(message.from_user.id)
    file_ids = []

    welcome_text = "добро пожаловать в Leningrad Kitchen, наше вкусное сообщество бла-бла \n" \
                   "здесь вы можете заказать всякое, нажимая на кнопочки в меню ниже"

    image = types.FSInputFile("pics/logo.jpeg")
    result = await message.answer_photo(image, caption=f'{message.from_user.first_name}, {welcome_text}')
    file_ids.append(result.photo[-1].file_id)

    # Подключение админской клавиатуры
    admin_panel_button = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=admin_keyboards.admin_buttons)
    if message.from_user.id == int(config.admin_id.get_secret_value()):
        await message.answer(text='Вы авторизовались как администратор!', reply_markup=admin_panel_button)
