import math
import random

#Variables
difficulte = ""
rejouer = True

# Constantes
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_VIES = 0
DIFFICULTIES = {
    1: "Facile",
    2: "Moyen",
    3: "Difficile",
    4: "Expert"
}

# Fonctions
def choisir_difficulte():
    global NOMBRE_MIN
    global NOMBRE_MAX
    global NB_VIES

    print("Choisissez une difficulté:")
    for key, value in DIFFICULTIES.items():
        print(f"[{key}] {value}")
    print("------------------")

    difficulte = input("Entrez le numéro de la difficulté: ")

    try:
        difficulte_int = int(difficulte)
    except ValueError:
        print("Vous n'avez pas entré une difficulté valide. Réessayez!")
        return choisir_difficulte()
    except TypeError:
        print("Vous n'avez pas entré une difficulté valide. Réessayez!")
        return choisir_difficulte()
    else:
        if difficulte_int < 1 or difficulte_int > 4:
            print("Vous n'avez pas entré une difficulté valide. Réessayez!")
            return choisir_difficulte()
        elif difficulte_int == 1:
            NOMBRE_MIN = 1
            NOMBRE_MAX = 10
            NB_VIES = 5
        elif difficulte_int == 2:
            NOMBRE_MIN = 1
            NOMBRE_MAX = 100
            NB_VIES = 10
        elif difficulte_int == 3:
            NOMBRE_MIN = 1
            NOMBRE_MAX = 100
            NB_VIES = 5
        elif difficulte_int == 4:
            NOMBRE_MIN = 1
            NOMBRE_MAX = 1000
            NB_VIES = 10

    print(f"Vous avez choisi la difficulté: {DIFFICULTIES[difficulte_int]}")
    print(f"Vous avez {NB_VIES} vies et vous devez trouver un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX}")
    print("Bonne chance!")
    print()


def demander_nombre(nombre_min, nombre_max):
    nombre_str = input("Entrez un nombre entre " + str(nombre_min) + " et " + str(nombre_max) + ": ")
    try:
        nombre_int = int(nombre_str)
    except ValueError:
        print("Vous n'avez pas entré un nombre. Réessayez!")
        return demander_nombre(nombre_min, nombre_max)
    except TypeError:
        print(f"Vous devez rentrer un nombre entre {nombre_min} et {nombre_max}. Réessayez!")
        return demander_nombre(nombre_min, nombre_max)

    else:
        if nombre_int < nombre_min or nombre_int > nombre_max or nombre_int == 0:
            print(f"Vous n'avez pas entré un nombre entre {nombre_min} et {nombre_max}. Réessayez!")
            return demander_nombre(nombre_min, nombre_max)
    return nombre_int


# Programme principal
print("############################################")
print("# Bienvenue dans le jeu du nombre magique! #")
print("############################################")

while rejouer:
    choisir_difficulte()
    nb_magique = random.randint(NOMBRE_MIN, NOMBRE_MAX)

    while NB_VIES > 0:
        response = demander_nombre(NOMBRE_MIN,NOMBRE_MAX)
        taille = ""

        if response == nb_magique:
            print("Bravo! Vous avez trouvé le nombre magique")
            break

        if int(response) > nb_magique:
            NB_VIES -= 1
            taille = "petit"

        elif int(response) < nb_magique:
            NB_VIES -= 1
            taille = "grand"

        if NB_VIES == 0:
            print(f"Vous avez perdu! Le nombre magique était {nb_magique}")
            break

        print("Le nombre magique est plus " + taille)
        print("Il vous reste " + str(NB_VIES) + " vies")

    rejouer = input("Voulez-vous rejouer? (o/n): ")
    if rejouer == "o":
        rejouer = True
    else:
        rejouer = False
        print("Merci d'avoir joué!")