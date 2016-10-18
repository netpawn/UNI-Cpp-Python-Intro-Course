from game2d import *

val = int(input("Val? "))
listaval = []
listaval.append(val)

while val != 0:
    val = int(input("Val? "))
    if val != 0:
        listaval.append(val)
    
xc = 500
yc = 500

canvas = canvas_init(( xc, yc ))

massimo = max(listaval)

avg = sum(listaval)/len(listaval)

x = 0
y = 500

b = 500/len(listaval)    

for i in listaval:
    
    lenght = (500*i)/massimo
    
    if i == massimo:
        draw_rect(canvas ,(250, 0, 0), (x , 0, b, lenght))
    elif i < avg:
        draw_rect(canvas ,(0, 0, 250), (x , y-i, b, lenght))
    elif i >= avg:
        draw_rect(canvas ,(250, 0, 0), (x , y-i, b, lenght))
    x += b
        
