
# 实心三角形

def triangle(num):

    for i in range(num):

        tab = False

        for j in range(i+1):

            print('*', end='')

            if j == i:

                tab = True

            if tab:

                print('\n', end='')

# 空心三角形


def hollow_triangle(num):

    for i in range(num):

        tab = False

        for j in range(i + 1):

            if i != num-1:

                if j == i:

                    tab = True

                if (i == j or j == 0):

                    print('*', end='')

                else:

                    print(' ', end='')

            else:

                print('*', end='')

        if tab:

            print('\n', end='')


Length = (input('边长字节数？\n'))

if str.isdecimal(Length):

    Type = input('请选择 实心/空心 \n')

    num = int(Length)

    if Type == ("实心" or "实"):

        triangle(num)

    elif Type == ('空心' or '空'):  # 加了个括号

        hollow_triangle(num)

    else:

        print('啷个看不懂嘛，实心儿或者空心儿撒')

else:

    print('请输入阿拉伯数字')

# try_1
# try_2
