from math import *
from game2d import *

class Planet:
    
    def __init__(self, r0, theta0, omega0, diameter0, colore0):
        self._r = r0
        self._theta = theta0
        self._omega = omega0
        self._diameter = diameter0
        self._colore = colore0
        
    def rect(self):
        radius = self._diameter / 2
        return radius
    

    def rect1(self):
        return self._colore
    
    def pos(self):
        x = self._r * sin(self._theta)
        y = self._r * cos(self._theta) 
        return x,y

    def move(self):
        self._theta += self._omega

def update():
    canvas_fill(canvas, (255,255,255))
    
    for p in planets :
        p.move()
        x1, y1 = p.pos()
        draw_circle(canvas, (p.rect1()), (x1+250, y1+250), p.rect())


planets = [Planet(30,0.52,0.3,20,(0,255,0)), Planet(80,0.4,0.2,25,(255,0,0))]
canvas = canvas_init((500,500))
set_interval(update, 1000//30)



    
    
