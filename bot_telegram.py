import json
from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from keyboard import greet_kb1, spread_keyboard


token = '5814873337:AAFmEDxaPRXmg8w1HQ4FTiNB1U5l8pgtFgE'

bot = Bot(token)
dp = Dispatcher(bot)

current_datetime = datetime.now()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=greet_kb1)

@dp.message_handler(Text(equals="Спред"))
async def with_puree(message: types.Message):
    with open('request_pos.txt', 'w') as fw:
        status = 'request'
        json.dump(status, fw)
    mess = 'Выберите актив:'
    await bot.send_message(message.chat.id, mess, reply_markup=spread_keyboard)

# Обработчики для "Действие 1", "Действие 2" и "Действие 3"
@dp.message_handler(Text(equals="USD"))
async def action1(message: types.Message):
    # Здесь вы можете выполнять необходимые действия для "Действие 1"
    with open('usd.txt', 'r') as fr:
        mess = json.load(fr)
        await bot.send_message(message.chat.id, mess)

@dp.message_handler(Text(equals="EUR"))
async def action2(message: types.Message):
    # Здесь вы можете выполнять необходимые действия для "Действие 2"
    with open('eur.txt', 'r') as fr:
        mess = json.load(fr)
        await bot.send_message(message.chat.id, mess)

@dp.message_handler(Text(equals="CNY"))
async def action3(message: types.Message):
    # Здесь вы можете выполнять необходимые действия для "Действие 3"
    with open('cny.txt', 'r') as fr:
        mess = json.load(fr)
        await bot.send_message(message.chat.id, mess)

@dp.message_handler(Text(equals="Зафиксировать ТВХ"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    with open('balance.txt', 'r') as fr:
        # читаем из файла
        bal = json.load(fr)
        await bot.send_message(message.chat.id,bal)

@dp.message_handler(Text(equals="Сигнал по %"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    with open('balance.txt', 'r') as fr:
        # читаем из файла
        bal = json.load(fr)
        await bot.send_message(message.chat.id,bal)

@dp.message_handler(Text(equals="Сбросить ТВХ"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    with open('balance.txt', 'r') as fr:
        # читаем из файла
        bal = json.load(fr)
        await bot.send_message(message.chat.id,bal)

if __name__ == '__main__':
    executor.start_polling(dp)


