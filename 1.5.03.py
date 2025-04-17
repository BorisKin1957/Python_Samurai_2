'''Sample Input 1:

1 2 3 4 5
Sample Output 1:

*
**
***
****
*****'''


numbers = map(int, input().split())

for number in numbers:
    for _ in range(number):
        print('*', end='')
    print()