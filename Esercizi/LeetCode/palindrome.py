def palindromo(x):

    x = str(x)
    pal = False
    for i in range(len(x)):
        if x[i] != x[-i]:
            pal = True
    
    if pal:
        print("Il numero è palindromo")
    else:
        print("Il numero non è palindromo")

palindromo(121)
palindromo(-121)
palindromo(10)