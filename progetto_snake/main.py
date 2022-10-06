"""
Gioco Snake
Le funzioni presenti in questo file permettono il funzionamento del gioco dello snake.
In modo particolare il gioco consiste in un serpente che si muove all'interno di un rettangolo diventando sempre più lungo
"""
from types import NoneType
import keyboard

# Variabili e costanti del campo da gioco
larghezza_campo = 20
altezza_campo = 10
BORDO_ORIZZONTALE = "+" + (larghezza_campo * "-") + '+\n'
BORDO_SINISTRO = "|"
BORDO_DESTRO = "|+\n"

# Variabili e costanti del serprente
pezzi_corpo = 0
x_testa = 0
y_testa = 0
TESTA = "O"
CORPO = "o"
CODA = "x"
def crea_campo() -> list[str]:
    """
    Ritorna l'area del campo da gioco definito nelle costanti
    :returns: una lista di stringhe che compongono l'area di gioco
    """
    campo = []
    for y in range(altezza_campo):
        linea_campo = [BORDO_SINISTRO]
        for x in range(larghezza_campo):
            linea_campo.append(" ")
        linea_campo.append(BORDO_DESTRO)
        campo.append(linea_campo)
    return campo

# test: proviamo a printare la lista
## print(crea_campo())

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