'''Вам нужно реализовать программу регистрации на сайте. В цикле сначала происходит запрос логина пользователя, он должен быть не менее 5-ти символов, иначе программа нам сообщит:

Логин должен содержать не менее 5 символов

Запрос начнется заново. Если логин валидный, далее начнется запрос пароля,
он должен быть не менее 8 символов и содержать символы "%" и "#". Если пароль не подошел,
программа нам сообщает:

Пароль менее 8 символов, либо не содержит символы "%#"

Начинаем все заново с запроса логина. Если пароль корректный, то цикл завершается и выводится строка:

Регистрация завершена!'''


while True:
    nic_name = input('')

    while len(nic_name) < 5:
        print('Логин должен содержать не менее 5 символов')
        nic_name = input()

    password = input('')

    if len(password) < 8 or '#' not in password or '%' not in password:
        print('Пароль менее 8 символов, либо не содержит символы "%#"')
        continue
    else:
        break

print('Регистрация завершена!')
