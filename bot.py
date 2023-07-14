import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /order
@dp.message(Command("order"))
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
    await message.answer("У нас вы можете заказать следующие позиции Ваших любимых продуктов",
                         reply_markup=builder.as_markup())


# Хэндлер на команду /delivery
@dp.message(Command("delivery"))
async def cmd_delivery(message: types.Message):
    file_ids = []

    delivery_text = "<b>Самовывоз и доставка:</b>\n\n" \
                    "Доставка по Детелинаре (район подсвечен красным) и самовывоз - бесплатно\n\n" \
                    "Доставка по Нови Саду - 200 динар\n\n"

    image = FSInputFile("pics/detelinara_map.jpeg")
    result = await message.answer_photo(image, caption=delivery_text)
    file_ids.append(result.photo[-1].file_id)

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Yandex.Карты", url="https://yandex.ru/maps/org/173930265463"))
    builder.row(types.InlineKeyboardButton(
        text="Google Maps", url="https://maps.app.goo.gl/TD69ejkLtFyQ39Ms9?g_st=ic"))
    await message.answer("<b>Самовывоз производится по адресу:</b>\n\n"
                         "Нови Сад, Илиje Бирчанина, 31", reply_markup=builder.as_markup())


@dp.message(Command("information"))
async def cmd_information(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Ссылка на Instagram", url="https://instagram.com/leningrad_kitchen"))
    await message.answer("Душещипательный текст про дворы и Leningrad Kitchen\n\n"
                         "И подписывайтесь на <b>наш Instagram</b>. Там всё красиво и по акции",
                         reply_markup=builder.as_markup())


# Хэндлер на callback-команду dumplings
@dp.callback_query(Text("dumpling_1"))
async def dumplings(callback: types.CallbackQuery):
    file_ids = []

    image = FSInputFile("pics/istockphoto-1392550147-612x612.jpg")
    result = await callback.message.answer_photo(image, caption="Петроградские")
    file_ids.append(result.photo[-1].file_id)

    # builder = InlineKeyboardBuilder()
    #
    # builder.add(types.InlineKeyboardButton(text="Заказать", callback_data="order"))
    # builder.add(types.InlineKeyboardButton(text="➡️️", callback_data="dumpling_2"))
    # builder.add(types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_3"))
    # builder.add(types.InlineKeyboardButton(text="Назад", callback_data="order"))

    buttons = [
        [types.InlineKeyboardButton(text="Заказать", callback_data="order")],
        [
            types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_3"),
            types.InlineKeyboardButton(text="⬅️", callback_data="dumpling_3")
        ],
        [types.InlineKeyboardButton(text="Назад", command="order")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer("По пельменям у нас есть вот такие позиции:", reply_markup=keyboard)


# Хэндлер на callback-команду soups
@dp.callback_query(Text("soups"))
async def soups(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали категорию супы")


# Хэндлер на callback-команду salads
@dp.callback_query(Text("salads"))
async def salads(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали категорию салаты")


# Хэндлер на callback-команду sauces
@dp.callback_query(Text("sauces"))
async def sauces(callback: types.CallbackQuery):
    await callback.message.answer("Вы выбрали категорию соусы")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Оставлю пока для процесса заказа
# builder.row(types.InlineKeyboardButton(text="Запросить геолокацию", request_location=True))


if __name__ == "__main__":
    asyncio.run(main())
