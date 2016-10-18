from game2d import *

def update():
    global x
    canvas_fill(canvas, (255, 255, 255))
    image_blit(canvas, image, (x,50))
    x = (x + 10) % 900

canvas = canvas_init((900,900))
image = draw_rect(canvas, (0, 255, 0), (0 , 0, 50, 50))
x = 50

set_interval(update, 1000 // 30)
