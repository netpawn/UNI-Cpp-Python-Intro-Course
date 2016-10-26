##f = open("dice.txt","r")
##domande = [x for x in f.readlines()] #list comprehension
##f.close()
##for x in domande:
##    print(x)

countlist = [0] * 11
results = []

with open("dice.txt", "r") as f1:
    for line in f1:
        a = str.split(line)
        a[0] = int(a[0])
        a[1] = int(a[1])
        s = int(a[0]+a[1])
        results.append(s)
        print(line.strip(), "sum:" , s)
    for s in results:
        countlist[s - 2] += 1
    for i in range(len(countlist)):
        print("Number {} - {} times".format(i+2, countlist[i]))


