'''Подается список целых чисел в одну строку через пробел.
Необходимо при помощи функции enumerate вывести в одну строку только те числа,
которые находятся на нечетных индексах. '''

numbers = enumerate(map(int, input().split()))

result = filter(lambda x: x[0] % 2 != 0, numbers)

for item in result:
    print(item[1], end=' ')