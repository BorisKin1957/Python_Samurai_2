'''На вход поступают слова в одну строку через пробел.
Вам необходимо создать словарь в котором ключом будет длина слова,
значением - само слово.'''

words = map(str, input().split())
result = {len(word): word for word in words}

print(result)