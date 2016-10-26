from random import randint

board = []
#creata la board scegliamo il numero di cols x rows
r = int(input("Rows x Cols?"))

for x in range(r):
    board.append(["0"] * r)

#definisco print board e uso .join per spaziare gli zeri
def print_board(board):
    for row in board:
        print ((" ").join(row))
#printiamo la board
print("Let's wreck some ships!")
print_board(board)

#creiamo la nostra barca
def random_row(board):
    return randint(0, len(board) -1)
def random_col(board):
    return randint(0, len(board) -1)
#questo -1 ed il prossimo, linea 52, evita un errore (linea 55, list index out of range) 

ship_row = random_row(board)
ship_col = random_col(board)

print ("")


#Le prossime due è dove si trova la barca
print(ship_row)
print(ship_col)

#passiamo al gioco vero. massimo n turni a seconda delle cols x rows scelte
#aumentiamo i turni ogni volta
#diamo da scegliere row e col all'utente

for turn in range(r):
    print("")
    print(("Turn"), turn +1)
    guess_row = int(input("Riga?"))
    guess_col = int(input("Colonna?"))

#ora vediamo se ci ha azzeccato
    if guess_row == ship_row and guess_col == ship_col:
        print("Sei un genio! Affondata!")
        break
#vari if per tentativi: fuori, mancata, game over
#utilissimo \ per andare a capo ma stare "sulla stessa riga"
    else:
        if (guess_row < 0 or guess_row > r - 1)\
        or (guess_col < 0 or guess_col > r - 1):
            print("Ti chiamavano cecchino!")
        elif (board[guess_row][guess_col] == "X"):
            print("Ci hai già provato...")
        else:
            print("Missss! Dai riprova")
            board [guess_row][guess_col] = "X"


print_board(board)


with open("bs.txt", "w") as f1:
    print(board, file=f1)
