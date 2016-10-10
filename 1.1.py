#variabile name contiene il nome
name = input("Who's that?")

#se il nome è admin allora digli ciao boss, altrimenti saluta il nome
#non spaziare prima di inserire "admin"
#possiamo usare + per "aggiungere stringhe assieme

if name == "admin":
    print("At your command Bboss!")
else:
    print("Wassup " + name + "?")
