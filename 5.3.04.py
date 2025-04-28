'''Вам необходимо написать функцию func. Она принимает в себя позиционно двумерный список,
который вам дан. В каждом вложенном списке могут быть различные типы данных.
Функция должна все содержимое всех вложенных списков собрать в одну большую строку.
Пример:

lst = [[1, 2, 3],['a', 's', 'd'],[True, False, None]]

func(lst, sep="") => 123asdTrueFalseNone'''


def func(lst: list, sp='') -> None:
    result = ''
    for item in lst:
        result += ''.join([str(i) for i in item]) + sp
    print(result[:-len(sp)] if sp else result)


lst = [[1, 2, 3, 4], ['s', 'f', 'r'], [1, '3', 5, 'w'],
       [True, False, None], [1, True, 'w', 4.5, {'k': 'v'}]]

func(lst)
func(lst, '<*>')