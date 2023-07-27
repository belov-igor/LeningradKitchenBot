# -*- coding: utf-8 -*-
from aiogram import types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command

router = Router()


# Хэндлер на команду /information
@router.message(Command("information"))
async def cmd_information(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Ссылка на Instagram", url="https://instagram.com/leningrad_kitchen"))
    await message.answer("Душещипательный текст про дворы и Leningrad Kitchen\n\n"
                         "И подписывайтесь на <b>наш Instagram</b>. Там всё красиво и по акции",
                         reply_markup=builder.as_markup())
