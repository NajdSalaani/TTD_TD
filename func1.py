# Exercice 1.1

# Fonction qui renvoie les 3 plus grandes valeurs d'une liste d'entiers

def max_list_int(list_int):
    # Cas 1 : Si la liste est vide, on retourne 0, sinon (-9) le max avec la fonction python qui ets quand même à vérifier 
    if list_int == []:
        return 0
    else:
        return max(list_int)

    