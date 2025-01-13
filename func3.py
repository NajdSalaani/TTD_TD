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
    
# Affichage du menu principal
def afficher_menu_principal():
    print("\n=== Menu Principal ===")
    print("1. Calculatrice de base")
    print("2. Calculatrice avancée")
    print("3. Quitter")

# Affichage du menu de la calculatrice de base
def afficher_menu_calculatrice():
    print("Bienvenue dans la calculatrice !")
    print("Options disponibles :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Puissance")
    print("6. Modulo")
    print("7. Quitter")

# Affichage du menu de la calculatrice avancée
def afficher_menu_avance():
    print("Options avancées :")
    print("1. Calculer la racine carrée")
    print("2. Calculer le carré")
    print("3. Retour au menu principal")

# Valider le choix de l'utilisateur pour les menus
def valider_choix(choix, options_valides):
    if choix not in options_valides:
        print(f"Choix invalide. Veuillez entrer {', '.join(options_valides)}.")
        return False
    return True

# Demander un nombre à l'utilisateur et gérer les erreurs
def demander_nombre():
    try:
        return float(input("Entrez un nombre : "))
    except ValueError:
        print("Erreur : Vous devez entrer un nombre valide.")
        return None

# Effectuer l'opération de calcul en fonction du choix de l'utilisateur
def effectuer_calcul(choix, num1, num2):
    if choix == "1":
        return addition(num1, num2)
    elif choix == "2":
        return soustraction(num1, num2)
    elif choix == "3":
        return multiplication(num1, num2)
    elif choix == "4":
        return division(num1, num2)
    elif choix == "5":
        return puissance(num1, num2)
    elif choix == "6":
        return modulo(num1, num2)


def calculator():
    afficher_menu_calculatrice()
    while True:
        choix = input("Entrez votre choix (1-7) : ")
        if choix == "7":
            print("Merci d'avoir utilisé la calculatrice. Au revoir !")
            break

        if not valider_choix(choix, ["1", "2", "3", "4", "5", "6"]):
            continue

        num1 = demander_nombre()
        if num1 is None:
            continue

        num2 = demander_nombre()
        if num2 is None:
            continue

        try:
            result = effectuer_calcul(choix, num1, num2)
            print(f"Résultat : {result}")
        except ValueError as e:
            print(f"Erreur : {e}")

# Fonction pour la calculatrice avancée
def advanced_calculator():
    afficher_menu_avance()
    while True:
        choix = input("Entrez votre choix (1-3) : ")
        if choix == "3":
            print("Retour au menu principal.")
            break

        if not valider_choix(choix, ["1", "2"]):
            continue

        num = demander_nombre()
        if num is None:
            continue

        if choix == "1":
            result = puissance(num, 0.5)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Résultat de la racine carrée : {result}")
        elif choix == "2":
            result = puissance(num, 2)
            print(f"Résultat du carré : {result}")

# Fonction principale qui gère l'entrée de l'utilisateur
def main():
    while True:
        afficher_menu_principal()
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

