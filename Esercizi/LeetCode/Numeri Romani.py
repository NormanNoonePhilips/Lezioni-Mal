class Solution:
    
    def romanToInt(s: str):
        numeriRomani = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        numero = 0
        temp = 'M'
        for x in s:
            
            if(numeriRomani[x]/numeriRomani[temp]==5 or numeriRomani[x]/numeriRomani[temp]==10):
                numero += (numeriRomani[x] - 2* numeriRomani[temp])
                print(numero)
            else:
                numero += numeriRomani[x]
                print(numero)
            temp = x
        return numero
            