from game2d import *
from random import *
from actor import *

class Jumper(Actor):
    W, H = 20, 15
    SPEED = 4
    GRAVITY = 0.5
    MAX_SPEED = 8

    def __init__(self, arena, x, y, synX, synY):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._synX, self._synY = synX, synY
        self._death = False
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
            self._dy += self.GRAVITY
            self._dy = min(self._dy, self.MAX_SPEED)
        
        self._x += self._dx       
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self.W: 
            self._x = arena_w - self.W

    
    def jump(self):
        pass
            
    def go_left(self):
        pass
    
    def go_right(self):
        pass

    def stay(self):
        pass

    def collide(self, other):
        
        if isinstance(other, Goomba):
            bx, by, bw, bh = self.rect()  # actor's pos
            wx, wy, ww, wh = other.rect() # enemy's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            arena.remove(self)
        
        if isinstance(other, Wall):
            bx, by, bw, bh = self.rect()  # actor's pos
            wx, wy, ww, wh = other.rect() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]
            if move[1] != 0:
                self._dy = 1
            if move[1] < 0:
                self._dy = 5
                self._landed = True
        
##        if  isinstance(other, Wall):
##            x, y, w, h = other.rect()
##
##            border_left = x - self.W
##            border_right = x + w
##            border_top =  y - self.H
##            border_bottom = y + h
##
##            if abs(border_left - self._x) < (border_right - self._x):
##                nearest_x = border_left
##            else:
##                nearest_x = border_right
##                
##            if abs(border_top - self._y) < (border_bottom - self._y):
##                nearest_y = border_top
##            else:
##                nearest_y = border_bottom
##
##            if abs(nearest_x - self._x) < abs(nearest_y - self._y):
##                self._x = nearest_x
##            
##            else:
##                self._y = nearest_y
        
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return self._synX, self._synY

class Mario(Jumper):

    def jump(self): #add boolean for mario in class 
        if self._landed:
            if self._dx >= 0:
                self._synX, self._synY = 355, 0

            elif self._dx < 0:
                self._synX, self._synY = 28, 0
            
            self._dy = -self.MAX_SPEED
            self._landed = False
            
    def go_left(self):
        self._synX, self._synY = 175, 0
        self._dx = -self.SPEED
        
    def go_right(self):
        self._synX, self._synY = 210, 0
        self._dx = self.SPEED

    def stay(self):
        if self._dx > 0:
            self._synX, self._synY = 210, 0
            
        elif self._dx < 0:
            self._synX, self._synY = 175, 0

        self._dx = 0   

class Luigi(Jumper):
    
    def jump(self):
        if self._landed:
            if self._dx >= 0:
                self._synX, self._synY = 355, 188

            elif self._dx < 0:
                self._synX, self._synY = 28, 188
        
            
            self._dy = -self.MAX_SPEED
            self._landed = False
            
    def go_left(self):
        self._synX, self._synY = 175, 188
        self._dx = -self.SPEED
        
    def go_right(self):
        self._synX, self._synY = 210, 188
        self._dx = self.SPEED

    def stay(self):
        if self._dx > 0:
            self._synX, self._synY = 210, 188
            
        elif self._dx < 0:
            self._synX, self._synY = 175, 188

        self._dx = 0    

class Enemy(Actor):
    W, H = 15, 15
    SPEED = 4

    def __init__(self, arena, x, y, synX, synY):
        self._x, self._y = x, y
        self._dx, self._dy = 2, 0
        self._synX, self._synY = synX, synY
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        
        r = randrange(20)
    
        self._x += self._dx
        if self._x < 0:
            self._x = -self._x
        elif self._x > arena_w - self.W: 
            self._x = arena_w - self.W
        
        elif r == 1:
            self._dx = -self._dx

    def collide(self, other):
        if isinstance(other, Wall):
            bx, by, bw, bh = self.rect()  # actor's pos
            wx, wy, ww, wh = other.rect() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            self._x += move[0]
            self._y += move[1]
            if move[1] != 0:
                self._dy = 1
            if move[1] < 0:
                self._dy = 5
                self._landed = True


    def jump(self):
        pass
            
    def go_left(self):
        pass
        
    def go_right(self):
        pass
        
    def stay(self):
        pass
       
    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return self._synX, self._synY

class Goomba(Enemy):
    pass


class Wall():

    def __init__(self, arena, x, y, w, h, synX, synY):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._synX, self._synY = synX, synY
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return self._synX, self._synY


def update():
    image_blit(canvas, background, (0, 0))
    
    for a in walls:
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        image_blit(canvas, sprites, (x, y), area = (xs, ys, w, h))
    
    for a in arena.actors():
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        image_blit(canvas, sprites, (x, y), area = (xs, ys, w, h))

    arena.move_all()

def print_arena(arena):
    for a in arena.actors():
        print(type(a).__name__, '@', a.rect())


def keydown(event):
    code = event.keyCode
    if code == 39:
        mario.go_right()
    elif code == 37:
        mario.go_left()
    elif code == 38:
        mario.jump()
    elif code == 68:
        luigi.go_right()
    elif code == 65:
        luigi.go_left()
    elif code == 87:
        luigi.jump()
        
def keyup(event):
    code = event.keyCode
    if code in (37, 39):
        mario.stay()
    if code in (65, 68):
        luigi.stay()


arena = Arena(995, 240)

mario = Mario(arena, 10, 10, 210, 0)
luigi = Luigi(arena, 20, 10, 210, 188)
goomba = Goomba(arena, 100, 225, 0, 380)
#---------------------------------------------
walls = []
wall = Wall(arena, 150, 160, 20, 20, 5, 640)
walls.append(wall)
tubo = Wall(arena, 240, 197, 35, 70, 309, 1167)
walls.append(tubo)
terrain1 = Wall(arena, 0, 230, 120, 10, 4, 889)
walls.append(terrain1)
terrain1 = Wall(arena, 0, 230, 120, 10, 4, 889)
walls.append(terrain1)
terrain2 = Wall(arena, 121, 230, 120, 10, 4, 889)
walls.append(terrain2)

#----------------------------------------------
canvas = canvas_init((arena.size()))
sprites = image_load("smb_sprites.png")
background = image_load("background.png")

set_interval(update, 1000 // 30)

doc.onkeydown = keydown
doc.onkeyup = keyup
