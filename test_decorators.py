def funzione1(fn):
    print("sono io!")
    fn()
    print("si, sono proprio io!")

@funzione1
def funzione2():
    print("Cesare Angelo Cattaneo")
    
funzione2()
