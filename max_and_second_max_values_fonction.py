def max_and_second_max_keys(dictionary):
    # Récupérer les clés et les valeurs du dictionnaire
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    
    # Vérifier si toutes les valeurs sont égales à zéro
    if all(value == 0 for value in values):
        return 0, 0
    
    # Trier les valeurs dans l'ordre décroissant
    sorted_values = sorted(values, reverse=True)
    
    # Trouver le maximum
    max_value = sorted_values[0]
    
    # Trouver les clés correspondant au maximum
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    
    # S'il y a plus d'une clé correspondant au maximum, retourner uniquement la première
    if len(max_keys) > 1:
        max_keys = [max_keys[0]]
    
    # Trouver le deuxième maximum
    if len(sorted_values) > 1:
        second_max_value = sorted_values[1]
        # Trouver les clés correspondant au deuxième maximum
        second_max_keys = [key for key, value in dictionary.items() if value == second_max_value]
    else:
        second_max_keys = []
    
    return max_keys, second_max_keys

# Exemple d'utilisation
dictionary = {'1': 1, 'X': 0, '2': 0}
max_keys, second_max_keys = max_and_second_max_keys(dictionary)
print("Clé correspondant au maximum :", max_keys)
print("Clé correspondant au deuxième maximum :", second_max_keys)
