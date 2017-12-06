from turtle import *

width(10)

# for i in range(10):
#
#         for i in range(3):
#             color('green')
#             forward(20)
#             penup()
#             forward(20)
#             pendown()
#
#         for i in range(3):
#             color('red')
#             forward(20)
#             penup()
#             forward(20)
#             pendown()

for i in range(10):
    if i % 6 < 3:
        color("blue")
    else:
        color("red")
    forward(50)
    penup()
    forward(50)
    pendown()



mainloop()
