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
#diamo le risposte
if x > 0:
    print("Due soluzioni reali")
if x < 0:
    print("Nessuna soluzione :(")
if x == 0:
    print("Una sola soluzione reale")
