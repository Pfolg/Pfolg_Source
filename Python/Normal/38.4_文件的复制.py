# 边读边写
def copy(old, new):
    fo = open(old, 'rb')
    fn = open(new, 'wb')
    s = fo.read()
    fn.write(s)

    # 先打开的后关，后打开的先关
    fn.close()
    fo.close()


if __name__ == '__main__':
    old = '.\\google.png'
    new = '..\\时钟(useless)\\copy_google.png'  # 两点表示上级目录
    copy(old, new)
    print('文件复制完毕')