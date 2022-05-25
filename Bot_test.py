import logging
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram import Bot, Dispatcher, executor, md, types

API_TOKEN = '2079190388:AAEXaeRE8t-KklkCJIuzWcQqyJDN3cG6ueo'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)

URL = 'https://docs.aiogram.dev/en/dev-2.x/_static/logo.png'
@dp.message_handler(commands=['image, img'])
async def cmd_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))


# @dp.message_handler()
# async def check_language(message: types.Message):
#     await message.answer('asdkfjsdk')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)