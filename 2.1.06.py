'''Дан словарь crypto, в котором ключами являются названия криптовалют, значениями их курсы.
На вход подается название криптовалюты(строка). Необходимо вывести ее курс,
если она присутствует в словаре, либо:

Нет данных по <название криптовалюты>'''


crypto = {
    'Биткоин': 38.623,
    'Эфириум': 2092.98,
    'USDt': 1.0002,
    'BNB': 228.60,
    'XRP': 0.60898,
    'Solana': 60.995,
    'USD Coin': 0.9995,
    'Cardano': 0.3813,
    'Dogecoin': 0.083747,
    }
unit = input()
print(crypto[unit] if unit in crypto else f'Нет данных по {unit}')