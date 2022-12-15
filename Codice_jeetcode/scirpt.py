def FizzBuzz(n):
    i = 1 
    Soluzione = []    #creo lista vuota che andra a contenere il risultato
    while i <= n:   #loop check condizioni di i e Soluzione.append del valore associato alla condizione 
        a = i % 3 == 0
        b = i % 5 == 0
        if a and b:
            Soluzione.append('Fizzbuzz')
        elif a and not b:
            Soluzione.append('Fizz')
        elif b and not a:
            Soluzione.append('Buzz')
        else:
            Soluzione.append(str(i))
        i += 1
    print(Soluzione)
    return Soluzione  #ritorno stringa falla funzione (opzionale)


FizzBuzz(15)