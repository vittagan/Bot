from aiogram import types, Dispatcher
import json, string
from create_bot import dp

# @dp.message_handler()
async def mat(message:types.Message):
    """Запрещает все матерные сообщения в файле cenz.json"""
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.answer('Маты запрещены!')
        await message.delete()

def register_handlers_other(dp:Dispatcher):
    dp.register_message_handler(mat)