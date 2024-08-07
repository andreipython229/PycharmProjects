import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
#from aiogram.utils import executor
import os
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

API_TOKEN
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Чтобы увидеть танцующего кота наберите /cat")
    #await message.answer("/cat")

@dp.message(Command("cat"))
async def cmd_cat(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кот танцует"), types.KeyboardButton(text="Фото кота")],
         ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("cat", reply_markup=keyboard)

# Обработка кнопок
@dp.message(F.text == 'Кот танцует')
async def cat_dance(message: types.Message):
    img_cat = FSInputFile('ioh0p.gif')
    await bot.send_animation(message.chat.id, img_cat)

@dp.message(F.text == 'Фото кота')
async def cat_photo(message: types.Message):
    gif = FSInputFile('ioh0p.gif')
    await bot.send_photo(message.chat.id, caption='Фото кота', photo=gif)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
