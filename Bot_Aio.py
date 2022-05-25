import logging, os, json
import string
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)
bot = Bot(token='2079190388:AAEXaeRE8t-KklkCJIuzWcQqyJDN3cG6ueo')
dp = Dispatcher(bot)

async  def on_startup(_):
    print('Бот онлайн')

'''******************************КЛИЕНТСКАЯ ЧАСТЬ*******************************************'''

@dp.message_handler(commands=['start','help'])
async  def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id,f'Привет {message.from_user.full_name}')
        await message.delete()
    except:
        await message.reply('Общение через ЛС:')                #Если не добавлять бота, а писать срузу в группу



'''*********************************ОБЩАЯ ЧАСТЬ*********************************************'''

# @dp.message_handler()
# async def mat(message:types.Message):
#     """Запрещает все матерные сообщения"""
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
#         .intersection(set(json.load(open('cenz.json')))) != set():
#         await message.answer('Маты запрещены!')
#         await message.delete()



@dp.message_handler()
async def eacho_send(message:types.Message):
    """Принимает все входящие сообщения"""
    if message.text == 'id':
        await message.answer(message.from_user.id)
    elif message.text == 'name':
        await message.answer(message.from_user.full_name)



'''*******************************АДМИНСКАЯ ЧАСТЬ*******************************************'''


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)