# Exercice 1.1

# Fonction qui renvoie les 3 plus grandes valeurs d'une liste d'entiers

def max_list_int(list_int):
    # Cas 1 : Si la liste est vide, on retourne 0, sinon (-9) le max avec la fonction python qui ets quand même à vérifier 
    if list_int == []:
        return 0
    else:
        max_values = []
        for _ in range(3):
            if list_int:
                # Trouver la plus grande valeur actuelle
                max_val = max(list_int)
                max_values.append(max_val)
                list_int.remove(max_val)
        return max_values

   
# Exercice 1.2

# nombre premier 

def est_premier(n):
        return True 