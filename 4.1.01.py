

lst = [1, 5.6, '3', [1, 2], (4, 7), {'a': 4}, True]

for i in lst:
    match i:
        case str(i):
            continue
        case _:
            print(f'Это тип данных - {type(i)}')
