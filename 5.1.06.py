'''Напишите функцию func, которая проверит ваш пароль на сложность.
Функция принимает в себя пароль(строку), в пароле в обязательном порядке должны присутствовать:

- не менее 1ой цифры

- не менее 1ой буквы в нижнем и верхнем регистре

- хотя бы 1 символ из строки "!@#$%*"

- общее количество символов не менее 8ми.

Если функция не проходит любую из проверок - выводится "Плохо. Но я уверен ты сможешь!
Наверное...". Если все проверки пройдены вывести - "Шикарный пароль!"'''


def func(pasword: str) -> None:
    flag1, flag2, flag3, flag4 = False, False, False, False
    for char in pasword:
        if char.isdigit():
            flag1 = True
        elif char.isupper():
            flag2 = True
        elif char.islower():
            flag3 = True
        elif char in '!@#$%*':
            flag4 = True
    if flag1 and flag2 and flag3 and flag4 and len(pasword) > 7:
            print('Шикарный пароль!')
    else:
        print('Плохо. Но я уверен ты сможешь! Наверное...')

func(input())