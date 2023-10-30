from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_spread = KeyboardButton("Спред")
button_set_proc = KeyboardButton("Сигнал по %")


greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_spread, button_set_proc)
spread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD"), KeyboardButton("EUR")).row(KeyboardButton("CNY"), KeyboardButton("Главное меню"))

usd_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Актуальная ТВХ USD"), KeyboardButton("Новая ТВХ USD")).row(KeyboardButton("Сброс ТВХ USD"), KeyboardButton("Назад"))
eur_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Актуальная ТВХ EUR"), KeyboardButton("Новая ТВХ EUR")).row(KeyboardButton("Сброс ТВХ EUR"), KeyboardButton("Назад"))
cny_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Актуальная ТВХ CNY"), KeyboardButton("Новая ТВХ CNY")).row(KeyboardButton("Сброс ТВХ CNY"), KeyboardButton("Назад"))

usd_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа USD")).row(KeyboardButton("Назад"))
eur_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа EUR")).row(KeyboardButton("Назад"))
cny_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа CNY")).row(KeyboardButton("Назад"))

usd_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа USD")).row(KeyboardButton("Назад"))
eur_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа EUR")).row(KeyboardButton("Назад"))
cny_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа CNY")).row(KeyboardButton("Назад"))