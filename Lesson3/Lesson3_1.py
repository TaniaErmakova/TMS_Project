#Первый способ
str_1 = input('Input your firstname and lastname: ')
words_1 = str_1.split()
formatted_str_1 = '!{} ! {}!'.format(words_1[1],words_1[0])
print(formatted_str_1)
#Второй способ
str_2 = input('Input your firstname and lastname: ')
words_2 = str_2.split()
formatted_str_2 = f'!{words_2[1]} ! {words_2[0]}!'
print(formatted_str_2)