def Gate(n):                    #controllo divisori
    gate = [False,False]        #primo Bool è per %3, il secondo è %5
    if(n%3==0):
        gate[0] = True
    if(n%5==0):
        gate[1] = True
    return(gate)                #l'idea è che parto immaginando che NON sia divisibile per nessuno, e poi controllo i due casi


def Answer(n):                  #restituisce FizzBuzz. Fizz, Buzz o il numero come carattere
    gate = Gate(n)
    if (gate[0] and gate[1]):   #controllo se è divisibile per 3 e per 5 assieme
        return("FizzBuzz")
    elif (gate[0]):             #in questo caso è sicuramente NON divisibile per tutti e due, controllo se %3==0
        return("Fizz")
    elif (gate[1]):             #in questo caso NON è divisibile per entrambi, e NON è divisibile per 3, controllo se %5==0
        return("Buzz")
    else:                       #NON è divisibile ne per 3 ne per 5
        return(str(n))


def FizzBuzz(n,cont,L):         #cont è un contatore (parte da 1), L è la lista dove inserire i risultati
    x = Answer(cont)            #partendo da 1, controlla Answer
    L.append(x)                 #carica la risposta
    if(cont<n):                 #fa in modo che la ricorsione si fermi quando il contatore è uguale a n
        FizzBuzz(n,cont+1,L)    #prossimo valore del contatore da controllare
    return(L)


# L'idea è che il ciclo sia  FizzBuzz(->Answer->Gate) -> FizzBuzz(->Answer->Gate) -> ... etc etc in maniera ricorsiva

esc = 'n'                                                   #serve per fare più test senza avviare il debug ogni volta
Tool = ['y','n','Y','N']                                    #stessa utilità di esc
while(esc != 'y'):
    n = int(input("inserire un numero fra 1 e 10000: "))    #questo è il numero iniziale
    L = list()                                              #questa è la lista dove immettere i risultati
    L = FizzBuzz(n,1,L)
    print(L)
    esc = input('uscire dal programma? y/n ' )               #per fare più test senza avviare il debug ogni volta
    while(not(esc in Tool)):
        print('ERRORE: valore non valido.')
        esc = input('uscire dal programma? y/n ' )
