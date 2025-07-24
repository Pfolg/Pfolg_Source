import openpyxl

# 打开工作簿
workbook = openpyxl.load_workbook('request+openpyxl.xlsx')

sheet = workbook['openpy_test']

# 遍历
list1 = []
for row in sheet.rows:
    list2 = []
    for cell in row:
        list2.append(cell.value)
    list1.append(list2)

for i in list1:
    print(i)
