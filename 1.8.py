from random import randrange

n = int(input("Inserire numero n"))

x = 0
y = 0

while n != 0:
    r = randrange (4)
    if r == 0:    #alto
        y = y - 1
    elif r == 1:  #destra
        x = x + 1
    elif r == 2:  #basso
        y = y + 1
    elif r == 3:  #sinistra
        x = x - 1
    n = n - 1
        
print("Coordinata x =", x)
print("Coordinata y =", y)
print("Distanza percorsa =", abs(x)+abs(y))
