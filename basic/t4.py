from turtle import *

side = 6
size = 140
pensize(4)
speed (0)
for i in range (side):
    pencolor('blue')
    forward (size)
    for i in range (6):
        pencolor('red')
        forward (70)
        circle(20)
        right(360/6)
        write('#',font=('Arial',14,'italic'))
    left(360/side)

mainloop()