def lunghezza(numero):
    for i in range(8):
        if (numero==0 or i==7):
            return i
        else:
            numero=numero//10

def controllaPalindromo(numero):
    if(numero>=(pow(2,31)-1) or numero<0):
        return False
    for i in range(lunghezza(numero)-1,0,-2):
        if(numero//pow(10,i) != numero%10):
            return False 
        numero=(numero%pow(10,i))//10
         
    return True

numero= 12321
controllaPalindromo(numero)
