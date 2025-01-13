#Exercice 3 

def calculator():
    print("Bienvenue dans la calculatrice !")
    print("Options disponibles :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Modulo")
    print("7. Quitter")

    while True:
        choix = input("Entrez votre choix (1-7) : ")
        if choix == "7":
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break
        elif choix not in ["1", "2", "3", "4", "5", "6"]:
            print("Choix invalide. Veuillez entrer un chiffre entre 1 et 7.")
            continue

        num1 = input("Entrez le premier nombre : ")
        num2 = input("Entrez le second nombre : ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Erreur : Vous devez entrer des nombres valides.")
            continue

        if choix == "1":
            result = num1 + num2
            print(f"Résultat de l'addition : {result}")
        elif choix == "2":
            result = num1 - num2
            print(f"Résultat de la soustraction : {result}")
        elif choix == "3":
            result = num1 * num2
            print(f"Résultat de la multiplication : {result}")
        elif choix == "4":
            if num2 == 0:
                print("Erreur : Division par zéro impossible.")
            else:
                result = num1 / num2
                print(f"Résultat de la division : {result}")
        elif choix == "5":
            result = num1 ** num2
            print(f"Résultat de la puissance : {result}")
        elif choix == "6":
            if num2 == 0:
                print("Erreur : Modulo par zéro impossible.")
            else:
                result = num1 % num2
                print(f"Résultat du modulo : {result}")

def advanced_calculator():
    print("Options avancées :")
    print("1. Calculer la racine carrée")
    print("2. Calculer le carré")
    print("3. Retour au menu principal")
    
    while True:
        choix = input("Entrez votre choix (1-3) : ")
        if choix == "3":
            print("Retour au menu principal.")
            break
        elif choix not in ["1", "2"]:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            continue
        
        num = input("Entrez un nombre : ")
        
        try:
            num = float(num)
        except ValueError:
            print("Erreur : Vous devez entrer un nombre valide.")
            continue

        if choix == "1":
            if num < 0:
                print("Erreur : Impossible de calculer la racine carrée d'un nombre négatif.")
            else:
                result = num ** 0.5
                print(f"Résultat de la racine carrée : {result}")
        elif choix == "2":
            result = num ** 2
            print(f"Résultat du carré : {result}")

def main():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Calculatrice de base")
        print("2. Calculatrice avancée")
        print("3. Quitter")
        
        choix = input("Faites un choix : ")
        if choix == "1":
            calculator()
        elif choix == "2":
            advanced_calculator()
        elif choix == "3":
            print("Merci d'avoir utilisé le programme. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

main()

