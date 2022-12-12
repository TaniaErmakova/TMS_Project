import timeit

code_to_test ="""
def decor(func):
    def inner(*args, **kwargs):
        print('Результат: ')
        result = func(*args, **kwargs)
        print(result)
        return result
    return inner


my_list_1 = [23, 34, 87, 45, 18, 31]


@decor
def inc_list(my_list):
    result = []
    for item in my_list:
        result.append(item+1)
    return result

@decor
def create_list(count: int):
    result = []
    for i in range(1, count+1):
        result.append(i)
    return result

inc_list(my_list_1)

create_list(5)
"""
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)