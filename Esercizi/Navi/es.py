#DISCLAIMER: L'ESERCIZIO É FINITO, NON OTTIMIZZATO. 
#"MOLTE COSE POTREBBERO ESSERE FATTE MEGLIO MA A VOLER SVILUPPARE UN SOFTWARE GIÀ OTTIMIZZATO PARTENDO DA 0 SI FANNO SOLO DANNI." - MATTEO BESUTTI (C) 2022

def initPlancia() -> list:
    plancia = []
    r = []
    for i in range(10):
        for j in range(10):
            r.append('0')
        plancia.append(r)
        r = []
    return plancia

#Controlla nella plancia se la posizione è utilizzabile, dati una x ed y iniziali
def checkPosAvailability(pln, tipo_nave, orientamento, x, y) -> bool:
    match(orientamento):
        case "v":
            match(tipo_nave):
                case "a":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] and pln[y][x+2] and pln[y][x+3]:
                        return True
                case "b":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1] and pln[y][x+2]:
                        return True
                case "c":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1]:
                        return True
                case "d":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y][x+1]:
                        return True
                case "e":
                    if pln[y][x] != '0':
                        return False
                    else:
                        return True
        case "o":
            match(tipo_nave):
                case "a":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] and pln[y+2][x] and pln[y+3][x]:
                        return True
                case "b":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x] and pln[y+2][x]:
                        return True
                case "c":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x]:
                        return True
                case "d":
                    if pln[y][x] != '0':
                        return False
                    elif pln[y+1][x]:
                        return True
                case "e":
                    if pln[y][x] != '0':
                        return False
                    else:
                        return True   

plancia = initPlancia()
for riga in plancia:
    print(riga)
