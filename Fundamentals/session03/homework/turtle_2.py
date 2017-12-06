from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(1, 6):
    fillcolor(colors[i-1])
    color(colors[i-1])
    begin_fill()
    for i in range(2):
        for j in range(1, 3):
            forward(50*j)
            left(90)
    end_fill()
    forward(50)

mainloop()
