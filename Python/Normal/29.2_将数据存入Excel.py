import myweather
import openpyxl

html = myweather.get_html()  # 发请求得响应结果
list1 = myweather.parse_html(html)  # 解析数据
# 创建一个新的表格
workbook = openpyxl.Workbook()
# 创建工作表
sheet = workbook.create_sheet('openpy_test')
# 向工作表中添加数据
for i in list1:
    sheet.append(i)  # 一次添加一行
    print(sheet)

workbook.save('request+openpyxl.xlsx')
