spisok = [2, 7, 8, 10, 4, 2, 8, 12, 7, 8, 9, 10, 4, 8, 12, 4, 2]
result = {}
for i in spisok:
    if result.get(i, 0):
       result[i] = result[i] + 1
    else:
        result[i] = 1
print(result)
