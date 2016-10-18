i = int(input("Numero? 0 per terminare"))

count = 0
total = 0
sequence = []
x = sequence.append(i)

while i != 0:
    i = int(input("Numero? 0 per terminare"))
    count += i
    total += 1
    sequence.append(i)

if count != 0:
    print("La media è:", count / total)

for x in sequence:
    if x < ( count / total ):
        print("Valori sotto la media:" ,x)
    else:
        print("Valori sopra la media:" ,x)
    
    
