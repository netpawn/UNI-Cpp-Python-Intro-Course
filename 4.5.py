from game2d import *
from actor import Actor, Arena

class FallingBall(Actor):
    
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

    def collide(self, other: Actor):
        '''Called by Arena, when the actor collides with another one
        Args:
            other: Actor -- the other actor involved in the collision
        '''
        return

    def symbol(self) -> (int, int):
        '''Return (0, 0) or the (x, y) position of current sprite in a
           larger image, containing more sprites
        Returns:
            (int, int) -- the position of current sprite
        '''
        return
    
    
class Plane(Actor):
    
    W, H = 35, 35
    ARENA_W, ARENA_H = 1000,1000
    
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._dx = 10
        self._aftercollision = 0

    def move(self):
        if not (0 <= self._x + self._dx <= Plane.ARENA_W - Plane.W):
            self._dx = -self._dx

        if self._aftercollision > 0:
            self._aftercollision -= 1
            
        self._x += self._dx

    def rect(self) -> (int, int, int, int):
        return (self._x, self._y, Plane.W, Plane.H)

    def collide(self, other: Actor):
        '''Called by Arena, when the actor collides with another one
        Args:
            other: Actor -- the other actor involved in the collision
        '''
        if (isinstance (other, FallingBall) and self._aftercollision == 0):
            self._dx = - self._dx
            self._aftercollision = 60

    def symbol(self) -> (int, int):
        '''Return (0, 0) or the (x, y) position of current sprite in a
           larger image, containing more sprites
        Returns:
            (int, int) -- the position of current sprite
        '''
        return
    
    
def update():
    image_blit(canvas, background, (0 - gx, 0 - gy))
    gameworld.move_all()
    for a in gameworld.actors():
        x, y , w , h = a.rect()
        draw_rect(canvas, (0, 255, 255), (x - gx, y - gy, w, h))
        

def keydown(event):
    global gx, gy
    code = event.code
    if code == "ArrowRight":
        gx = min(gx + 10, aw - gw)
    elif code == "ArrowLeft":
        gx = max(gx - 10, 0)
    elif code == "ArrowDown":
        gy = min(gy + 10, ah - gh)
    elif code == "ArrowUp":
        gy = max(gy - 10, 0)
        
        
aw , ah = 1000, 1000
gameworld = Arena(aw,ah)

f1 = FallingBall(10,10)
f2 = FallingBall(70,70)
p1 = Plane(1,350)
p2 = Plane(1,250)
p3 = Plane(1,150)

gameworld.add(f1)
gameworld.add(f2)
gameworld.add(p1)
gameworld.add(p2)
gameworld.add(p3)

gx, gy, gw, gh = 0, 0, 500, 300
canvas = canvas_init((gw,gh))
background = image_load("background.png")
set_interval(update, 1000 // 30)
doc.onkeydown = keydown
