##
sx, sy = 4.5, 7.5
x1, y1 = 4, 8
x2, y2 = 4, 6
x3, y3 = 6, 6
x4, y4 = 6, 8
n1, n2, n3, n4 = [14, 20.4, 18.3, 12.9]
list_num = [n1, n2, n3, n4]


def distance(x, y):
    d = ((sx - x) ** 2 + (sy - y) ** 2) ** 0.5
    return d


list_d = [distance(x1, y1), distance(x2, y2), distance(x3, y3), distance(x4, y4)]
print(list_d)


def w(list_input, num):
    list_use = []
    s = 0
    for i in range(4):
        d = 1 / list_input[i]
        list_use.append(d)
    all_d = sum(list_use)
    print(all_d)
    for i in range(4):
        ws = list_d[i] / all_d * num[i]
        s += ws
    return s


print(w(list_d, list_num))
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

point_x = np.array([4, 4, 6, 6])
point_y = np.array([8, 6, 6, 8])
target_x = 4.5
target_y = 7.5
R_points = np.array([14, 20.4, 18.3, 12.9])
distance = np.zeros(4)
weights = np.zeros(4)

for i in range(4):
    temp = (point_x[i] - target_x) ** 2 + (point_y - target_y) ** 2
    distance[i] = np.sqrt(temp)

for i in range(4):
    weights[i] = (1 / distance[i]) / np.sum(1 / distance)

R_points = np.sum(R_points * weights)
print(f'output {R_points}')
##
