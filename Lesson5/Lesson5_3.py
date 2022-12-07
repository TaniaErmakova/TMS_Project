current_list = ('потоп', 'доход', 'шалаш', 'заря', 'таня')
new_list = tuple(filter(lambda x: x[0:] == x[::-1], current_list))
print(new_list)
