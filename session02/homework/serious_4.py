row = int(input('Enter the number of rows:'))
column = int(input('Enter the number of columns:'))

# for i in range(1, row+1):
#     for i in range(1, column+1):
#         print('* ', end='')
#     print()

for i in range(1, row+1):
    if (i%2==0):
        for i in range(1, column+1):
            if(i%2==0):
                print('x ', end='')
            else:
                print('* ', end='')
    else:
        for i in range(1, column+1):
            if(i%2==0):
                print('* ', end='')
            else:
                print('x ', end='')
    print()
