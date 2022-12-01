#                                                DISCLAIMER: L'ESERCIZIO É FINITO, NON OTTIMIZZATO. 
#       "MOLTE COSE POTREBBERO ESSERE FATTE MEGLIO MA A VOLER SVILUPPARE UN SOFTWARE GIÀ OTTIMIZZATO PARTENDO DA 0 SI FANNO SOLO DANNI." - MATTEO BESUTTI (C) 2022
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#inizalizza un plancia vuota 10x10
def initPlancia() -> list:
    plancia = []
    r = []
    for i in range(10):
        for j in range(10):
            r.append('0')
        plancia.append(r)
        r = []
    return plancia

#Controlla nella plancia se la posizione è utilizzabile, dati una x ed y iniziali, il tipo di nave ed il suo orientamento (V-erticale: Dall'alto verso il basso // O-rizzontale: da sinistra verso destra)
def checkPosAvailability(pln, tipo_nave, orientamento, x, y) -> bool:
    x = int(x)
    y = int(y)
    match(orientamento):
        case "v":
            match(tipo_nave):
                case "a":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] == '0' and pln[y][x+2] == '0' and pln[y][x+3] == '0':
                        return True
                case "b":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] == '0' and pln[y][x+2] == '0':
                        return True
                case "c":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] == '0':
                        return True
                case "d":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] == '0':
                        return True
                case "e":
                    if pln[y][x] != '0':
                        return False
                    else:
                        return True
                case _def:
                    return False
        case "o":
            match(tipo_nave):
                case "a":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] == '0' and pln[y+2][x] == '0' and pln[y+3][x] == '0':
                        return True
                case "b":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] == '0' and pln[y+2][x] == '0':
                        return True
                case "c":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] == '0':
                        return True
                case "d":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] == '0':
                        return True
                case "e":
                    if pln[y][x] != '0':
                        return False
                    else:
                        return True 
                case _def:
                    return False  
        case _def:
            return False

#Posiziona la nave del tipo voluto nella posizione ed orientamento desiderato
def placeShip(pln, tipo_nave, orientamento, x, y) -> None:
    x = int(x)
    y = int(y)          #Si, sono gli stessi argomenti di checkPosAvailability, e allora?
    if checkPosAvailability(pln, tipo_nave, orientamento, x, y):    #controllo della posizione, intanto controlla anche tutto il resto, al minimo errore esce subito dalla funzione
        if orientamento == "o":
            match(tipo_nave):
                case "a":
                    for i in range(0,4):
                        pln[y][x+i] = 'a'
                case "b":
                    for i in range(0,3):
                        pln[y][x+i] = 'b'
                case "c":
                    for i in range(0,2):
                        pln[y][x+i] = 'c'
                case "d":
                    for i in range(0,2):
                        pln[y][x+i] = 'd'
                case "e":
                    pln[y][x] = 'e'                
        elif orientamento == "v":
            match(tipo_nave):
                case "a":
                    for i in range(0,4):
                        pln[y+i][x] = 'a'
                case "b":
                    for i in range(0,3):
                        pln[y+i][x] = 'b'
                case "c":
                    for i in range(0,2):
                        pln[y+i][x] = 'c'
                case "d":
                    for i in range(0,2):
                        pln[y+i][x] = 'd'
                case "e":
                    pln[y][x] = 'e' 
    else:
        print("Spazio non disponibile oppure Nave/Orientamento non valido.")
        return False

#stampa la plancia attuale, in un modo presentabile
def stamPlancia(plancia):
    cnt = 0
    print("",0,1,2,3,4,5,6,7,8,9, sep="\t")
    for riga in plancia:
        print(str(cnt), end="\t")
        for elem in riga:
            print(elem, end="\t")
        print("")
        cnt +=1

if __name__ == '__main__':              #potrebbe essere avanzato per gli altri ma heyyyy, devo comunque applicare una minima parte di quello che imparo anche in uni
    plancia = initPlancia()            #se non ho il senso dell'orientamento tritato, dovrebbe partire dall'angolo in alto a sinistra
    while True:#love you mal <3
        stamPlancia(plancia)
        print("\n1. Inserisci Nave\n0. Esci")
        opz = input("Inserire opzione: ")
        match(opz):
            case "1":
                tipo_n = input("\"a\"-> 4 Spazi\n\"b\"-> 3 Spazi\n\"c\"-> 2 Spazi\n\"d\"-> 2 Spazi\n\"e\"-> 1 Spazio\n\n Inserire tipo di nave:")
                orient = input("\"o\" - Orizzontale\n\"v\" - Verticale\n\nInserisci un orientamento: ")
                x = input("Inserisci coordinata X di partenza: ")
                y = input("Inserisci coordinata Y di partenza: ")
                placeShip(plancia, tipo_n, orient, x, y)
            case "0":
                exit()

