words, flag = input().split(), True

while words:
    if len(words.pop()) > 4:
        continue
    else:
        flag = False
        break

print(['НЕТ', 'ДА'][flag])