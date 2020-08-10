num = int(input('111'))

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
