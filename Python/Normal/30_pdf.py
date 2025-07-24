# 这是小学公式吗？震惊我3秒钟
import pdfplumber

with pdfplumber.open('小学数学公式.pdf') as pdf:
    for i in pdf.pages:  # 遍历页——对象
        print(i.extract_text())  # 提取内容
        print('-'*50+f'第{i.page_number}页结束')
