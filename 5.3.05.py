'''Вам нужно создать функцию func, которая возвращает матрицу(двумерный список,
в каждом вложенном списке целые числа). Она имеет ключевые параметры size=5, up=0,
down=0. Напомню, что диагональ матрицы проходит от верхнего левого края, до нижнего правого,
она должна заполняться 1.  size отвечает за размер матрицы(5x5 по умолчанию).
up отвечает за то, какими цифрами мы должны заполнять матрицу выше диагонали,
down - тоже самое, только ниже диагонали.'''

def func(size=5, up=0, down=0):
    result = []
    for i in range(size):
        inner = []
        for j in range(size):
            if i > j:
                inner.append(down)
            elif i < j:
                inner.append(up)
            elif i == j:
                inner.append(1)
        result.append(inner)
    print(result)


print(func())
print(func(size=3, up=3))