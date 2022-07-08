from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Команда 1')
b2 = KeyboardButton('/Команда 3')
b3 = KeyboardButton('/Команда 2')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1)