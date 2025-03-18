def convertir(valeur, conversion_type):
    if conversion_type == "cm_en_inch":
        return valeur * 0.394, "inch"
    else:
        return valeur * 2.54, "cm"

choix = ""
while not choix == "exit":
    print("Convertir: 1) cm en inch ou 2) inch en cm (si vous voulez quitter le programme taper 'exit')")
    choix = input("Choisissez la conversion : '1' ou '2' \n--> ").strip().lower()
    if choix == "exit":
        break

    elif choix in ["1", "2"]:
        conversion_type= "cm_en_inch" if choix == "1" else "inch_en_cm"
        unite = "cm" if choix == "1" else "inch"
        valeur_str = ""
        while valeur_str != "exit":
            valeur_str = input("Veuillez donner votre valeur en " + (unite) +"-->").strip()
            try:
                valeur_float= float(valeur_str)
                valeur_convertie, unite_finale= convertir(valeur_float, conversion_type)
                print(f"{valeur_float} {unite} donne {valeur_convertie:.2f} {unite_finale}")
            except ValueError:
                print("Veuillez choisir un nombre, et n'oublier pas de remplacer la virgule(,) par un point(.)")
            else:
                print("Voulez-vous retourner au menu ?")
                valeur_str = input("Si oui, taper 'exit'-->")
    else:
        print(" Choix Invalide ! Vous devez choisir la conversion:\n-'1'--> des centimètres en pouces\n-'2'--> des pouces en centimètres\n -Ou sortir en tapant 'exit' ")
        continue

print()
print("Fin du programme !!!")