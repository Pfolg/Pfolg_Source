def loss_fun(y1, y2):
    su = 0
    for i in range(len(y1)):
        m_s = (y1[i] - y2[0][i]) ** 2
        su += m_s
    return su
