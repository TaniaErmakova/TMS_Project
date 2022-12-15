str_1 = str(input('Введите строку: '))
str_2 = str(input('Введите строку: '))
str_3 = str(input('Введите строку: '))
str_4 = str(input('Введите строку: '))
with open('file_name.txt', 'w') as file:
    file.write(str_1 + '\n')
    file.write(str_2 + '\n')
with open('file_name.txt', 'a') as file:
    file.write(str_3 + '\n')
    file.write(str_4 + '\n')
