x = str(input("Name?"))
count = 0
total = 0
lista = []

while x != "":
    
    y = int(input("Val?"))
    pt = (x, y)
    count += pt[1]
    total += 1
    x = str(input("Name?"))
    lista.append(pt)
    
avgx = ( count / total )
print("The average is:", avgx)

for i in lista:
    if i[1] > avgx:
        print("Name with values above the average: " , i[0])
    elif i[1] < avgx:
        print("Names with values under the average: " , i[0])
    else:
        print("Names with values equal the average: ", i[0])
        
        

