import pandas as pd

# 读取并格式化数据
book1 = pd.read_excel('.\\satellite_x_y_rainfall.xlsx', index_col=None, header=None)
book2 = pd.read_excel('targetPoint_x_y.xlsx', index_col=None, header=None)
work1 = book1.to_numpy()
work2 = book2.to_numpy()

list_obj = []
for item in work2:
    for obj in work1:
        if obj[0] <= item[0] <= obj[0] + 2 and obj[1] >= item[1] >= obj[1] - 2:
            list_obj.append(obj)


# 算权重
def distance(a1, b1, a2, b2):
    d1 = ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5
    d2 = (((a1 - 2) - a2) ** 2 + (b1 - b2) ** 2) ** 0.5
    d3 = (((a1 - 2) - a2) ** 2 + ((b1 - 2) - b2) ** 2) ** 0.5
    d4 = ((a1 - a2) ** 2 + ((b1 - 2) - b2) ** 2) ** 0.5
    sum_d = 1 / d1 + 1 / d2 + 1 / d3 + 1 / d4
    w1, w2, w3, w4 = 1 / d1 / sum_d, 1 / d2 / sum_d, 1 / d3 / sum_d, 1 / d4 / sum_d
    return w1, w2, w3, w4


# 获得点对应数据
list_n = []
global n1, n2, n3, n4
for i in range(len(list_obj)):
    list_n.append([])
    for j in range(len(work1)):
        if list_obj[i][0] == work1[j][0] and list_obj[i][1] == work1[j][1]:
            n1 = work1[j][2]
        elif list_obj[i][0] + 2 == work1[j][0] and list_obj[i][1] == work1[j][1]:
            n2 = work1[j][2]
        elif list_obj[i][0] == work1[j][0] and list_obj[i][1] - 2 == work1[j][1]:
            n3 = work1[j][2]
        elif list_obj[i][0] + 2 == work1[j][0] and list_obj[i][1] - 2 == work1[j][1]:
            n4 = work1[j][2]
    list_n[i] = n1, n2, n3, n4

output = []
for i in range(len(work2)):
    x1, y1, x2, y2 = list_obj[i][0], list_obj[i][1], work2[i][0], work2[i][1]
    w = distance(x1, y1, x2, y2)
    a = list_n[i][0] * w[0] + list_n[i][1] * w[1] + list_n[i][2] * w[2] + list_n[i][3] * w[3]
    output.append(a)

# 输出数据
for i in range(len(work2)):
    print(f'{work2[i][0], work2[i][1]}点对应的插值数据为{output[i]}')
