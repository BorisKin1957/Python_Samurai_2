'''Нужно написать программу, которая сформирует и выведет на экран словарь,
где ключами будут латинские строчные буквы, а значениями - порядковые номера букв.
Строка с алфавитом будет храниться в переменной alph_str.'''


import string
alph_str = string.ascii_lowercase
alph_dict = {}
for number, char in enumerate(alph_str, start=1):
    alph_dict[char] = number

print(alph_dict)




