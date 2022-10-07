def test_campo_cancella ():
    campo_crea (10,10)
    campo_cancella()
    assert campo_cella (1,1) == ‘ ‘ 

def test_campo_crea1 ():
    campo_crea (10,10)
    assert campo_cella (0,0) ==  ‘ ‘ 

def test_campo_crea2 ():
    campo_crea (20,10)
    assert campo_cella(10,5) == ' '

def test_campo_altezza_larghezza ():
    campo_crea (10,20)
    assert campo_larghezza()
 == 10
    assert campo_altezza() ==  20
    
def test_campo_imposta_cella ():
    campo_imposta_cella(20,10, '@')
    assert campo_cella(20,10) == '@'


test_campo_cancella ()
test_campo_crea1 ()
test_campo_crea2 ()
test_campo_altezza_larghezza ()
test_campo_imposta_cella ()