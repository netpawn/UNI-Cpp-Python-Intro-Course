from game2d import *

val = int(input("Val?"))
listaval = []
listaval.append(val)


while val != 0:
    val = int(input("Val?"))
    if val != 0:
        listaval.append(val)
    
xc = 500
yc = 50 * len(listaval)

canvas = canvas_init(( xc, yc ))

massimo = max(listaval)

x = 0
y = 0
    
for i in listaval:
    lenght = (500*i)/massimo
    draw_rect(canvas ,(0,0,250), (x , y, lenght, 50))
    y += 50
    
        
    
    

