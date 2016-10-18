from game2d import *

rows = int(input("Rows?"))
cols = int(input("Cols?"))

xc = (( cols * 50 ) + cols)
yc = (( rows * 50 ) + rows)

canvas = canvas_init(( xc, yc ))

green = 0
y = 0

for i in range(rows):
    x = 0
    blue = 0
    for j in range(cols):
        draw_rect(canvas, (0, green, blue), (x , y, 50, 50))
        x += int(( xc / cols ) + 1)
        blue += int(( 255 / cols ))

    y += int(( yc / rows ) + 1)
    green += int(( 255 / rows ))
