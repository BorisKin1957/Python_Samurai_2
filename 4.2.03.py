'''В какой-то стране проходят выборы президента. Участвуют 2 кандидата -
"Аркадий Хруст" и "Бьянка Чеснокова". Но в одном из избирательных участков,
камерой ночью было зафиксирован вброс дополнительных бюллетеней в пользу
одного из кандидатов, неизвестным человеком в ростовом костюме панды или коня
(плохое качество видео). Необходимо посчитать голоса за каждого из кандидатов.
 Естественно голоса с вброшенных бюллетеней не стоит учитывать.
 Вброшенными бюллетенями считаются те, в которых повторяется имя избирателя
 (т.к данный человек уже голосовал). Вам дан список кортежей, в каждом из них
 находятся данные избирателя. Необходимо сформировать словарь в формате:

{'Аркадий Хруст': <количество голосов>, 'Бьянка Чеснокова': <количество голосов>}'''


lst = [
    (1, {'избиратель': 'Крыжовников Игорь', 'пол': 'м', 'возраст': 18, 'кандидат': 'Аркадий Хруст'}),
    (2, {'избиратель': 'Огурцова Урсула', 'пол': 'ж', 'возраст': 54, 'кандидат': 'Бьянка Чеснокова'}),
    (3, {'избиратель': 'Вывихов Максим', 'пол': 'м', 'возраст': 22, 'кандидат': 'Аркадий Хруст'}),
    (4, {'избиратель': 'Снег Григорий', 'пол': 'м', 'возраст': 78, 'кандидат': 'Бьянка Чеснокова'}),
    (5, {'избиратель': 'Щекастая Елена', 'пол': 'ж', 'возраст': 36, 'кандидат': 'Аркадий Хруст'}),
    (6, {'избиратель': 'Балтика Людмила', 'пол': 'ж', 'возраст': 105, 'кандидат': 'Аркадий Хруст'}),
    (7, {'избиратель': 'Крыжовников Игорь', 'пол': 'м', 'возраст': 68, 'кандидат': 'Аркадий Хруст'}),
    (8, {'избиратель': 'Щекастая Елена', 'пол': 'ж', 'возраст': 47, 'кандидат': 'Аркадий Хруст'}),
    (9, {'избиратель': 'Овальная Наташа', 'пол': 'ж', 'возраст': 55, 'кандидат': 'Бьянка Чеснокова'}),
    (10, {'избиратель': 'Иванов Геральт', 'пол': 'м', 'возраст': 27, 'кандидат': 'Аркадий Хруст'})
]

new_lst = set([(item[1]['избиратель'], item[1]['кандидат']) for item in lst])

bianka_votes, hrust_votes = 0, 0

for vote in new_lst:
    match vote:
        case (name, 'Аркадий Хруст'):
            hrust_votes += 1
        case (name, 'Бьянка Чеснокова'):
            bianka_votes += 1

result = dict([('Аркадий Хруст', hrust_votes), ('Бьянка Чеснокова', bianka_votes)])

print(result)

