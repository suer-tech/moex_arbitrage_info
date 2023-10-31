from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_spread = KeyboardButton("Спред")
button_set_proc_tvh = KeyboardButton("Сигнал изменения спреда от точки входа, %")
button_set_proc = KeyboardButton("Сигнал изменения спреда, %")


greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_spread).row(button_set_proc_tvh).row(button_set_proc)
spread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD"), KeyboardButton("EUR")).row(KeyboardButton("CNY"), KeyboardButton("Главное меню"))

usd_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ USD"), KeyboardButton("Новая ТВХ USD")).row(KeyboardButton("Сброс ТВХ USD"), KeyboardButton("Назад"))
eur_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ EUR"), KeyboardButton("Новая ТВХ EUR")).row(KeyboardButton("Сброс ТВХ EUR"), KeyboardButton("Назад"))
cny_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ CNY"), KeyboardButton("Новая ТВХ CNY")).row(KeyboardButton("Сброс ТВХ CNY"), KeyboardButton("Назад"))

usd_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа USD")).row(KeyboardButton("Назад"))
eur_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа EUR")).row(KeyboardButton("Назад"))
cny_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать новую точку входа CNY")).row(KeyboardButton("Назад"))

usd_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа USD")).row(KeyboardButton("Назад"))
eur_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа EUR")).row(KeyboardButton("Назад"))
cny_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа CNY")).row(KeyboardButton("Назад"))

signal_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD, %"), KeyboardButton("EUR, %")).row(KeyboardButton("CNY, %"), KeyboardButton("Главное меню"))

signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD. %"), KeyboardButton("EUR. %")).row(KeyboardButton("CNY. %"), KeyboardButton("Главное меню"))
usd_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по USD."), KeyboardButton("Новый сигнал в % по USD.")).row(KeyboardButton("Сброс сигнала в % по USD."), KeyboardButton("Отмена."))
eur_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по EUR."), KeyboardButton("Новый сигнал в % по EUR.")).row(KeyboardButton("Сброс сигнала в % по EUR."), KeyboardButton("Отмена."))
cny_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по CNY."), KeyboardButton("Новый сигнал в % по CNY.")).row(KeyboardButton("Сброс сигнала в % по CNY."), KeyboardButton("Отмена."))

usd_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал USD.")).row(KeyboardButton("Отмена."))
eur_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал EUR.")).row(KeyboardButton("Отмена."))
cny_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал CNY.")).row(KeyboardButton("Отмена."))


usd_signal_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по USD"), KeyboardButton("Новый сигнал в % по USD")).row(KeyboardButton("Сброс сигнала в % по USD"), KeyboardButton("Отмена"))
eur_signal_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по EUR"), KeyboardButton("Новый сигнал в % по EUR")).row(KeyboardButton("Сброс сигнала в % по EUR"), KeyboardButton("Отмена"))
cny_signal_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по CNY"), KeyboardButton("Новый сигнал в % по CNY")).row(KeyboardButton("Сброс сигнала в % по CNY"), KeyboardButton("Отмена"))

usd_signal_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал USD")).row(KeyboardButton("Отмена"))
eur_signal_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал EUR")).row(KeyboardButton("Отмена"))
cny_signal_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал CNY")).row(KeyboardButton("Отмена"))