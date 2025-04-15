'''Подается список целых чисел в одну строку через пробел.
Необходимо при помощи цикла for и функции enumerate найти индекс минимального значения,
функции min, max и сортировки постарайтесь не использовать.
Вывести значение на экран.'''


numbers, min_num = map(int, input().split()), 1.797e+308

for i, num in enumerate(numbers):
    if num < min_num:
        min_num = num
        i_min = i

print(i_min)