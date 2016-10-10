from random import randrange

monete = 10
gioco = 1

while monete > 0 and gioco == 1:

    print("Monete =", monete)   #Monete ad ogni turno
    puntata = int(input("Quante monete punti? "))
    numero = int(input("Su quale numero? (Scegliere numeri compresi tra 1 e 3) "))

    #if puntata < monete and 1 <= numero <= 3:   #Regole del gioco
    secret = randrange(1,4)

    if secret == numero:
        monete += puntata
    else:
        monete -= puntata

    print("Monete =",monete)
    
    if monete != 0:
        x = input("Ti ritiri? ")
        if x == "si":
            gioco = 0
    #else:
        #print("ERROR!")
        #gioco = 0

        
    

    
