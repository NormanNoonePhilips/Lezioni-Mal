def Railroad(n, temp, Own):                 #rende il numero un array di singole cifre (n = numero, temp = numero temporaneo, Own = n messo a array)
  if(n>=10):
    temp = n%10                             #ottengo ultima cifra
    Own.append(temp)
    n = ((n-temp)/10)                       #tolgo l'ultima cifra da n
    Railroad(n, temp, Own)
  else:
    temp = n
    Own.append(temp)
  return(Own)


def Gate(Own, wall, gate, cont):            #Own = n in array, wall è linghezza di Own, gate = vero/falso, cont = contatore
  if(cont<wall and gate):                   #se abbiamo la prova ch enon è palindromo, inutile continuare a cercare
    if( Own[cont] != Own[(-cont-1)] ):      #se elemento array è diverso da quelllo specchaitto.... (esempio, posizione 0 e -1, oppure 1 e -2 e così via)
      gate = False
    gate = Gate(Own, wall, gate, cont+1)
  return(gate)


esc = 'n'                                                                           #serve per fare più test senza avviare il debug ogni volta
Tool = ['y','n','Y','N']                                                            #stessa utilità di esc
while(esc != 'y'):
  
    n = int(input("inserire un numero fra -2'147'483'648 e +2'147'483'648: "))      #questo è il numero iniziale
    wall = len(Own)
    bool gate = True                                                                #vedi def Gate
    if (n<0):
      gate = false                                                                  # se è negativo, non può esserer palindromo
    elif(n>=10):                                                                    # se è una cifra sola, è automaticamente palindromo
      int Own[] = Railroad(n,0,Own)                                                 #vedi def Railroad
      gate = Gate(Own, wall, gate, 0)
    print('caso palindromia: ', gate)
    
    esc = input('uscire dal programma? y/n ' )                                      #per fare più test senza avviare il debug ogni volta
    while(not(esc in Tool)):
        print('ERRORE: valore non valido.')
        esc = input('uscire dal programma? y/n ' ) 
