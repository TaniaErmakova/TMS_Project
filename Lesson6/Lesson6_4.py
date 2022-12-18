import csv
import json

with open("my_file.json", encoding='utf-8') as json_file:
    data = json.load(json_file)
cols = ['id', 'name', 'age', 'phone']
new_dict = [{'id': k, 'name': v[0], 'phone': v[2], 'age': v[1]} for (k, v) in data.items()]
print(new_dict)

path = "D:\TMS_Python\TMS_Project\Lesson6\csv_test.csv"
with open(path, 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=cols)add
    wr.writeheader()
    wr.writerows(new_dict)
