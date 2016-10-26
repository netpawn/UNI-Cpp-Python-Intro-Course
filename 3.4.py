from math import *
from game2d import *

class Planet:
    def __init__(self, r0, theta0, omega0, diameter):
        self._r = r0
        self._theta = theta0
        self._omega = omega0
        self._diameter = diameter

    def pos(self):
        x = self._r * sin(self._theta)
        y = self._r * cos(self._theta)
        return (x+250, y+250)
    
    def move(self):
        self._theta += self._omega

    def getradius(self):
        radius = self._diameter / 2
        return radius
                
r0 = float(input("Raggio? "))
theta0 = float(input("Angolo? "))
omega0 = float(input("Velocità? "))
diameter = float(input("Diametro del pianeta? (dimensione)"))

p = Planet(r0, theta0, omega0, diameter)

print("x,y = ", p.pos())
print("Diametro = ", diameter)
print("\n")

canvas = canvas_init((500, 500))

def update():
    global r0,theta0,omega0,p,a
    canvas_fill(canvas, (255, 255, 255))
    p.move()
    draw_circle(canvas, (0, 255, 0), (p.pos()), p.getradius())
    print(p.pos()) #for debug in brython console
    
set_interval(update, 1000 // 5 )






