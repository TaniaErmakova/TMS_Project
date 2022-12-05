from datetime import datetime
import time


def datetime_plus_sec():
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


n = int(input('Введите количество элементов: '))
new_list = [datetime_plus_sec() for i in range(0, n)]

print(new_list)
