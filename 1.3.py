from math import sqrt

azione = 1

while azione == 1:         

    print("Ora ti chiedero la a, la b e la c della tua funzione  di tipo ax^2+bx+c=0")
#Salaviamo le nostre variabili
    a = input("Dimmi la a...?")
    b = input(" ora la b...")
    c = input("  infine la c!")
#convertiamo ad interi
    a = int(a)
    b = int(b)
    c = int(c)
#Ora facciamo calcolare alla macchina il delta!
    x = b*b - 4*a*c
#le facciamo calcolare anche la soluzione
    x1 = ( (-b) + (sqrt(x)) ) /2
    x2 = ( (-b) - (sqrt(x)) ) /2
#diamo le risposte
#printiamo anche il risultato
#però convertiamo in stringa la X! che prima era solamente int
#mai dimenticare str(x) ;)
    if x > 0:
        print("Due soluzioni reali")
        print("Grande! Il delta è " + str(x) )
        print("X1 = " + str(x1))
        print("X2 = " + str(x2))

    if x < 0:
        print("Nessuna soluzione :(")
    
    if x == 0:
        print("Una sola soluzione reale")
        print("Ed è " + str(x) )
        print("X1 = " + str(x1))
        print("X2 = " + str(x2))
#uscire dal programma o continuare
    uscita = (input)("ancora una? (si o no)")
    if uscita == "si":
        azione = 1
    if uscita == "no":
        azione = 0
    
   
