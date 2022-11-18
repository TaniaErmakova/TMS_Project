string_1 = 'aaaaaBccBddBeeBffBggB'
result_1 = string_1[5::3]
print(result_1)

string_2 = 'AAAABBBBCCCCDDDDFFFF'
result_2 = string_2[:4] + string_2[4:8] + string_2[8:12] + string_2[12:16] + string_2[16:]
print(result_2)

string_3 = 'PYTHON'
result_3 = string_3[::-1]
print(result_3)