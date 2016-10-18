from math import *

class Planet:
    def __init__(self, r0, theta0):
        self._r = r0
        self._theta = theta0 

    def pos(self):
        x = self._r * sin(self._theta)
        y = self._r * cos(self._theta)
        return (x, y)
        
r0 = float(input("Raggio? "))
theta0 = float(input("Angolo? "))

p = Planet(r0, theta0)

print("x,y = ", p.pos())

