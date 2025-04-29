'''Вам нужно создать функцию func, которая принимает произвольное количество
именованных аргументов. Возвращает она список двух вложенных кортежей.
В первом находятся все ключи **kwargs, во втором - значения.'''

def func(**kwargs):
    all_keys, all_values = [], []
    for k, v in kwargs.items():
        all_keys.append(k)
        all_values.append(v)
    return [tuple(all_keys), tuple(all_values)]


print(func(x='эники', y='беники'))