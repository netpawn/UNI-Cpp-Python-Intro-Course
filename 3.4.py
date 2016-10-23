from math import *
from game2d import *

class Planet:
    def __init__(self, r0, theta0, omega0):
        self._r = r0
        self._theta = theta0
        self._omega = omega0

    def pos(self):
        x = self._r * sin(self._theta)
        y = self._r * cos(self._theta)
        return (x+250, y+250)
    

    def move(self):
        self._theta += self._omega

    def getdiameter(self):
        d = self._r * 2
        return d
        
        
r0 = float(input("Raggio? "))
theta0 = float(input("Angolo? "))
omega0 = float(input("Velocità? "))

p = Planet(r0, theta0, omega0)

print("x,y = ", p.pos())
print("Diametro = ", p.getdiameter())
print("\n")

canvas = canvas_init((500, 500))

def update():
    global r0,theta0,omega0,p,a
    canvas_fill(canvas, (255, 255, 255))
    p.move()
    draw_circle(canvas, (0, 255, 0), (p.pos()), 50)
    print(p.pos()) #for debug in brython console
    
set_interval(update, 1000 // 5)






