def FizzBuzz(n):
    i = 1 
    Soluzione = []    #creo lista vuota che andra a contenere il risultato
    while i <= n:   #loop check condizioni di i e Soluzione.append del valore associato alla condizione 
        a = i % 3 == 0
        b = i % 5 == 0
        if a and b:              #se è divisibile per 3 e per 5...
            Soluzione.append('Fizzbuzz')
        elif a and not b:        #se è divisibile per 3 ma non per 5...
            Soluzione.append('Fizz')    
        elif b and not a:    #se è divisibile per 5 ma non per 3...
            Soluzione.append('Buzz')   
        else:               #se non è divisibile per 3 o per 5...
            Soluzione.append(str(i))    
        i += 1
    print(Soluzione)
    return Soluzione  #ritorno Soluzione dalla funzione (opzionale)


FizzBuzz(15)
