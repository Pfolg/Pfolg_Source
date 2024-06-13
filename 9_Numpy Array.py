##
import numpy
import matplotlib.pyplot as plt

list_start = [1, 2, 3, 4, 5]
array_middle = numpy.zeros((6, 5))
array_middle_middle = numpy.zeros(5)
print(array_middle, '\n\n', array_middle_middle)
##
print('-' * 50)
for i in range(6):  # row
    for j in range(5):
        array_middle_middle[j] = list_start[j] + 10 * i
        array_middle[i, :] = array_middle_middle
target = array_middle
print(target)

####################################################################
h0, g = 10, 9.8

position = numpy.zeros(21)
for i in range(20):
    position[i] = 10 - 0.5 * i
print(position)

tim = numpy.zeros(21)
for i in range(21):
    tim[i] = ((h0 - position[i]) * 2 / g)**0.5
print(tim)
plt.plot(tim, position, '-*r')
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('time', fontsize=20)
plt.ylabel('position', fontsize=20)
plt.show()
# ##
# ho = 10
# g = 9.8
# position = np.linspace(10, 0, 21)
# t = np.sqrt(2 * (ho - position) / g)
# print('position=', position)
# print('t=', t)
# plt.plot(t, position, '-*b')
# plt.xlabel('time', fontsize=20)
# plt.ylabel('position', fontsize=20)
# plt.tick_params(axis='x', labelsize=20)
# plt.tick_params(axis='y', labelsize=20)
# plt.show()
# ##
