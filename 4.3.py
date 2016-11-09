from game2d import *

class SimpleActor:
    
    def move(self): pass
    def rect(self) -> (int,int,int,int): pass
    

class FallingBall(SimpleActor):
    
    W, H = 20, 20
    ARENA_W, ARENA_H = 1000,1000

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 5
        self._dy = 5
        self._g = 9.81

    def move(self):
        if not (0 <= self._x + self._dx <= FallingBall.ARENA_W - FallingBall.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= FallingBall.ARENA_H - FallingBall.H):
            self._dy = -self._dy
            self._dy = -100

        self._x += self._dx
        self._y += self._dy
        self._dy += self._g
            
    def rect(self) -> (int, int, int, int):
        return (self._x, self._y, FallingBall.W, FallingBall.H)

class Plane(SimpleActor):
    
    W, H = 35, 35
    ARENA_W, ARENA_H = 1000,1000
    
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 10

    def move(self):
        if not (0 <= self._x + self._dx <= Plane.ARENA_W - Plane.W):
            self._dx = -self._dx
            
        self._x += self._dx

    def rect(self) -> (int, int, int, int):
        return (self._x, self._y, Plane.W, Plane.H)
        
def update():
    canvas_fill(canvas, (0, 0, 0))
    for i in ballsandplanes:
        i.move()
        x1, y1, aw, ah = i.rect()
        draw_rect(canvas, (0, 255, 255), (x1, y1, 40, 40))

canvas = canvas_init((1000,1000))
ballsandplanes = [Plane(1,200), Plane(1,250), Plane(1,300), FallingBall(10,10), FallingBall(70,70)]  
set_interval(update, 1000 // 30)

        
