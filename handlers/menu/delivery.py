# -*- coding: utf-8 -*-
from aiogram import types, Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command

router = Router()


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
