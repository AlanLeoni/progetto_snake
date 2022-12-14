##
## Modulo campo da gioco
##

def campo_crea1 (c: int, r: int):
    # Imposta il gioco con un campo di c colonne e r righe.
    # Sia c che r devono essere numeri positivi.
    global campo
    campo = []
    for y in range(r):
        riga = []
        for x in range(c):
            riga.append(' ')
        campo.append(riga)

def campo_crea2 (c: int, r: int):
    # Imposta il gioco con un campo di c colonne e r righe.
    # Sia c che r devono essere numeri positivi.
    global campo
    campo = [[' ' for x in range(c)] for y in range(r)]
    
campo_crea = campo_crea1

def campo_altezza() -> int:
    # Ritorna il numero di righe del campo di gioco.
    return len(campo)

def campo_larghezza() -> int:
    # Ritorna il numero di colonne del campo di gioco.
    return len(campo[0])

def campo_cancella ():
    # Cancella il campo di gioco, reimpostando tutte le celle al
    # valore di cella vuota.  Questa funzione va fatta seguire da
    # snake_inizia.
    campo_crea(campo_larghezza(), campo_altezza())

def campo_cella (c: int, r: int) -> str:
    # Ritorna la cella del campo di gioco alla colonna c, riga r.
    return campo[r][c]

def campo_imposta_cella (c: int, r: int, valore: str):
    # Imposta la cella del campo di gioco alla colonna c, riga r.
    global campo
    campo[r][c] = valore

##
## Modulo snake
##

DIR_NORD = 'N'
DIR_SUD = 'S'
DIR_EST = 'E'
DIR_OVEST = 'O'

def snake_inizia (c: int, r: int, d: str, l: int):
    # Inizia il gioco con un serpente di dimensione iniziale 1 (solo
    # testa) con la testa alla colonna c, riga r, e con una direzione
    # iniziale di movimento d, che può essere uno dei valori DIR_NORD,
    # DIR_SUD, DIR_EST, DIR_OVEST.  Questa funzione va preceduta
    # immediatamente da campo_cancella.
    pass

def snake_un_passo () -> bool:
    # Esegue un passo del serpente.  Ritorna il valore True se il
    # passo è andato a buon fine e quindi il gioco può continuare,
    # oppure False se il passo ha portato alla fine del gioco.
    return True

def snake_direzione (d: str):
    # Imposta la direzione di movimento della testa del serpente.  d
    # indica la direzione, può essere uno dei valori DIR_NORD,
    # DIR_SUD, DIR_EST, DIR_OVEST.  La direzione data è effettiva per
    # il prossimo passo del serpente e fino a quando non venga di
    # nuovo impostata con questa stessa funzione snake_direzione.
    pass
