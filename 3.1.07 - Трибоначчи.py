'''Вам необходимо сформировать последовательность Трибоначчи'''

n, result = int(input()), (1, 1, 1)

for i in range(n - 3):
    result += (sum(result[-3:]),)

print(*result)