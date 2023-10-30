import telebot
import os
import time
import json
import os

token = '6419893616:AAG-tbu524ZN7IGIulbJA_ZxNLykdaJWeU0'
bot = telebot.TeleBot(token, parse_mode = None)
users_id = [412850740]

def send_message(txt_file):
    if os.stat(txt_file).st_size > 0:
        with open(txt_file, 'r') as fr:
            mess = json.load(fr)
        for user in users_id:
            try:
                bot.send_message(user, mess)
            except:
                continue
        with open(txt_file, 'w') as fw:
            pass

while True:
    time.sleep(1)
    try:
        send_message('usd.txt')
        send_message('eur.txt')
        send_message('cny.txt')


    except json.decoder.JSONDecodeError as err:
        bot.send_message(users_id[0], 'Ошибка: ' + str(err))

bot.infinity_polling()


