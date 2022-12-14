plancia = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#questa lista serve solo se si vuole implementare un sistema per permettere a un utente di iserire le informazioni da terminale o in altro modo
navi = [
    {
        'nome': 'a',
        'lunghezza': 4
    },
    {
        'nome': 'b',
        'lunghezza': 3
    },
    {
        'nome': 'c',
        'lunghezza': 2
    },
    {
        'nome': 'd',
        'lunghezza': 2
    },
    {
        'nome': 'e',
        'lunghezza': 1
    },
]


def mostraPlancia():
    i = 0
    print('   1  2  3  4  5  6  7  8  9  10')
    for x in plancia:
        print(chr(i + 65) + ' ' + str(x))
        i += 1


def elencoNavi(navi):
    for x in navi:
        print(x)


def aggiungiNave(nome, lunghezza, inizio, verso):
    x, y = inizio.split()
    try:
        if (verso == 'destra'):
            i = 0
            for i in range(lunghezza):
                if (plancia[int(x)][int(y) + i] != 0):
                    return "errore: si sovrappone a un'altra nave"
                else:
                    plancia[int(x)][int(y) + i] = nome
        elif (verso == 'basso'):
            i = 0
            for i in range(lunghezza):
                if (plancia[x + i][y] != 0):
                    return "errore: si sovrappone a un'altra nave"
                else:
                    plancia[x][y + i] = nome
        return 'bravo, nave inserita correttamente'
    except:
        return 'errore: fuori dai margini della plancia'

mostraPlancia()
print(aggiungiNave('a', 4, '0 0', 'destra'))
mostraPlancia()
