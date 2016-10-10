a = int(input("Lunghezza lato a? "))
b = int(input("Lunghezza lato b? "))
c = int(input("Lunghezza lato c? "))

if c > ( a + b ) or a > ( b + c ) or c > ( a + b ):
    print("I tre lati non possono formare un triangolo")
else:
    if b == a and b == c and c == a:
        print("Il triangolo è equilatero")
    elif b == c or a == b or c == a:
        print("Il triangolo è isoscele")
    elif b != c and a != b and c != a:
        print("Il triangolo è scaleno")
