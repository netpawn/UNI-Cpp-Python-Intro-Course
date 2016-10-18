from math import *

class Planet:
    def __init__(self, r0, theta0, omega0):
        self._r = r0
        self._theta = theta0
        self._omega = omega0

    def pos(self):
        x = self._r * sin(self._theta)
        y = self._r * cos(self._theta)
        return (x, y)

    def move(self):
        self._theta += self._omega
        
        
r0 = float(input("Raggio? "))
theta0 = float(input("Angolo? "))
omega0 = float(input("Velocità? "))

p = Planet(r0, theta0, omega0)

print("x,y = ", p.pos())


while input() != "x":
    p.move()
    print(p.pos())


