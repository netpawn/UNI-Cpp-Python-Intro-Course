class Tris:
    

    def __init__(self):
        self._matrix = [["." for i in range(3)] for h in range (3)]
        
        
        
    def play(x, y):
        pass
        

    def __str__(self):
        grid = ""
        for y in range(3):
            for x in range(3):
                grid += self._matrix[y * 3 + x]
            grid += "\n"
        return grid
##        for i in self._matrix:
##            print ((" "))
    
Tris()
print(Tris())

for i in range(8):
    x = int(input("X? "))
    y = int(input("Y? "))
    Tris.move(x, y)

        
        



