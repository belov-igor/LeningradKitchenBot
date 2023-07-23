import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import client, admin, common
from config_reader import config

import database as db


# TODO пощупать, решить, как правильнее реализовать подключение к базе
# async def on_startup(_):
#     await db.db_start()
#     print('bd starting')


# для получения id
# @dp.message(Command("id"))
# async def cmd_id(message: types.Message):
#     await message.answer(f'{message.from_user.id}')


async def main():
    # Запуск логгирования
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Объект бота и диспетчер
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрация роутеров
    dp.include_routers(client.router, admin.router, common.router)

    # Пропускаем все накопленные входящие и запускаем процесс поллинга новых апдейтов
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)

    # Старт базы данных
    await db.db_start()


if __name__ == "__main__":
    asyncio.run(main())
