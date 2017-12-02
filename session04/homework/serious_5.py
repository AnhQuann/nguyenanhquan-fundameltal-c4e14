x1 = 0
x2 = 1

for i in range(5):
    x3 = x1 + x2
    x1 = x2
    x2 = x3
    print('Month {0}: {1} pair(s) of rabbit'.format(i, x3))
