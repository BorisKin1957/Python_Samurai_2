'''На вход подается строка в формате:

"<раса> <количество> <раса> <количество> <раса> <количество>"
Необходимо на основе строки сформировать и вывести на экран список формата:

[[<раса>, <количество>], [<раса>, <количество>], [<раса>, <количество>]]
Где во вложенном списке первый элемент - строка, второй - целое число.'''

data = [item for item in input().split()]

result = [[data[i], int(data[i + 1])] for i in range(0, len(data) - 1, 2)]

print(result)
