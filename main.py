# Variabili (valori di default)
larghezza_default = 20
altezza_default = 20

# Costanti globali
TESTA = "O"
CODA = "x"
CORPO = "o"
BORDO_ORIZ_CAMPO = '+' + (larghezza_default * '-') + '+\n'

def main(larghezza, altezza):
    larghezza = input("Inserisci la larghezza del campo?")
    crea_campo()

def crea_campo():
    campo = []
    for y in range(altezza):_
        riga = []
        for x in range(larghezza):
            riga.append(" ")
        campo.append(riga)
    return campo        

