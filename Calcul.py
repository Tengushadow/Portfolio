import os
import random
NB_MAX2 = 50
NB_MAX3 = 100
NB_MAX = 10
NB_MIN = 1
NB_QUESTION = 4

FACILE = (NB_MIN, NB_MAX)
INTERMEDIAIRE = (NB_MAX, NB_MAX2)
DIFFICILE = (NB_MAX2, NB_MAX3)

def poser_quest():
    niveau = {"nv1": FACILE,"nv2": INTERMEDIAIRE,"nv3": DIFFICILE}
    niveau_str = input("Choisissez un niveau de difficulté: nv1, nv2, nv3-->")
    if niveau_str in niveau:
        a, b = niveau[niveau_str]
        a = random.randint(a, b)
        b = random.randint(a, b)
        return a, b
    else:
        print("Niveau de difficulté invalide")
        return FACILE


def reponse_utili():
    a_val = random.randint(a, b)
    b_val = random.randint(a, b)
    o = random.randint(0, 1)
    calcul = a_val + b_val
    signes_str = "+"
    reponse_str = ""
    if o == 1:
        signes_str = "*"
        calcul = a_val * b_val
    while True:
       try:
            reponse_str = input(f"Calculer: {a_val} {signes_str} {b_val} = ")
            reponse_int = int(reponse_str)
       except:
            print("Donner un nombre entier")
            continue
       if reponse_int == calcul:
           return True
       return False


a, b = poser_quest()
nb_points = 0
for i in range(0, NB_QUESTION):
    print(f"Vous avez {nb_points}")
    print(f"Question {i + 1} sur {NB_QUESTION}")
    calcul = reponse_utili()
    if calcul :
        print("Réponse correcte !!!")
        nb_points += 1

    else:
        print("Réponse incorrecte")

moyenne = int(NB_QUESTION/2)
if nb_points == NB_QUESTION:
    print(f"Bravo, vous avez {nb_points} / {NB_QUESTION}, excellent!!!!")
elif nb_points == 0 :
    print("Réviser vos math")
elif nb_points > moyenne :
    print("Pas mal")
elif nb_points < moyenne:
    print("Peut mieux faire")






