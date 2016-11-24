from game2d import *
from random import *
from actor import *

class Arena_SuperMario(Arena):

    def __init__(self, width, height):
        self._w, self._h = width, height
        self._actors = []

    def game_lost(self):
        if mario.death() == True and luigi.death() == True:
            return True
        else:
            return False

    def game_win(self):
        if mario.end_level() == True or luigi.end_level() == True:
            return True
        else:
            return False
    

class Jumper(Actor):
    W, H = 20, 15
    SPEED = 5.1
    GRAVITY = 0.5
    MAX_SPEED = 8

    def __init__(self, arena, x, y, synX, synY):
        self._x, self._y = x, y
        self._dx, self._dy = 0, 0
        self._synX, self._synY = synX, synY
        self._death = False
        self._won = False
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self.H:
            arena.remove(self)
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

    def death(self):
        if not self in arena.actors():
            return True
        else:
            return False

    def end_level(self):
        if self._won == True:
            return True
        else:
            return False
        
            
    def collide(self, other):
        
        if isinstance(other, Goomba):
            bx, by, bw, bh = self.rect()  # actor's pos
            wx, wy, ww, wh = other.rect() # enemy's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            border_up, border_down = (0, wy - bh - by), (0, wy + wh - by)
            border_left, border_right = (wx - bw - bx, 0), (wx + ww - bx, 0)
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))
            if move == border_left:
                arena.remove(self)
            if move == border_right:
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
            if move[1] < 0:
                self._dy = 5 
                self._landed = True
            elif move == borders_distance[3]:
                self._dy = -self._dy
               

        if isinstance(other, Flag):
            self._won = True
            
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

    def jump(self):
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

class Slider(Actor):
    W, H = 15, 15
    SPEED = 6
    GRAVITY = 0.5
    MAX_SPEED = 8

    def __init__(self, arena, x, y, synX, synY):
        self._x, self._y = x, y
        self._dx, self._dy = 2, 0
        self._synX, self._synY = synX, synY
        self._death = False
        self._landed = False
        self._arena = arena
        arena.add(self)

    def move(self):
        global view_x, view_y
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
            
        r = randrange(25)

        self._x += self._dx       
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self.W: 
            self._x = arena_w - self.W
            
        if r == 1:
            self._dx = -self._dx
        
        if self._x < 0:
            self._x = -self._x


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
            if move[1] < 0:
                self._dy = 1 
                self._landed = True
            elif move == borders_distance[3]:
                self._dy = -self._dy

        if isinstance(other, Jumper):
            bx, by, bw, bh = self.rect()  # actor's pos
            wx, wy, ww, wh = other.rect() # wall's pos
            borders_distance = [(wx - bw - bx, 0), (wx + ww - bx, 0),
                                (0, wy - bh - by), (0, wy + wh - by)]
            # move to the nearest border: left, right, top or bottom
            move = min(borders_distance, key=lambda m: abs(m[0] + m[1]))

            border_up, border_down = (0, wy - bh - by), (0, wy + wh - by)
            border_left, border_right = (wx - bw - bx, 0), (wx + ww - bx, 0)
            
            self._x += move[0]
            self._y += move[1]

            if move == border_down:

            self.W, self.H = 15, 7
            self._synX, self._synY = 60, 384

            arena.remove(self)
                


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

class Goomba(Slider):
    pass


class Object():

    def __init__(self, arena, x, y, w, h, synX, synY):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._synX, self._synY = synX, synY

    def move(self):
        pass

    def collide(self, other):
        pass
        
    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return self._synX, self._synY

class Wall(Object):
    
    def __init__(self, arena, x, y, w, h, synX, synY):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._synX, self._synY = synX, synY
        self._arena = arena
        arena.add(self)

class Flag(Object):
    def __init__(self, arena, x, y, w, h, synX, synY):
        self._x, self._y = x, y
        self._w, self._h = w, h
        self._synX, self._synY = synX, synY
        self._arena = arena
        arena.add(self)

class Cloud(Object):
    pass

class Castle(Object):
    pass


   
def update():
    arena_w, arena_h = arena.size()
    image_blit(canvas, background, (0, 0))

    #, area=(view_x, view_y, view_w, view_h))
    
    arena.move_all()
#    global view_x, view_w
#    x, y, w, h = mario.rect()
  
#    if x >= view_w/2 + view_x:
#        view_x += mario.SPEED
#   if x < view_w/2 + view_x:
#        view_x -= mario.SPEED

    for a in objects:
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        image_blit(canvas, sprites, (x, y), area = (xs, ys, w, h))
    
    for a in arena.actors():
        x, y, w, h = a.rect()
        xs, ys = a.symbol()
        image_blit(canvas, sprites, (x, y), area = (xs, ys, w, h))
    
    if arena.game_lost() == True:
        draw_text(canvas, "GAME OVER!", (255, 0, 0), (int((arena_w / 2) - 150), int((arena_h / 2)) - 30), 50)
    elif arena.game_win() == True:
        draw_text(canvas, "YOU WON!", (255, 0, 0), (int((arena_w / 2) - 150), int((arena_h / 2)) - 30), 50)

    
    
 
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


#---------------------------------------------

arena = Arena_SuperMario(995, 240)

#---------------------------------------------

mario = Mario(arena, 70, 10, 210, 0)
luigi = Luigi(arena, 50, 10, 210, 188)
goomba = Goomba(arena, 800, 205, 0, 380)

#---------------------------------------------

objects = []
cube = Wall(arena, 550, 100, 16, 16, 4, 641)
objects.append(cube)
cube1 = Wall(arena, 116, 120, 16, 16, 4, 641)
objects.append(cube1)
cube2 = Wall(arena, 132, 120, 16, 16, 4, 641)
objects.append(cube2)
cube3 = Wall(arena, 400, 180, 16, 16, 79, 1605)
objects.append(cube3)
cube4 = Wall(arena, 416, 180, 16, 16, 79, 1605)
objects.append(cube4)
cube5 = Wall(arena, 432, 180, 16, 16, 79, 1605)
objects.append(cube5)


tube = Wall(arena, 50, 155, 35, 70, 309, 1167)
objects.append(tube)

castle = Castle(arena, 809, 55, 147, 175, 79, 1518)
objects.append(castle)

flag = Flag(arena, 970, 129, 20, 101, 250, 1345)
objects.append(flag)

terrain = Wall(arena, 30, 185, 128, 55, 2, 889)
objects.append(terrain)
terrain1 = Wall(arena, 250, 205, 80, 35, 130, 913)
objects.append(terrain1)
terrain2 = Wall(arena, 500, 152, 128, 88, 2, 889)
objects.append(terrain2)
terrain3 = Wall(arena, 715, 230, 95, 88, 2, 889)
objects.append(terrain3)
terrain5 = Wall(arena, 810, 230, 95, 10, 4, 889)
objects.append(terrain5)
terrain6 = Wall(arena, 900, 230, 95, 10, 4, 889)
objects.append(terrain6)

cloud1 = Cloud(arena, 120, 30, 65, 25, 144, 820)
objects.append(cloud1)
cloud2 = Cloud(arena, 250, 70, 65, 25, 144, 820)
objects.append(cloud2)
cloud3 = Cloud(arena, 350, 50, 65, 25, 144, 820)
objects.append(cloud3)
cloud4 = Cloud(arena, 550, 30, 65, 25, 144, 820)
objects.append(cloud4)
cloud5 = Cloud(arena, 750, 80, 65, 25, 144, 820)
objects.append(cloud5)
cloud6 = Cloud(arena, 900, 20, 65, 25, 144, 820)
objects.append(cloud6)
cloud7 = Cloud(arena, 450, 90, 35, 25, 210, 820)
objects.append(cloud7)
cloud8 = Cloud(arena, 680, 50, 35, 25, 210, 820)
objects.append(cloud8)
cloud9 = Cloud(arena, 20, 50, 35, 25, 210, 820)
objects.append(cloud9)

#----------------------------------------------

##view_x, view_y, view_w, view_h = 0, 0, 300, 240
canvas = canvas_init((arena.size()))
##canvas = canvas_init((view_w, view_h))
sprites = image_load("smb_sprites.png")
background = image_load("background.png")

set_interval(update, 1000 // 30)

doc.onkeydown = keydown
doc.onkeyup = keyup
