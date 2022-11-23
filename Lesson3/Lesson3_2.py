firstname = input('Имя пользователя: ')
age = int(input('Введите ваш возраст: '))
if not isinstance(age,int) or age<=0:
    print('Ошибка,повторите ввод')
elif age>0 and age<10:
    print(f'Привет,шкет{firstname}')
elif age>=10 and age <=18:
    print(f'Как жизнь,{firstname}?')
elif age>18 and age <100:
    print(f'Что желаете,{firstname}?')
else:
    print(f'{firstname} вы лжете-в наше время столько не живут...')