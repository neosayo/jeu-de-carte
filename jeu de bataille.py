from jeu_cartes import jeu_cartes
manche = 0
vospoints = 0
pointsordi = 0
bonus = 0
score_ordi = 0
score_joueur = 0
while (manche<26):
    input ("Taper Sur Entrer")
    mon_jeu = jeu_cartes()
    #mon_jeu.melanger()
    carte_joueur = mon_jeu.tirer()
    print("Le Joueur Tire")
    carte_joueur.affiche()
    carte_ordi = mon_jeu.tirer()
    print("Ordi Tire")
    carte_ordi.affiche()
    if carte_joueur.valeur > carte_ordi.valeur :
        print ("Le Joueur Gagne")
        vospoints = vospoints + 1
    if carte_joueur.valeur == carte_ordi.valeur :
        print("bonus",bonus +1)
        bonus = bonus + 1
    if joueur.valeur < ordi.valeur :
            score_joueur += (bonus+1)
            bonus = 0
            print ("joueur gagne")
    else :
        print ("Ordi gagne")
        pointsordi = pointsordi + 1
        bonus += 1
        print ("bataille")
        print("score_ordi",score_ordi)
        print("score_joueur",score_joueur)
        manche=manche+1
        
        
        
    
    
    
    
    
    



    
    
    



