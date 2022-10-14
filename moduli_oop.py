##
## Modulo campo da gioco
##

class campo:
    
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
    
    