from random import *
   
n = int(input("You are playing dice. How many throws? "))

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

with open("dice.txt", "w") as f1:
    for i in range(n):
        a = choice(dice1)
        b = choice(dice2)
        print(a, b)
        print(a, b, file=f1)

    
