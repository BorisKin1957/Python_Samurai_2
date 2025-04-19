'''На вход подается список в формате:

["<название греха> <имя грешника>", "<название греха> <имя грешника>",
"<название греха> <имя грешника>"]

Нужно сформировать и вывести на экран словарь в котором ключами будут
 названия грехов(строка), а значениями списки имен грешников.

Sample Input 1:

Похоть Игнат
Жадность Жора
Гнев Митя
Лень Лёня
Жадность Гжижек
Эксгибиционизм Шакира

Sample Output 1:

{'Похоть': ['Игнат'], 'Жадность': ['Жора', 'Гжижек'], 'Гнев': ['Митя'],
'Лень': ['Лёня'], 'Эксгибиционизм': ['Шакира']}
'''

import sys
lst = [i.rstrip() for i in sys.stdin.readlines()]

result = {}
for item in lst:
    sin, name = item.split()
    result.setdefault(sin, []).append(name)

print(result)
