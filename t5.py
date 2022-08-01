from turtle import *

start = 180
speed(0)
while (start > 0):
    circle(start)
    left(90)
    start -= 10
    write(start, font = ('Arial', 8, 'italic'))

mainloop()