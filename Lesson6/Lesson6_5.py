import csv

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

with open("csv_test.csv", "r") as file:
    new_list = list(csv.reader(file))
    print(new_list)

row_headers = [""] + [f"Person {indx}" for indx in range(1, len(new_list))]
print(row_headers)

def list_by_indx(source: list[list[str]], indx: int) -> list[str]:
    return [elem[indx] for elem in source]


row_id = list_by_indx(new_list, indx=0)
row_name = list_by_indx(new_list, indx=1)
row_phone = list_by_indx(new_list, indx=3)
rows = [row_headers, row_id, row_name, row_phone]


# Добавляем строки в книгу эксель и сохраняем
wb = Workbook()
sheet: Worksheet = wb.active
for row in rows:
    sheet.append(row)

wb.save("my_data.xlsx")
