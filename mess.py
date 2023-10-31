import telebot
import os
import time
import chardet

token = '5814873337:AAFmEDxaPRXmg8w1HQ4FTiNB1U5l8pgtFgE'
bot = telebot.TeleBot(token, parse_mode=None)
users_id = [412850740]  # Замените на свой список ID пользователей

def send_message(txt_file):
    if os.path.exists(txt_file) and os.stat(txt_file).st_size > 0:
        encoding = detect_encoding(txt_file)
        with open(txt_file, 'r', encoding=encoding) as fr:
            mess = fr.read()
        for user in users_id:
            try:
                bot.send_message(user, mess)
            except Exception as e:
                print(f"Error sending message to user {user}: {e}")
        with open(txt_file, 'w') as fw:
            pass

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

while True:
    time.sleep(1)
    send_message('sig_proc.txt')

bot.polling(none_stop=True)



