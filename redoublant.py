import sqlite3

def afficher_redoublants():
    # Nom de la base de données et de la table
    db_name = "DB/primatips.sqlite"
    table_name = "primatips_table"

    # Connexion à la base de données
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # Requête pour trouver les enregistrements avec des valeurs en double
    query = f"""
    SELECT ID,PAYS, TEAMS, BET1, BETX, BET2, RESULTAT, COUNT(*)
    FROM {table_name}
    GROUP BY PAYS, TEAMS, BET1, BETX, BET2, RESULTAT
    HAVING COUNT(*) > 1;
    """

    # Exécution de la requête
    c.execute(query)
    redoublants = c.fetchall()

    # Fermeture de la connexion
    conn.close()

    # Affichage des doublons
    if redoublants:
        print("Voici les enregistrements avec des valeurs en double :")
        for redoublant in redoublants:
            print(redoublant)
    else:
        print("Aucun enregistrement avec des valeurs en double n'a été trouvé.")

# Appel de la fonction pour afficher les doublons
afficher_redoublants()
