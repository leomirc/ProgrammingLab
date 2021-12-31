class Automa:

    def __init__(self):
        self.biancheria = None
        self.calzini = None
        self.maglia = None
        self.pantaloni = None
        self.calzatura = None


    def indossa_biancheria(self):
        if self.is_correct_order(0):
            self.biancheria = True
            return 1
        else:
            print("Errore: il capo deve segiure la procedura")
            return 0


    def indossa_calzini(self):
        if self.is_correct_order(1):
            self.calzini = True
            return 1
        else:
            print("Errore: il capo deve segiure la procedura")
            return 0


    def indossa_maglia(self):
        if self.is_correct_order(2):
            self.maglia = True
            return 1
        else:
            print("Errore: il capo deve segiure la procedura")
            return 0


    def indossa_pantaloni(self):
        if self.is_correct_order(3):
            self.pantaloni = True
            return 1
        else:
            print("Errore: il capo deve segiure la procedura")
            return 0


    def indossa_calzatura(self):
        if self.is_correct_order(4):
            self.calzatura = True
            return 1
        else:
            print("Errore: il capo deve segiure la procedura")
            return 0


    def is_correct_order(self, index):
        correct_order = [self.biancheria, self.calzini, self.maglia, self.pantaloni, self.calzatura]
        if all(n for n in correct_order[0:index]) and all(not n for n in correct_order[index+1:len(correct_order)]):
            return True
        else:
            return False






def esegui(automa, capo):
    if capo == "biancheria":
        automa.indossa_biancheria()
    elif capo == "calzini":
        automa.indossa_calzini()
    elif capo == "maglia":
        automa.indossa_maglia()
    elif capo == "pantaloni":
        automa.indossa_pantaloni()
    elif capo == "calzatura":
        automa.indossa_calzatura()
    else:
        print("Capo non valido")


import random
automa = Automa()

capi_vestiario = ["biancheria", "calzini", "maglia", "pantaloni", "calzatura"]

while(not automa.calzatura):
    esegui(automa, random.choice(capi_vestiario))

print("Automa vestito correttamente")
