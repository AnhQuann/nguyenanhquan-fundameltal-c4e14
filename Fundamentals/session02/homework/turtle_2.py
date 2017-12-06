from turtle import *

n = int(input("Nhap so canh: "))

for i in range(3, n+1):
    for u in range(i):
        if(i%2==0):
            color('red')
        else:
            color('blue')
        forward(50)
        left(180-(((i-2)*180)/i))

mainloop()
