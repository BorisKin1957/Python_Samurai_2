'''На вход подается список целых положительных чисел.
Вам необходимо перебрать все числа и вывести их в одной строке без разделителя.

Sample Input 1:

34 7 12 89
Sample Output 1:

3471289'''

numers = map(int, input().split())

for i in numers:
    print(i, end='')