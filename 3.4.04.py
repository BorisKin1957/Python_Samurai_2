'''

Дан список множеств и неизменяемых множеств, необходимо на основе этого списка
сформировать неизменяемое множество с содержимым множеств всех типов из списка.
Вывести его на экран.

Sample Output:

frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24})

'''

lst = [
    {1, 2}, frozenset({3, 4}), {5, 6}, frozenset({8, 7}),
    {9, 10}, frozenset({11, 12}), {13, 14}, frozenset({16, 15}),
    {17, 18}, frozenset({19, 20}), {21, 22}, frozenset({24, 23})
]


st = frozenset()

for item in lst:
    if isinstance(item, frozenset):
        st = st.union(item)
    else:
        st = st.union(set(item))

print(st)

