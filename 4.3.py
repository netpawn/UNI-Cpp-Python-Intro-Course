class Actor:
    def move(self): pass
    def rect(self) -> (int,int,int,int): pass

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

class Plane(Actor):
    def __init__(self, x: int, y: int)
        self._x = x
        self._y = y
        self._dx = 5

    def move(self):
        self._x += self._dx

canvas = canvas_init((1000,1000))

def update():
    canvas_fill(canvas, (0, 0, 0))
    bf1.move()
    draw_rect(canvas, (0, 255, 255), (bf1.rect()))
    
    
set_interval(update, 1000 // 40)

        
