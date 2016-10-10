i = float(input("Numero?"))

maxi = i
mini = i

while i != 0:
    i = float(input("Numero?"))
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i
print("MAX =", maxi, "MIN =", mini)
