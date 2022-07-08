from aiogram import types, Dispatcher
from create_bot import dp, bot


# @dp.message_handler(commands=['start','help'])
async  def command_start(message:types.Message):
    try:
        await bot.send_message(message.from_user.id,f'Привет {message.from_user.full_name}')
        await message.delete()
    except:
        await message.reply('Общение через ЛС:')                #Если не добавлять бота, а писать срузу в группу

# @dp.message_handler(content_types='text')
async def info_send(message:types.Message):
    """Принимает все входящие сообщения"""
    if message.text == 'id':
        await message.answer(message.from_user.id)
    elif message.text == 'name':
        await message.answer(message.from_user.full_name)

def register_handlers_client(dp:Dispatcher):
    dp.register_message_handler(command_start,commands=['start','help'])
    dp.register_message_handler(info_send,content_types='text')