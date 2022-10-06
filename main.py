"""
Gioco Snake
Le funzioni presenti in questo file permettono il funzionamento del gioco dello snake.
In modo particolare il gioco consiste in un serpente che si muove all'interno di un rettangolo diventando sempre più lungo
"""

import keyboard
from threading import Thread
import time

# Variabili e costanti del campo da gioco
larghezza_campo = 20
altezza_campo = 10
BORDO_ORIZZONTALE = "+" + (larghezza_campo * "-") + '+\n'
BORDO_SINISTRO = "|"
BORDO_DESTRO = "|\n"

# Variabili e costanti del serprente
pezzi_corpo = 0
x_testa = 0
y_testa = 0
direzione = "d"
TESTA = "O"
CORPO = "o"
CODA = "x"


def crea_campo() -> list[list[str]]:
    """
    (campo vuoto)
    Ritorna l'area del campo da gioco (senza bordo) definito nelle costanti
    :returns: una lista di liste di stringe vuote
    """
    campo = []
    for y in range(altezza_campo):
        linea_campo = []
        for x in range(larghezza_campo):
            linea_campo.append(" ")
        campo.append(linea_campo)
    return campo

#print(crea_campo())


campo_gioco = crea_campo()

def componi_campo():
    """
    Ritorna il campo da gioco completo con il bordo
    :returns: una lista di liste di stringhe che compongono il campo da gioco completo di bordo
    """
    campo = []
    for lista in campo_gioco:
        campo.append(BORDO_SINISTRO)
        campo.append("".join(lista))
        campo.append(BORDO_DESTRO)
    return(BORDO_ORIZZONTALE + "".join(campo) + BORDO_ORIZZONTALE)
        
print(componi_campo()) 


def posiziona_serpente() -> None:
    global campo_gioco
    campo_gioco[y_testa][x_testa] = TESTA
    return

def vuota_campo():
    global campo_gioco
    campo_gioco[y_testa][x_testa] = " "
    return
    
def controls() -> None:
    """
    Definisce la direzione di marcia del serpente
    """
    global direzione
    while direzione != 'stop':
        if keyboard.is_pressed('w'):
            direzione = 'w'
        if keyboard.is_pressed('a'):
            direzione = 'a'
        if keyboard.is_pressed('s'):
            direzione = 's'
        if keyboard.is_pressed('d'):
            direzione = 'd'
        if keyboard.is_pressed('k'):
            direzione = 'stop'


def game():
    global direzione, y_testa, x_testa
    while direzione != 'stop':
        time.sleep(2)
        posiziona_serpente()
        print(componi_campo())
        vuota_campo()
        if direzione == 'w':
            y_testa -= 1
        if direzione == 'a':
            x_testa -= 1
        if direzione == 's':
            y_testa += 1
        if direzione == 'd':
            x_testa += 1
        if y_testa < 0 or y_testa >= altezza_campo or x_testa < 0 or x_testa >= larghezza_campo:
            direzione = 'stop'


if __name__ == '__main__':
    t1 = Thread(target=game)
    t2 = Thread(target=controls)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
