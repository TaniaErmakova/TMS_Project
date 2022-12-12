def decor(func):
    def inner(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print(result)
        print('end')
        return result
    return inner

@decor
def sum_(a:int, b:int):
    result = a+b
    return result

def multiple_(a:int, b:int):
    result = a*b
    return result


m = decor(multiple_)

sum_(2,4)
m(2,4)