n = int(input("Inserisci un numero: "))
answer = []
for i in range(1, n+1):
    #ottengo il numero e piglio il modulo
    n1 = i%3
    n2 = i%5
    #faccio i controlli con if/elif dato che ho bisogno solo di un risultato
    if n1 == 0 and n2 != 0:
        answer.append("Fizz")
    elif n1 != 0 and n2 == 0:
        answer.append("Buzz")
    elif n1 == 0 & n2 == 0:
        answer.append("FizzBuzz")
    else:
        answer.append(str(i))
print(answer)
        