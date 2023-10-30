import json
from datetime import datetime
import os
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from keyboard import greet_kb1, spread_keyboard, usd_fiks_keyboard, eur_fiks_keyboard, cny_fiks_keyboard, usd_yes_no_keyboard, eur_yes_no_keyboard, cny_yes_no_keyboard, usd_sbros_keyboard, eur_sbros_keyboard, cny_sbros_keyboard


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

    with open('usd.txt', 'r', encoding='utf-8') as fr:
        mess = fr.read()  # Corrected to call the read() method
        await bot.send_message(message.chat.id, mess, reply_markup=usd_fiks_keyboard)

@dp.message_handler(Text(equals="EUR"))
async def action1(message: types.Message):
    # Здесь вы можете выполнять необходимые действия для "Действие 1"
    with open('eur.txt', 'r', encoding='utf-8') as fr:
        mess = fr.read()  # Corrected to call the read() method
        await bot.send_message(message.chat.id, mess, reply_markup=eur_fiks_keyboard)

@dp.message_handler(Text(equals="CNY"))
async def action1(message: types.Message):
    # Здесь вы можете выполнять необходимые действия для "Действие 1"
    with open('cny.txt', 'r', encoding='utf-8') as fr:
        mess = fr.read()  # Corrected to call the read() method
        await bot.send_message(message.chat.id, mess, reply_markup=cny_fiks_keyboard)


@dp.message_handler(Text(equals="Главное меню"))
async def back_to_previous_menu(message: types.Message):
    mess = 'Главное меню'
    await bot.send_message(message.chat.id, mess, reply_markup=greet_kb1)

@dp.message_handler(Text(equals="Назад"))
async def back_to_previous_menu(message: types.Message):
    mess = 'Выберите актив:'
    await bot.send_message(message.chat.id, mess, reply_markup=spread_keyboard)


@dp.message_handler(Text(equals="Новая ТВХ USD"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Зафиксировать новую точку входа по USD?'
    await bot.send_message(message.chat.id, mess, reply_markup=usd_yes_no_keyboard)

@dp.message_handler(Text(equals="Новая ТВХ EUR"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Зафиксировать новую точку входа по EUR?'
    await bot.send_message(message.chat.id, mess, reply_markup=eur_yes_no_keyboard)

@dp.message_handler(Text(equals="Новая ТВХ CNY"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Зафиксировать новую точку входа по CNY?'
    await bot.send_message(message.chat.id, mess, reply_markup=cny_yes_no_keyboard)


@dp.message_handler(Text(equals="Зафиксировать новую точку входа USD"))
async def fix_usd_tvh(message: types.Message):
    usd_tvh_file = 'usd_tvh.txt'

    if os.path.exists(usd_tvh_file):
        # Проверьте, является ли файл пустым
        is_empty = not bool(open(usd_tvh_file, 'r', encoding='utf-8').read())

        if is_empty:
            with open(usd_tvh_file, 'a', encoding='utf-8') as fw:
                with open('usd.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                x = None
                for line in lines:
                    if "Спред Si - USDRUBF:" in line:
                        parts = line.split()
                        x_index = parts.index('Спред') + 4
                        x = parts[x_index]
                        break

                if x is not None:
                    data_to_write = x
                    fw.write(data_to_write)
                    await message.answer(f"Точка входа {x} для USD зафиксирована.")
                else:
                    await message.answer("Не удалось найти точку входа для USD.")
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.")
    else:
        # Файл не существует, создайте его и записывайте информацию
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            with open('usd.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            x = None
            for line in lines:
                if "Спред Si - USDRUBF:" in line:
                    parts = line.split()
                    x_index = parts.index('Спред') + 4
                    x = parts[x_index]
                    break

            if x is not None:
                data_to_write = x
                fw.write(data_to_write)
                await message.answer(f"Точка входа {x} для USD зафиксирована.")
            else:
                await message.answer("Не удалось найти точку входа для USD.")

@dp.message_handler(Text(equals="Зафиксировать новую точку входа EUR"))
async def fix_usd_tvh(message: types.Message):
    usd_tvh_file = 'eur_tvh.txt'

    if os.path.exists(usd_tvh_file):
        # Проверьте, является ли файл пустым
        is_empty = not bool(open(usd_tvh_file, 'r', encoding='utf-8').read())

        if is_empty:
            with open(usd_tvh_file, 'a', encoding='utf-8') as fw:
                with open('eur.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                x = None
                for line in lines:
                    if "Спред Eu - EURRUBF:" in line:
                        parts = line.split()
                        x_index = parts.index('Спред') + 4
                        x = parts[x_index]
                        break

                if x is not None:
                    data_to_write = x
                    fw.write(data_to_write)
                    await message.answer(f"Точка входа {x} для USD зафиксирована.")
                else:
                    await message.answer("Не удалось найти точку входа для EUR.")
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.")
    else:
        # Файл не существует, создайте его и записывайте информацию
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            with open('eur.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            x = None
            for line in lines:
                if "Спред Eu - EURRUBF:" in line:
                    parts = line.split()
                    x_index = parts.index('Спред') + 4
                    x = parts[x_index]
                    break

            if x is not None:
                data_to_write = x
                fw.write(data_to_write)
                await message.answer(f"Точка входа {x} для EUR зафиксирована.")
            else:
                await message.answer("Не удалось найти точку входа для USD.")

@dp.message_handler(Text(equals="Зафиксировать новую точку входа CNY"))
async def fix_usd_tvh(message: types.Message):
    usd_tvh_file = 'cny_tvh.txt'

    if os.path.exists(usd_tvh_file):
        # Проверьте, является ли файл пустым
        is_empty = not bool(open(usd_tvh_file, 'r', encoding='utf-8').read())

        if is_empty:
            with open(usd_tvh_file, 'a', encoding='utf-8') as fw:
                with open('cny.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                x = None
                for line in lines:
                    if "Спред Cny - CNYRUBF:" in line:
                        parts = line.split()
                        x_index = parts.index('Спред') + 4
                        x = parts[x_index]
                        break

                if x is not None:
                    data_to_write = x
                    fw.write(data_to_write)
                    await message.answer(f"Точка входа {x} для USD зафиксирована.")
                else:
                    await message.answer("Не удалось найти точку входа для USD.")
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.")
    else:
        # Файл не существует, создайте его и записывайте информацию
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            with open('cny.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            x = None
            for line in lines:
                if "Спред Cny - CNYRUBF:" in line:
                    parts = line.split()
                    x_index = parts.index('Спред') + 4
                    x = parts[x_index]
                    break

            if x is not None:
                data_to_write = x
                fw.write(data_to_write)
                await message.answer(f"Точка входа {x} для CNY зафиксирована.")
            else:
                await message.answer("Не удалось найти точку входа для USD.")

@dp.message_handler(Text(equals="Сигнал по %"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    with open('balance.txt', 'r') as fr:
        # читаем из файла
        bal = json.load(fr)
        await bot.send_message(message.chat.id,bal)

@dp.message_handler(Text(equals="Сброс ТВХ USD"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить точку входа по USD?'
    await bot.send_message(message.chat.id, mess, reply_markup=usd_sbros_keyboard)

@dp.message_handler(Text(equals="Сброс ТВХ EUR"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить точку входа по EUR?'
    await bot.send_message(message.chat.id, mess, reply_markup=eur_sbros_keyboard)

@dp.message_handler(Text(equals="Сброс ТВХ CNY"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить точку входа по CNY?'
    await bot.send_message(message.chat.id, mess, reply_markup=cny_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить точку входа USD"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'usd_tvh.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Точка входа для USD сброшена.")
    else:
        await message.answer("Нет сохранённой точки входа.")

@dp.message_handler(Text(equals="Сбросить точку входа EUR"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'eur_tvh.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Точка входа для EUR сброшена.")
    else:
        await message.answer("Нет сохранённой точки входа.")

@dp.message_handler(Text(equals="Сбросить точку входа CNY"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'cny_tvh.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Точка входа для CNY сброшена.")
    else:
        await message.answer("Нет сохранённой точки входа.")




if __name__ == '__main__':
    executor.start_polling(dp)


