#WAY1
a = 2  #起点
b = 5  #终点
d = 0.001  #精度
s = 0  #面积和
x = a  #变量
while x < b:
    f1 = x * x + 6 * x + 9  #左高
    f2 = (x + d) ** 2 + (x + d) * 6 + 9  #右高
    c = ((f1 + f2) * d) / 2  #小梯形面积
    s += c  #求和
    x += d  #变量变化
w = abs(s - 129)  #误差
print(s)
print(w)
#WAY2
inte_begin = 2
inte_end = 5
dx = 0.1
dx_dx = 0.001
cal_error = 100
while cal_error > 0.001:
    x = inte_begin
    sum_x = 0
    while x < inte_end:
        fx_1 = x ** 2 + 6 * x + 9
        fx_2 = (x + dx) ** 2 + 6 * (x + dx) + 9
        area = ((fx_1 + fx_2) * dx) / 2
        sum_x += area
        x += dx
    cal_error = abs(sum_x - 129)
    dx -= dx_dx
print(f"The maximum step is {dx} for the error less than 0.001")
print(f"The result is {sum_x}")
print(f"THe cal_error is {cal_error}")
