x = int(input('Nhap x: '))
y = int(input('Nhap y: '))

while True:
    calc = input('Operation(+, -, *, /): ')
    if(calc == '+'):
        print('{0} + {1} = '.format(x, y), (x+y))
        break
    elif(calc == '-'):
        print('{0} - {1} = '.format(x, y), (x-y))
        break
    elif(calc == '*'):
        print('{0} * {1} = '.format(x, y), (x*y))
        break
    elif(calc == '/'):
        print('{0} / {1} = '.format(x, y), (x/y))
        break
    else:
        print('Error. Try again!')
