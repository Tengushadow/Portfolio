import os
import time
import random


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def afficher_sequence(seq,nb):
    for i in range (nb):
        seq += str(random.randint(0,9))
    return seq


nb_pt = 0
sequence = ""
sequence = afficher_sequence(sequence,1)
while True:
#On affiche le nombre de points au départ
    print(f"Vous avez {nb_pt} points")
#On attend 2 secondes avant d'effacer cette phrase
    time.sleep(2)
    clear_screen()
#Séquence à retenir
    print("Retenez la séquence :")
    time.sleep(1)
    clear_screen()


    print(sequence)

#On efface la séquence après 3 secondes
    time.sleep(3)
    clear_screen()

    reponse = input("Quel est la séquence : ")
    if reponse == sequence:
        print("Bonne réponse !")
        nb_pt += 1
        time.sleep(1)
        clear_screen()

        sequence = afficher_sequence(sequence, 1)
    else:
        print(f"Mauvaise réponse. La séquence était : {sequence}")
        print(f"Votre score finale est {nb_pt}")
    #On sort de la boucle car la réponse est fausse
        break



