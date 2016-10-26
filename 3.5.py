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

    def color(self, rc, gc, bc):
        rc = self._rc
        gc = self._gc
        bc = self._bc
        return (rc, gc, bc)                


how = int(input("Quanti pianeti? "))

planets = []

for i in range(how):
    r0 = float(input("Raggio? "))
    theta0 = float(input("Angolo? "))
    omega0 = float(input("Velocità? "))
    diameter = float(input("Diametro del pianeta? (dimensione)"))
    Planet(r0, theta0, omega0, diameter)
    planets.append(Planet)
    

#print("x,y = ", p.pos())
#print("Diametro = ", diameter)
#print("\n")

canvas = canvas_init((500, 500))

def update():
    global r0,theta0,omega0,planets
    canvas_fill(canvas, (255, 255, 255))
    for i in planets:
        planets[0].move()
        draw_circle(canvas, (0, 255, 0), (planets[0].pos()), planets[0].getradius())
        print(planets[0].pos()) #for debug in brython console
    
set_interval(update, 1000 // 5 )






