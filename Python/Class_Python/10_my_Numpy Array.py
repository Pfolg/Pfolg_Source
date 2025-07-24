##  2024年5月8日16:07:05  author=Pfolg
import numpy

a = numpy.array([1, 2, 3])
print(a)

ar1 = numpy.array([[1, 2, 3], [8, 9, 5]])
ar2 = numpy.array([[5, 5, 4], [6, 7, 2]])
ar3 = ar1 - ar2
print(ar3)
##
ar4 = numpy.zeros(3)
ar5 = numpy.ones(3)
print(ar4, ar5)
##
ar6 = numpy.zeros((3, 4))
print(ar6)
row_get = ar6.shape  # (3, 4)tuple
print(row_get[0], row_get[1])  # 3 4
r = ar6.shape[0]  # int 3
c = ar6.shape[1]  # int 4
##
ar_eye = numpy.eye(3)
print(ar_eye)
ar_random = numpy.random.random(3)
print(ar_random)
ar_random1 = numpy.random.random((3, 3))
print(ar_random1)
##
ar_1 = numpy.linspace(start=0, stop=10, num=5)
ar_2 = numpy.arange(start=0, stop=10, step=2)
print(ar_1, '\n', ar_2)
##
# ar_3 = ar1 @ ar2
# print(ar_3)
##
ar7 = numpy.random.random((5, 6))
print(ar7, '\n')

i = ar7[1, :]
j = ar7[:, 3]
k = ar7[3, 0:3]
l = ar7[4:6, 4]
print(f'{i}\n{j}\n{k}\n{l}')
##
ar7_1 = numpy.cos(ar7)
ar7_2 = numpy.sin(ar7)
ar7_3 = numpy.floor(ar7)
ar7_4 = numpy.ceil(ar7)
print(f'\n{ar7_1}\n\n{ar7_2}\n\n{ar7_3}\n\n{ar7_4}')
## 合并
ar8 = numpy.array([[4, 5, 6], [7, 8, 9]])
ar9 = numpy.array([[7, 4, 1], [9, 6, 3]])
ar10 = numpy.vstack(ar8 + ar9)
ar11 = numpy.hstack(ar8 + ar9)
print(ar10)
print(ar11)

## 转置
ar12 = numpy.transpose(ar10)
print(ar12)
