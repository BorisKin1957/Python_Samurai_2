'''Вам нужно написать функцию func, которая принимает слово, считает сумму всех символов,
которые являются цифрами и выводит ее на экран.'''

def func(word: str) -> None:
    print(sum(int(c) for c in word if c.isdigit()))

func(input())