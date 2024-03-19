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
    if max_value == 0:
        return 0, 0
    
    # Trouver les clés correspondant au maximum et au deuxième maximum
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    second_max_keys = [key for key, value in dictionary.items() if value == second_max_value]
    
    max12 = str(max_keys) + " - " + str(second_max_keys)

    return max12

# Exemple d'utilisation
dictionnaire = {"a": 15, "b": 20, "c": 15}
max12 = max_and_second_max(dictionnaire)
print("Max:", max12)

