from game2d import *

col = 0
x, y, w, h = 0, 0, 1000, 1000
canvas = canvas_init((w,h))
draw_rect(canvas, (80, 80, 80), (x, y, w, h))

def circle(x, y, w, h, col):
    
    color = (0, 0, 0)
    draw_circle(canvas, (color), (x + w / 2, y + h / 2), h / 2)
    new1 = circle(x, y, w / 2, h, 0)
##    new2 = circle(x, y + h / 2, w / 2, h, 1)

    
    if (col % 2) == 0:
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)

for i in range (2):
    circle(x, y, w, h, col)
    


