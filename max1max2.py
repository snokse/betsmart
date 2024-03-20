def max_and_second_max(dictionary):
    # Récupérer les clés et les valeurs du dictionnaire
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    
    # Trier les valeurs dans l'ordre décroissant
    sorted_values = sorted(values, reverse=True)
    
    # Trouver le maximum et le deuxième maximum
    max_value = sorted_values[0]
    second_max_value = sorted_values[1] if len(sorted_values) > 1 else None
    
    # Si toutes les valeurs sont égales à zéro, retourner 0 pour les deux
    if max_value == 0 and (second_max_value is None or second_max_value == 0):
        return 0, 0
    
    # Trouver les clés correspondant au maximum et au deuxième maximum
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    second_max_keys = [key for key, value in dictionary.items() if value == second_max_value]
    
    # Si la deuxième plus grande valeur est nulle, retourner 0 pour second_max_keys
    if second_max_value == 0:
        return max_keys, 0
    
    # Si les valeurs de maximum sont égales, retourner 0 pour second_max_keys
    if max_value == second_max_value:
        return max_keys, 0
    
    return max_keys, second_max_keys

# Exemple d'utilisation
# dictionnaire = {"1": 0, "X": 0, "2": 1}
# max12 = max_and_second_max(dictionnaire)
# print("Max:", max12)
