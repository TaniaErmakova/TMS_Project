x = int(input('Введите число:'))
even = lambda a: a % 2 == 0


def fn(y: int):
    if even(y):
        print('Чётное')
    else:
        print('Нечётное')


fn(x)
