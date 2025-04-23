'''Вам дан список файлов. Вам необходимо при помощи генератора создать множество
файлов с расширением ".py" вне зависимости от его регистра.
Все добавляемые файлы необходимо приводить к нижнему регистру.
Вывести итоговое множество одной строкой, отсортировав по алфавиту,
разделяя элементы пробелом.'''


files = ['main.py', 'spisok.txt', '123.Py', 'paint.exe', 'tupik2003.mkv', 'foto.rar',
         'tanecjivota.Mkv', 'RDR2.eXe', 'blacklist.Txt', 'lesson.py', 'foto2.rAr',                            'hack_pintagon.pY', 'lesson.py'
         ]

print(*sorted({file_name.lower() for file_name in files if file_name.lower(
).endswith('.py')}))