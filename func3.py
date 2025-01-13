#Exercice 3 


# Ajout de fonctions intermédiaires 
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b

def puissance(base, exposant):
    if base < 0 and exposant < 1:
        return "Erreur : Impossible de calculer une puissance fractionnaire pour un nombre négatif."
    return base ** exposant


def modulo(a, b):
    if b == 0:
        raise ValueError("Modulo par zéro impossible.")
    return a % b
    



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

        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le second nombre : "))

            if choix == "1":
                print(f"Résultat de l'addition : {addition(num1, num2)}")
            elif choix == "2":
                print(f"Résultat de la soustraction : {soustraction(num1, num2)}")
            elif choix == "3":
                print(f"Résultat de la multiplication : {multiplication(num1, num2)}")
            elif choix == "4":
                print(f"Résultat de la division : {division(num1, num2)}")
            elif choix == "5":
                print(f"Résultat de la puissance : {puissance(num1, num2)}")
            elif choix == "6":
                print(f"Résultat du modulo : {modulo(num1, num2)}")
        except ValueError as e:
            print(f"Erreur : {e}")


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
            result = puissance(num,0.5)
            if isinstance(result, str):  # Vérifie si c'est une erreur
                print(result)
            else:
                print(f"Résultat de la racine carrée : {result}")
        elif choix == "2":
            result = puissance(num,2)
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

