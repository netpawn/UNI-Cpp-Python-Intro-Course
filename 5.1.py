#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from game2d import *
from random import choice, randrange
from actor import *

class Turtle(Actor):
    W, H = 20, 20
    SPEED = 5

    def __init__(self, arena, x, y):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()

        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self.H:
            self._y = arena_h - self.H
            self._landed = True

        if not self._landed:
            self._dy += 0.5
            
        self._x += self._dx       
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self.W:
            self._x = arena_w - self.W

    def go_left(self):
        self._dx, self._dy = -self.SPEED, 0
        
    def go_right(self):
        self._dx, self._dy = self.SPEED, 0

    def stay(self):
        self._dx, self._dy = 0, 0

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 20

    def jump(self):
        if self._landed:
            self._dy = -self.SPEED * 2
            self._landed = False

        
def update():
    canvas_fill(canvas, (0, 0, 0))
    arena.move_all()
    for t in arena.actors():
        xt, yt, w, h = t.rect()
        image_blit(canvas, turtleimg, (xt, yt))


def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.rect())


def keydown(event):
    code = event.code
    if code == "ArrowRight":
        Turtle.go_right()
    elif code == "ArrowLeft":
        Turtle.go_left()
    elif code == "Space":
        Turtle.jump()

def keyup(event):
    code = event.code
    if code in ("ArrowLeft", "ArrowRight"):
        Turtle.stay()

        
canvas = canvas_init((320, 240))
turtleimg = image_load("turtle.png")

arena = Arena(320, 240)
Turtle = Turtle(arena, 10, 10)

set_interval(update, 1000 // 30)

doc.onkeydown = keydown
doc.onkeyup = keyup

    

