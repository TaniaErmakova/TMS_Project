while True:
    firstname = input('Имя пользователя: ')
    age = input('Введите ваш возраст: ')
    if isinstance(age, int) or int(age) <= 0:
        print('Ошибка,повторите ввод')
    elif int(age) > 0 and int(age) < 10:
        print(f'Привет,шкет{firstname}')
    elif int(age) >= 10 and int(age) <= 18:
        print(f'Как жизнь,{firstname}?')
    elif int(age) > 18 and int(age) < 100:
        print(f'Что желаете,{firstname}?')
    else:
        print(f'{firstname} вы лжете-в наше время столько не живут...')
