'''На вход подается список целых чисел в одну строку через пробел.
Напишите функцию func, которая принимает этот список и среди его чисел возвращает первое уникальное.
Если такое отсутствует, то возвращается -1. Вызвать функцию, результат вывести в консоль.'''


def get_unique_number(string: str) -> int:
    chars = string.replace(' ', '')
    for char in chars:
        if chars.count(char) == 1:
            return int(char)
            break
    return -1

print(get_unique_number(input()))