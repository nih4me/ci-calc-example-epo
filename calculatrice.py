from functions import *

# Boucle principale
while True:
    print("----- Calculatrice Console -----")
    num1 = float(input("Saisir le premier nombre : "))
    num2 = float(input("Saisir le deuxième nombre : "))

    print("Opérations disponibles :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Saisir le numéro de l'opération choisie : ")

    if choix == "1":
        resultat = addition(num1, num2)
        print("Résultat : ", resultat)
    elif choix == "2":
        resultat = soustraction(num1, num2)
        print("Résultat : ", resultat)
    elif choix == "3":
        resultat = multiplication(num1, num2)
        print("Résultat : ", resultat)
    elif choix == "4":
        resultat = division(num1, num2)
        if resultat is not None:
            print("Résultat : ", resultat)
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez choisir une opération valide.")

    print("\n")
