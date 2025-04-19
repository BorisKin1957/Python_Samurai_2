
result = {}

for char in input():
    if char.isalpha():
        result[char] = result.get(char, 0) + 1
print(result)