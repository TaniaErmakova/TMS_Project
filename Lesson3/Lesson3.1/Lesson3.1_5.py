list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]
list_3 = [i+int(j) for i in list_1 for j in list_2]
print(list_3)


from itertools import product

list3 = [a+int(b) for a, b in product(list_1, list_2)]
print(list3)