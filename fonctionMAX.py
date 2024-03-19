def max_of_three_values(dictionary):
    # Récupérer les clés et les valeurs du dictionnaire
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    
    # Trier les valeurs dans l'ordre décroissant
    sorted_values = sorted(values, reverse=True)
    
    # Trouver le maximum
    max_value = sorted_values[0]
    
    # Si toutes les valeurs sont égales à zéro, retourner 0
    if max_value == 0:
        return 0
    
    # Vérifier s'il y a des valeurs égales
    if len(set(values)) == 1:
        return keys
    
    # Trouver les clés correspondant au maximum
    max_keys = [key for key, value in dictionary.items() if value == max_value]
    
    return max_keys

# dict_max_1
# dict_max_1 = {'1': 3, 'X': 3, '2': 3}

# dict_max_1
# dict_max_1 = {'1': countDic["count_1_1"], 'X': countDic["count_1_X"], '2': countDic["count_1_2"]}

# Utilisation de la fonction MAX
# max_1 = max_of_three_values(dict_max_1)



# Affichage du résultat
# print("Résultat:", max_1)
