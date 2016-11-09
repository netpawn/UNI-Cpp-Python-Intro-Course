
from game2d import *
from random import choice, randrange
from actor import *

class Ball(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = self.SPEED, self.SPEED
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        if not (0 <= self._x + self._dx <= arena_w - self.W):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= arena_h - self.H):
            self._dy = -self._dy
        self._x += self._dx
        self._y += self._dy

    def collide(self, other):
        if  isinstance(other, Wall):
            x, y, w, h = other.rect()

            border_left = x - self.W
            border_right = x + w
            border_top =  y - self.H
            border_bottom = y + h

            if abs(border_left - self._x) < (border_right - self._x):
                nearest_x = border_left
            else:
                nearest_x = border_right
                
            if abs(border_top - self._y) < (border_bottom - self._y):
                nearest_y = border_top
            else:
                nearest_y = border_bottom

            if abs(nearest_x - self._x) < abs(nearest_y - self._y):
                self._x = nearest_x
            else:
                self._y = nearest_y
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 0


class Wall(Actor):

    def __init__(self, arena, x, y, w, h):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        pass

def update():
    canvas_fill(canvas, (0, 0, 0))
    arena.move_all()
    for e in arena.actors():
        if isinstance(e, Wall):
            draw_rect(canvas, (125, 125, 125), e.rect())
        else:
            xb, yb, w, h = e.rect()
            image_blit(canvas, ballimg, (xb , yb))


canvas = canvas_init((320, 240))
ballimg = image_load("ball.png")

arena = Arena(320, 240)
Ball(arena, 60, 50)
Ball(arena, 30, 20)
Wall(arena, 100, 80, 120, 70)

set_interval(update, 1000 // 30)
