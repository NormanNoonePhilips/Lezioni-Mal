def inToRoman(num):
    #dizionario numeri romani
    numRom = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",   
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",  
        100: "C",
        400: "CD",  
        500: "D", 
        900: "CM",
        1000: "M"
    }
    res = ''
    #lista di chiavi relativi ai numeri che vado a ciclare
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n <= num:             #controllo che il valore "chiave" sia minore o uguale al numero 
            res += numRom[n]        #aggiungo alla soluzione il numero romano
            num-=n                  #sottraggo al numero da convertire il valore della chiave (es: se n è 1500, a res viene aggiunto "D", e poi viene fatto 'num-n' -> 1500-500, e ricomincia daccapo)
    print(res)


inToRoman(3)
inToRoman(58)
inToRoman(1994)