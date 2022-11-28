my_list = list(range(1,51))
result = []
my_list_length = len(my_list)
for x in my_list:
    result.append(my_list[my_list_length-x])
print(result)