def FizzBuzz(n):
    answer = []

    for i in range (1, n+1): #controllo i divisori di ogni numero fino ad n.
        if i%3 == 0 and i%5 == 0: #per come è strutturato il ciclo, è necessario che questa sia la prima cond. accessibile.
            answer.append('Fizzbuzz')
        elif i%3 == 0:
            answer.append('Fizz')
        elif i%5 == 0:
            answer.append('Buzz')
        else:
            answer.append(str(i))
        
    print(answer)
