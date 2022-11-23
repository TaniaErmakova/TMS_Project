result = 0
n_1 = int(input('Введите число: '))
for i in range(1,n_1+1):
       result += i**3
print(result)



sum = 0
n_2 = int(input('Введите число: '))
while n_2 > 0:
    sum += n_2**3
    n_2-=1
print(sum)