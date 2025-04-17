'''Вам нужно посчитать сумму элементов матрицы, находящихся на ее диагонали
(проходит от левого верхнего угла до правого нижнего) и вывести ее на экран. '''

import sys

lst = sys.stdin.readlines()
lst = [list(map(int, i.split())) for i in lst]
result = 0

for i in range(len(lst)):
    result += lst[i][i]

print(result)