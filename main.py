"""
jeu de devinnette (a finir)
par Bradley Perreault
groupe 4567
"""
#imports

import random

#variables

borne_minimal : int = 0 # nombre minimum choisi par l'ordi
borne_maximal : int = 1000 # nombre maximum choisi par l'ordi
nombre_essaie : int = 0 # nombre d'essaie du joueur
nombre_choisi : int = random.randint(borne_minimal, borne_maximal) # nombre choisi par l'ordi
playing : bool = True # indicateur si le jeu est en cours

#functions

def verifier_nombre(nombre : int) -> str:
    """
    Vérifie si le nombre choisi par le joueur est correct trop petit ou trop grand.
    """
    global nombre_essaie
    nombre_essaie += 1

    if nombre < nombre_choisi:
        return f"Mauvais choix, le nombre est plus grand que {nombre}."
        
    elif nombre > nombre_choisi:
        return f"Mauvais choix, le nombre est plus petit que {nombre}."
        
    else:
        return f"Félicitations! Vous avez trouvé le bon nombre en {nombre_essaie} essais."

#main loop

while playing:
    try:
        nombre_joueur : int = int(input(f"Devinez le nombre entre {borne_minimal} et {borne_maximal}: "))
        print(verifier_nombre(nombre_joueur))

        if nombre_joueur == nombre_choisi:
            playing = False

    except ValueError:
        print("Veuillez entrer un nombre valide.")


