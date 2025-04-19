'''Вам нужно сделать то же самое, что и в прошлой задаче, список изменился.'''

lst = [
    {
     'id': 1, 'name': 'fruits',
     'list': ['apples', 'bananas', 'oranges']
    },
    {
     'id': 2, 'name': 'vegetables',
     'lst': ['potato', 'tomatoes', 'cucumbers']
    },
    {
     'id': 3, 'name': 'milk products',
     'sp': ['milk', 'ice cream', 'cheese']
    }
]

print([item[list(item)[2]] for item in lst])