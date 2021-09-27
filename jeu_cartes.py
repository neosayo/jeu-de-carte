from Lescartes2 import Carte


    
class jeu_cartes :
    def __init__(self) :
        self.Cartes = []
        for val in range (2,15) :
            for coul in range (0,4) :
                self.Cartes.append(Carte(val,coul))
    def melanger(self):
        import random
        random.shuffle(self.Cartes)
    def tirer(self):
        return self.Cartes.pop(0)
    
    
    
    
    
                


