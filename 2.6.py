
n = int(input("n (0 < n < 10)?"))

if n > 9 or n < 0:
    print("Error! Change value n")

else:  

    for a in range(n):
        print("\n")
        
        for b in range(a+1):
            print(b+1, end = "")
            

    
