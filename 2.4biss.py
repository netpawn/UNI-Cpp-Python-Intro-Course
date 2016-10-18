from game2d import *

b = int(input("Numero di quadrati? "))

xc = 500

canvas = canvas_init(( xc, xc ))
green = 0
x = xc

for i in range(b):
    draw_rect(canvas, (0, green, 0), (0,0,x,x))
    green += int(( 255 / b ))
    x -= int(( xc / b ))
