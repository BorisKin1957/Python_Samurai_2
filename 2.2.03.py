'''этот же список, но в котором в словарях не будет параметра "salary".
На экран вывести измененный список.'''

employees = [
    {
        'name': 'Alex',
        'position': 'director',
        'salary': 1000000
    },
{
        'name': 'Marty',
        'position': 'security',
        'salary': 50000
    },
{
        'name': 'Gloria',
        'position': 'accountant',
        'salary': 150000
    }
]

for item in employees:
    item.pop('salary')

print(employees)

