import json
#запись словаря на диск в json-файл
dict_ = {
    '111111': ('Tania', 24, 'phone1'),
    '222222': ('Svetlana', 35, 'phone3'),
    '333333': ('Alexandr', 47, 'phone2'),
    '444444': ('Elena', 15, 'phone41'),
    '555555': ('Svetlana', 35, 'phone15')
}
with open('my_file.json', 'w') as file:
    json.dump(dict_, file)
    print(dict_)