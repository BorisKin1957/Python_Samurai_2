'''Вам дан словарь. Вам нужно создать функцию func и с его помощью она должна
конвертировать кириллицу в латиницу. Функция принимает обязательно строку,
которую нужно преобразовать(регистр не учитывать) и необязательный аргумент -
разделитель между словами(строка), по умолчанию пробел. Функцию вызывать не нужно.

Sample Output:

protivoudarnyy zahvat kulaka licom
a!u!vas!pikseli!ubezhali
syrnaya neizbezhnost bytiya
alya^ulyu
tra%lya%lya'''

def translit(text, sp=' '):
    for char in text:
        if char.lower() in dct:
            text = text.replace(char, dct[char.lower()])
        else:
            text = text.replace(char, sp)
    return text

asdfgh = [['Противоударный захват кулака лицом', ' '], ['а у вас пиксели убежали', '!'],
          ['сырная неизбежность бытия', ' '], ['аля улю', '^'], ['тра ля ля', '%']]


dct = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

for lst in asdfgh:
    print(translit(lst[0], lst[1]))