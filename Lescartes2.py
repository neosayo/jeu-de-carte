class Carte :
    table_couleur = ["Coeur","trèfle","carreau","pique"]
    table_valeur = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","AS"]
    def __init__(self,val,coul) :
        self.valeur = val
        self.couleur = coul
    def affiche(self) :
           print (Carte.table_valeur[self.valeur - 2 ] ,'de',Carte.table_couleur[self.couleur])
            
        
