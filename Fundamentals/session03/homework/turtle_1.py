from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(3, 8):
    color(colors[i-3])
    for u in range(i):
        forward(50)
        left(180-(((i-2)*180)/i))

mainloop()
