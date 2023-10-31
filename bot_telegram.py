import json
from datetime import datetime
import os

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils import executor

from keyboard import greet_kb1, spread_keyboard, usd_fiks_keyboard, eur_fiks_keyboard, cny_fiks_keyboard, usd_yes_no_keyboard, eur_yes_no_keyboard, cny_yes_no_keyboard, usd_sbros_keyboard, eur_sbros_keyboard, cny_sbros_keyboard, signal_keyboard, usd_signal_keyboard, eur_signal_keyboard, cny_signal_keyboard, usd_signal_sbros_keyboard, eur_signal_sbros_keyboard, cny_signal_sbros_keyboard, signal_only_keyboard, usd_signal_only_keyboard, eur_signal_only_keyboard, cny_signal_only_keyboard, usd_signal_only_sbros_keyboard, eur_signal_only_sbros_keyboard, cny_signal_only_sbros_keyboard
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext, storage


class YourState(StatesGroup):
    new_usd = State()
    new_eur = State()
    new_cny = State()
    new_usd_only = State()
    new_eur_only = State()
    new_cny_only = State()



token = '5814873337:AAFmEDxaPRXmg8w1HQ4FTiNB1U5l8pgtFgE'

bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

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


@dp.message_handler(Text(equals="Текущая ТВХ USD"))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("usd_tvh.txt", "r") as file:
            tvh = file.read()
            if not tvh:
                await message.answer("Точка входа по USD не установлена", reply_markup=usd_fiks_keyboard)
            else:
                await message.answer(f"Точка входа по USD: {tvh}", reply_markup=usd_fiks_keyboard)
    except FileNotFoundError:
        await message.answer("Точка входа не найдена", reply_markup=usd_fiks_keyboard)


@dp.message_handler(Text(equals="Текущая ТВХ EUR"))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("eur_tvh.txt", "r") as file:
            tvh = file.read()
            if not tvh:
                await message.answer("Точка входа по EUR не установлена", reply_markup=eur_fiks_keyboard)
            else:
                await message.answer(f"Точка входа по EUR: {tvh}", reply_markup=eur_fiks_keyboard)
    except FileNotFoundError:
        await message.answer("Точка входа не найдена", reply_markup=eur_fiks_keyboard)



@dp.message_handler(Text(equals="Текущая ТВХ CNY"))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("cny_tvh.txt", "r") as file:
            tvh = file.read()
            if not tvh:
                await message.answer("Точка входа по CNY не установлена", reply_markup=cny_fiks_keyboard)
            else:
                await message.answer(f"Точка входа по CNY: {tvh}", reply_markup=cny_fiks_keyboard)
    except FileNotFoundError:
        await message.answer("Точка входа не найдена", reply_markup=cny_fiks_keyboard)


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
                    await message.answer(f"Точка входа {x} для USD зафиксирована.", reply_markup=usd_fiks_keyboard)
                else:
                    await message.answer("Не удалось найти точку входа для USD.", reply_markup=usd_fiks_keyboard)
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.", reply_markup=usd_fiks_keyboard)
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
                await message.answer(f"Точка входа {x} для USD зафиксирована.", reply_markup=usd_fiks_keyboard)
            else:
                await message.answer("Не удалось найти точку входа для USD.", reply_markup=usd_fiks_keyboard)

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
                    await message.answer(f"Точка входа {x} для USD зафиксирована.", reply_markup=eur_fiks_keyboard)
                else:
                    await message.answer("Не удалось найти точку входа для EUR.", reply_markup=eur_fiks_keyboard)
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.", reply_markup=eur_fiks_keyboard)
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
                await message.answer(f"Точка входа {x} для EUR зафиксирована.", reply_markup=eur_fiks_keyboard)
            else:
                await message.answer("Не удалось найти точку входа для USD.", reply_markup=eur_fiks_keyboard)

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
                    await message.answer(f"Точка входа {x} для USD зафиксирована.", reply_markup=cny_fiks_keyboard)
                else:
                    await message.answer("Не удалось найти точку входа для USD.", reply_markup=cny_fiks_keyboard)
        else:
            await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.", reply_markup=cny_fiks_keyboard)
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
                await message.answer(f"Точка входа {x} для CNY зафиксирована.", reply_markup=cny_fiks_keyboard)
            else:
                await message.answer("Не удалось найти точку входа для USD.", reply_markup=cny_fiks_keyboard)

@dp.message_handler(Text(equals="Сигнал изменения спреда от точки входа, %"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    mess = 'Выберите актив'
    await bot.send_message(message.chat.id, mess, reply_markup=signal_keyboard)





@dp.message_handler(Text(equals="USD, %"))
async def with_puree(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами
    await message.answer("Выберите действие:", reply_markup=usd_signal_keyboard)


@dp.message_handler(Text(equals="Текущий сигнал в % по USD"))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("usd_signal.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал по USD не установлен", reply_markup=usd_signal_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % от точки входа по USD: {signal}", reply_markup=usd_signal_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал не найден", reply_markup=usd_signal_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по USD"))
async def new_signal_usd(message: types.Message, state: FSMContext):
    # Запрашиваем новое значение сигнала и записываем его в файл
    await message.answer("Введите новое значение сигнала в % от точки входа по USD:")
    # Устанавливаем состояние для ожидания нового значения сигнала
    await YourState.new_usd.set()

@dp.message_handler(state=YourState.new_usd)
async def process_new_signal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        # Сохраняем новый сигнал в файл
        with open("usd_signal.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % от точки входа по USD установлен: {data['new_signal']}",
                             reply_markup=signal_keyboard)

    # Завершаем состояние FSMContext
    await state.finish()



@dp.message_handler(Text(equals="Сброс сигнала в % по USD"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить сигнал по USD?'
    await bot.send_message(message.chat.id, mess, reply_markup=usd_signal_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал USD"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'usd_signal.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Сигнал для USD сброшен.", reply_markup=usd_signal_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала.", reply_markup=usd_signal_keyboard)





@dp.message_handler(Text(equals="EUR, %"))
async def with_eur_signal(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами по EUR
    await message.answer("Выберите действие для EUR:", reply_markup=eur_signal_keyboard)

@dp.message_handler(Text(equals="Текущий сигнал в % по EUR"))
async def current_signal_eur(message: types.Message):
    try:
        with open("eur_signal.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал по EUR не установлен", reply_markup=eur_signal_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % от точки входа по EUR: {signal}", reply_markup=eur_signal_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал по EUR не найден", reply_markup=eur_signal_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по EUR"))
async def new_signal_eur(message: types.Message, state: FSMContext):
    await message.answer("Введите новое значение сигнала в % от точки входа по EUR:")
    await YourState.new_eur.set()

@dp.message_handler(state=YourState.new_eur)
async def process_new_signal_eur(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        with open("eur_signal.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % от точки входа по EUR установлен: {data['new_signal']}", reply_markup=signal_keyboard)

    await state.finish()


@dp.message_handler(Text(equals="Сброс сигнала в % по EUR"))
async def fix_eur_signal(message: types.Message):
    mess = 'Сбросить сигнал по EUR?'
    await bot.send_message(message.chat.id, mess, reply_markup=eur_signal_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал EUR"))
async def reset_eur_signal(message: types.Message):
    eur_signal_file = 'eur_signal.txt'

    if os.path.exists(eur_signal_file):
        with open(eur_signal_file, 'w', encoding='utf-8') as fw:
            pass
        await message.answer("Сигнал для EUR сброшен.", reply_markup=eur_signal_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала для EUR.", reply_markup=eur_signal_keyboard)





@dp.message_handler(Text(equals="CNY, %"))
async def with_eur_signal(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами по EUR
    await message.answer("Выберите действие для CNY:", reply_markup=cny_signal_keyboard)

@dp.message_handler(Text(equals="Текущий сигнал в % по CNY"))
async def current_signal_eur(message: types.Message):
    try:
        with open("cny_signal.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал от точки входа по CNY не установлен", reply_markup=cny_signal_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % от точки входа по CNY: {signal}", reply_markup=cny_signal_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал по EUR не найден", reply_markup=cny_signal_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по CNY"))
async def new_signal_eur(message: types.Message, state: FSMContext):
    await message.answer("Введите новое значение сигнала в % от точки входа по CNY:")
    await YourState.new_cny.set()

@dp.message_handler(state=YourState.new_cny)
async def process_new_signal_eur(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        with open("cny_signal.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % от точки входа по CNY установлен: {data['new_signal']}", reply_markup=signal_keyboard)

    await state.finish()


@dp.message_handler(Text(equals="Сброс сигнала в % по CNY"))
async def fix_eur_signal(message: types.Message):
    mess = 'Сбросить сигнал по CNY?'
    await bot.send_message(message.chat.id, mess, reply_markup=cny_signal_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал CNY"))
async def reset_eur_signal(message: types.Message):
    cny_signal_file = 'cny_signal.txt'

    if os.path.exists(cny_signal_file):
        with open(cny_signal_file, 'w', encoding='utf-8') as fw:
            pass
        await message.answer("Сигнал для CNY сброшен.", reply_markup=cny_signal_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала для CNY.", reply_markup=cny_signal_keyboard)






@dp.message_handler(Text(equals="Отмена"))
async def fix_usd_tvh(message: types.Message):
    mess = 'Выберите актив'
    await bot.send_message(message.chat.id, mess, reply_markup=signal_keyboard)

@dp.message_handler(Text(equals="Отмена."))
async def fix_usd_tvh(message: types.Message):
    mess = 'Выберите актив'
    await bot.send_message(message.chat.id, mess, reply_markup=signal_only_keyboard)

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
        await message.answer("Точка входа для USD сброшена.", reply_markup=usd_fiks_keyboard)
    else:
        await message.answer("Нет сохранённой точки входа.", reply_markup=usd_fiks_keyboard)

@dp.message_handler(Text(equals="Сбросить точку входа EUR"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'eur_tvh.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Точка входа для EUR сброшена.", reply_markup=eur_fiks_keyboard)
    else:
        await message.answer("Нет сохранённой точки входа.", reply_markup=eur_fiks_keyboard)

@dp.message_handler(Text(equals="Сбросить точку входа CNY"))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'cny_tvh.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Точка входа для CNY сброшена.", reply_markup=cny_fiks_keyboard)
    else:
        await message.answer("Нет сохранённой точки входа.", reply_markup=cny_fiks_keyboard)


@dp.message_handler(Text(equals="Сигнал изменения спреда, %"))
async def with_puree(message: types.Message):
    # открываем файл в режиме чтения
    mess = 'Выберите актив'
    await bot.send_message(message.chat.id, mess, reply_markup=signal_only_keyboard)


@dp.message_handler(Text(equals="USD. %"))
async def with_puree(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами
    await message.answer("Выберите действие:", reply_markup=usd_signal_only_keyboard)


@dp.message_handler(Text(equals="Текущий сигнал в % по USD."))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("usd_signal_only.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал по USD не установлен", reply_markup=usd_signal_only_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % по USD: {signal}", reply_markup=usd_signal_only_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал не найден", reply_markup=usd_signal_only_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по USD."))
async def new_signal_usd(message: types.Message, state: FSMContext):
    # Запрашиваем новое значение сигнала и записываем его в файл
    await message.answer("Введите новое значение сигнала в % по USD:")
    # Устанавливаем состояние для ожидания нового значения сигнала
    await YourState.new_usd_only.set()

@dp.message_handler(state=YourState.new_usd_only)
async def process_new_signal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        # Сохраняем новый сигнал в файл
        with open("usd_signal_only.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % по USD установлен: {data['new_signal']}",
                             reply_markup=signal_only_keyboard)

    # Завершаем состояние FSMContext
    await state.finish()
    with open('usd.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    x = None
    for line in lines:
        if "Спред Si - USDRUBF:" in line:
            parts = line.split()
            x_index = parts.index('Спред') + 4
            x = parts[x_index]
    with open("usd_spread_only.txt", "w") as file:
        pass
        file.write(x)

@dp.message_handler(Text(equals="Сброс сигнала в % по USD."))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить сигнал по USD?'
    await bot.send_message(message.chat.id, mess, reply_markup=usd_signal_only_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал USD."))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'usd_signal_only.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Сигнал для USD сброшен.", reply_markup=usd_signal_only_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала.", reply_markup=usd_signal_only_keyboard)


@dp.message_handler(Text(equals="EUR. %"))
async def with_puree(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами
    await message.answer("Выберите действие:", reply_markup=eur_signal_only_keyboard)


@dp.message_handler(Text(equals="Текущий сигнал в % по EUR."))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("eur_signal_only.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал по EUR не установлен", reply_markup=eur_signal_only_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % по EUR: {signal}", reply_markup=eur_signal_only_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал не найден", reply_markup=eur_signal_only_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по EUR."))
async def new_signal_usd(message: types.Message, state: FSMContext):
    # Запрашиваем новое значение сигнала и записываем его в файл
    await message.answer("Введите новое значение сигнала в % по USD:")
    # Устанавливаем состояние для ожидания нового значения сигнала
    await YourState.new_eur_only.set()

@dp.message_handler(state=YourState.new_eur_only)
async def process_new_signal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        # Сохраняем новый сигнал в файл
        with open("eur_signal_only.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % по EUR установлен: {data['new_signal']}",
                             reply_markup=signal_only_keyboard)

    # Завершаем состояние FSMContext
    await state.finish()
    with open('eur.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    x = None
    for line in lines:
        if "Спред Eu - EURRUBF:" in line:
            parts = line.split()
            x_index = parts.index('Спред') + 4
            x = parts[x_index]
    with open("eur_spread_only.txt", "w") as file:
        pass
        file.write(x)

@dp.message_handler(Text(equals="Сброс сигнала в % по EUR."))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить сигнал по EUR?'
    await bot.send_message(message.chat.id, mess, reply_markup=eur_signal_only_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал EUR."))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'eur_signal_only.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Сигнал для EUR сброшен.", reply_markup=eur_signal_only_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала.", reply_markup=eur_signal_only_keyboard)


@dp.message_handler(Text(equals="CNY. %"))
async def with_puree(message: types.Message):
    # Открываем клавиатуру с кнопками для управления сигналами
    await message.answer("Выберите действие:", reply_markup=cny_signal_only_keyboard)


@dp.message_handler(Text(equals="Текущий сигнал в % по CNY."))
async def current_signal_usd(message: types.Message):
    # Считываем текущий сигнал из файла и отправляем его пользователю
    try:
        with open("cny_signal_only.txt", "r") as file:
            signal = file.read()
            if not signal:
                await message.answer("Текущий сигнал по CNY не установлен", reply_markup=cny_signal_only_keyboard)
            else:
                await message.answer(f"Текущий сигнал в % по CNY: {signal}", reply_markup=cny_signal_only_keyboard)
    except FileNotFoundError:
        await message.answer("Сигнал не найден", reply_markup=cny_signal_only_keyboard)

@dp.message_handler(Text(equals="Новый сигнал в % по CNY."))
async def new_signal_usd(message: types.Message, state: FSMContext):
    # Запрашиваем новое значение сигнала и записываем его в файл
    await message.answer("Введите новое значение сигнала в % по CNY:")
    # Устанавливаем состояние для ожидания нового значения сигнала
    await YourState.new_cny_only.set()

@dp.message_handler(state=YourState.new_cny_only)
async def process_new_signal(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_signal'] = message.text

        # Сохраняем новый сигнал в файл
        with open("cny_signal_only.txt", "w") as file:
            file.write(data['new_signal'])
        await message.answer(f"Новый сигнал в % по CNY установлен: {data['new_signal']}",
                             reply_markup=signal_only_keyboard)

    # Завершаем состояние FSMContext
    await state.finish()
    with open('cny.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    x = None
    for line in lines:
        if "Спред Cny - CNYRUBF:" in line:
            parts = line.split()
            x_index = parts.index('Спред') + 4
            x = parts[x_index]
    with open("cny_spread_only.txt", "w") as file:
        pass
        file.write(x)

@dp.message_handler(Text(equals="Сброс сигнала в % по CNY."))
async def fix_usd_tvh(message: types.Message):
    mess = 'Сбросить сигнал по CNY?'
    await bot.send_message(message.chat.id, mess, reply_markup=cny_signal_only_sbros_keyboard)

@dp.message_handler(Text(equals="Сбросить сигнал CNY."))
async def reset_usd_tvh(message: types.Message):
    usd_tvh_file = 'cny_signal_only.txt'

    if os.path.exists(usd_tvh_file):
        with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
            pass  # Это создаст пустой файл, стирая всё содержимое
        await message.answer("Сигнал для CNY сброшен.", reply_markup=cny_signal_only_keyboard)
    else:
        await message.answer("Нет сохранённого сигнала.", reply_markup=cny_signal_only_keyboard)




if __name__ == '__main__':
    executor.start_polling(dp)


