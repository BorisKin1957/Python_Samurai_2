'''

Дан список с вложенными словарями, необходимо достать из них списки с продуктами и положить их в
новый список. Данный список вывести на экран.

Sample Input:

Sample Output:

[['apples', 'bananas', 'oranges'], ['potato', 'tomatoes', 'cucumbers'], ['milk', 'ice cream', 'cheese']]

'''


lst = [
    {
     'id': 1, 'name': 'fruits',
     'lst': ['apples', 'bananas', 'oranges']
    },
    {
     'id': 2, 'name': 'vegetables',
     'lst': ['potato', 'tomatoes', 'cucumbers']
    },
    {
     'id': 3, 'name': 'milk products',
     'lst': ['milk', 'ice cream', 'cheese']
    }
]



print([i['lst'] for i in lst])