"""
jeu de devinnette 
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
    if nombre < borne_minimal or nombre > borne_maximal:
        return f"Le nombre doit être entre {borne_minimal} et {borne_maximal}."
    if nombre < nombre_choisi:
        return f"Mauvais choix, le nombre est plus grand que {nombre}."
        
    elif nombre > nombre_choisi:
        return f"Mauvais choix, le nombre est plus petit que {nombre}."
        
    else:
        return f"Félicitations! Vous avez trouvé le bon nombre en {nombre_essaie} essais."

def changer_borne():
    """
    Change la borne minimale et maximale grace à l'input du joueur.
    """
    global borne_minimal, borne_maximal
    borne_minimal = int(input("Entrez la borne minimale: "))
    borne_maximal = int(input("Entrez la borne maximale: "))
    if borne_minimal >= borne_maximal:
        print("La borne minimale doit être inférieure à la borne maximale. Veuillez réessayer.")
        changer_borne()
    

#main loop
changer_borne()
while playing:
    try:
        nombre_joueur : int = int(input(f"Devinez le nombre entre {borne_minimal} et {borne_maximal}: "))
        print(verifier_nombre(nombre_joueur))

        if nombre_joueur == nombre_choisi:
            veut_jouer_encore = input("Voulez-vous jouer encore? (o/n): ").lower()
            if veut_jouer_encore == "o":
                nombre_choisi = random.randint(borne_minimal, borne_maximal)
                nombre_essaie = 0
                changer_borne()
            else:
                print("Merci et au revoir…")
                playing = False

    except ValueError:
        print("Veuillez entrer un nombre valide.")
