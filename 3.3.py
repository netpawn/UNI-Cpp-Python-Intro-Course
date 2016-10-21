from game2d import *

def update():
    global x, y, dy
    canvas_fill(canvas, (255, 255, 255))
    draw_rect(canvas, (0, 255, 255), (x, y, 50, 50))
    x = (x + 10) % 450
    y = (y + dy)
    dy += 0.4
    if y >= (450 - 50):
        dy = -dy
            
x = 0
dy = 0
y = 0

canvas = canvas_init((450,450))

set_interval(update, 1000 // 30)
