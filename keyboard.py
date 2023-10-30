from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_spread = KeyboardButton("Спред")
button_fiks = KeyboardButton("Зафиксировать ТВХ")
button_set_proc = KeyboardButton("Сигнал по %")
button_del = KeyboardButton("Сбросить ТВХ")

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_spread, button_fiks).row(button_set_proc, button_del)

spread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
spread_keyboard.add(KeyboardButton("USD"))
spread_keyboard.add(KeyboardButton("EUR"))
spread_keyboard.add(KeyboardButton("CNY"))



