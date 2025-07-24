# -*- coding: utf-8 -*-
# Project >>> Pyworking   ||    Environment >>> PyCharm
# FileName >>> 42.2__    ||    Author >>> Pfolg
# Date >>> 2024/6/7 and Time >>> 22:27
def find_answer(ques):
    with open('reply.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            # 字符串分割
            keyword = line.split('|')[0]
            reply = line.split('|')[1]
            if keyword in ques:
                return reply
    return False


if __name__ == '__main__':
    question = input('Hi,主人你好，瓦塔西久等于此，可否向吾说一说烦恼,退出=“bye”:')
    while True:
        if question == 'bye':
            break
        else:
            reply = find_answer(question)
            if reply == 0:
                question = input('瓦塔西听不懂思密达！牛可以问问“订单 物流 账户 支付” 退出请扣“bye”:')
            else:
                print(reply)
                question = input('瓦塔西……:')
    print('瓦塔西仍等候于此！！！')
