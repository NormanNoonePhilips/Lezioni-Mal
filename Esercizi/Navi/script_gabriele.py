#creo plancia con input navi (a,b,c,d,e)
#------------------ho provato questo metodo ma non worka perchè crea liste con lo stesso nome e anche usando indici diversi modificando una riga cambia anche le altre---------------
# def plancia():
#     plancia=[]
#     riga= ['0','0','0','0','0','0','0','0','0','0']
#     for i in range(10):
#         plancia.append(riga)
#     return plancia
#--------------------------------------------------
#creo  una stampa della plancia senza parentesi quadre(mi aspetto una matrice 10x10 di zeri)
def initPlancia() -> list:
    matrice = []
    r = []
    for i in range(10):
        for j in range(10):
            r.append('0')
        matrice.append(r)
        r = []
    return matrice
#creo funzione che mi printa la plancia 
def printplancia(plancia):
    for i in range(len(plancia)):
        for j in range(len(plancia[i])):
            print(plancia[i][j], end='  ')
        print()

#inserimento navi al'interno della plancia (ordine prescelto)
def navi(plancia):
    
    # ----------------------------avevo pensato di fare cosi ma non è efficiente---------------------------
    # a=['a']
    # b=['b']
    # c=['c']
    # d=['d']
    # e=['e']
    # quindi potrei sostituire coordinate con lettere delle navi direttamente
    
    plancia[0][2]='a' 
    plancia[0][3] = 'a'
    plancia[0][4] = 'a'
    plancia[0][5] = 'a'
    plancia[2][7] = 'b'
    plancia[2][8] = 'b'
    plancia[2][9] = 'b'
    plancia[5][7] = 'd'
    plancia[6][7] = 'd'
    plancia[7][0] = 'c'
    plancia[8][0] = 'c'
    plancia[9][5] = 'e'

#chiamo le funzioni 
plancia= initPlancia()
navi(plancia)
printplancia(plancia)
