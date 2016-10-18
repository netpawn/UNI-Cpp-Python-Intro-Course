testo = input("Testo ?")
total = 0
n = len(testo)

for char in testo:
    if "A" <= char and char <= "Z":
        total += 1

        per = n/total*100

print(total)
print(per ,"%")
