'''Вам подается список со вложенными списками. Пример списка:

lst = [["носки", "б"], ["шорты", "цв"]]
В каждом вложенном списке 1ый элемент - одежда, 2ой - цвет(белый или цветной).
Необходимо при помощи функции enumerate определить элемент одежды либо в список с белой одеждой,
либо с цветной. Вывести сначала список с белой одеждой, затем с новой строки с цветной.

Sample Input 1:

носки цв
трусы цв
фуфайка б
шорты цв
перчатки б
Sample Output 1:

['фуфайка', 'перчатки']
['носки', 'трусы', 'шорты']'''


# import sys
#
# lst = sys.stdin.readlines()
# lst = [tuple(reversed(i.rstrip().split())) for i in lst]
#
# new = {}
# for i in lst:
#     new.setdefault(i[0], []).append(i[1])
#
# print(new['б'])
# print(new['цв'])

import sys
lst = sys.stdin.readlines()
lst = [i.rstrip().split() for i in lst]

white, colors = [], []

for item in lst:
    if item[1].lower() == 'б':
        white.append(item[0])
    else:
        colors.append(item[0])

print(white)
print(colors)
