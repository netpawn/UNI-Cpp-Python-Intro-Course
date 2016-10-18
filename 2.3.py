from math import sqrt
#print("Scrivi Heron e inserisci i lati")
def heron(a, b, c):

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    float(area)
    
    return area


    
def main():
    a = float(input("Lato a"))
    b = float(input("Lato b"))
    c = float(input("Lato c"))

    area = heron(a, b, c)
    print(area)

if __name__ == "__main__":
    main()
