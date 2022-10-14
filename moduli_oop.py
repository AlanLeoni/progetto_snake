##
## Modulo campo da gioco
##

from progetto_snake.moduli import DIR_EST


class Campo:
    
    def __init__(self, nr_c: int, nr_r: int):
        self.c = nr_c
        self.r = nr_r
        self.campo = [[' ' for x in range(self.c)] for y in range(self.r)]
        
    def larghezza(self):
        return self.c
    
    def altezza(self):
        return self.r
    
    def cella(self, c: int, r: int):
        return self.campo[r][c]
    
    def svuota(self):
        self.campo = [[' ' for x in range(self.c)] for y in range(self.r)]
        
    def imposta_cella(self, c: int, r: int, valore: str):
        self.campo[r][c] = valore
 
class Snake():
    
    TESTA = 'O'
    CORPO = 'x'
    CODA = 'o'
    
    DIR_NORD = 'N'
    DIR_SUD = 'S'
    DIR_EST = 'E'
    DIR_OVEST = 'O'
    
    def __init__(self, campo: Campo, lunghezza_corpo: int = 1, r_i: int = 0, c_i: int = 0, d_i: str = 'E'):
        self.l = lunghezza_corpo
        self.r = r_i
        self.c = c_i
        self.d = d_i
        self.campo = campo
        
    def un_passo(self):
        if self.d == Snake.DIR_EST:
            self.c += 1
        elif self.d == Snake.DIR_OVEST:
            self.c -= 1
        elif self.d == Snake.DIR_NORD:
            self.r -= 1
        elif self.d == Snake.DIR_SUD:
            self.r += 1
            
    def cambia_direzione(self):
        pass