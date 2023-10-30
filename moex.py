from FinamPy import FinamPy
from FinamPy.Config import Config

if __name__ == '__main__':
    write_to_file = lambda filename, content: open(filename, "w").write(content)
    # Создаем экземпляр FinamPy и подключаемся с использованием токена доступа
    fp_provider = FinamPy(Config.AccessToken)

    # Определяем тикеры и площадки
    tickers = [
        ('CETS', 'USDRUB'),   # USDRUB
        ('FUT', 'SiZ3'),      # SIZ3
        ('CETS', 'USDRUBF')   # USDRUBF
    ]

    # Создаем словарь для хранения цен по активам
    asset_prices = {}
    write_to_file = lambda filename, content: open(filename, "w").write(content)

    # Запрашиваем цены по каждому активу
    for board, code in tickers:

        fp_provider.on_order_book = lambda order_book: write_to_file("price_moex.txt", f'{code}: {order_book.asks[0].price}')  # Обработчик события прихода подписки на стакан
        fp_provider.subscribe_order_book(code, board, 'orderbook1')  # Подписываемся на стакан тикера
        fp_provider.unsubscribe_order_book('orderbook1', code, board)  # Отписываемся от стакана тикера
        fp_provider.close_channel()  # Закрываем канал перед выходом

    # Выводим цены активов
    for code, price in asset_prices.items():
        print(f'Цена для {code}: {price}')

    # Рассчитываем разницу в процентах между активами
    if 'USDRUB' in asset_prices and 'SIZ3' in asset_prices and 'USDRUBF' in asset_prices:
        usdrub_price = asset_prices['USDRUB']
        siz3_price = asset_prices['SIZ3']
        usdrubf_price = asset_prices['USDRUBF']

        # Расчет разницы в процентах
        price_difference = ((usdrub_price - siz3_price) / siz3_price) * 100
        price_difference_usdrubf = ((usdrubf_price - siz3_price) / siz3_price) * 100

        print(f'Разница между USDRUB и SIZ3: {price_difference:.2f}%')
        print(f'Разница между USDRUBF и SIZ3: {price_difference_usdrubf:.2f}%')

    # Закрываем канал
    fp_provider.close_channel()
