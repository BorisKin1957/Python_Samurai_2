'''Необходимо сформировать список со вложенными списками внутри(двумерный список)
заполненными "?". На вход подаются 2 целых числа в одну строку через пробел.
Где первое - количество вложенных списков, второе - количество объектов в списке.
Сформированный список вывести на экран.

Sample Input 1:

2 3
Sample Output 1:

[['?', '?', '?'], ['?', '?', '?']]'''

count_lists, count_chars = map(int, input().split())
result = []

for i in range(count_lists):
    l = []
    for j in range(count_chars):
        l.append('?')
    result.append(l)

print(result)