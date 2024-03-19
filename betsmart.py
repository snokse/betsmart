import sqlite3
import tkinter as tk
from tkinter import ttk
import fonctionMAX
import tkinter.font as tkFont


# from tkinter.ttk import Treeview
# from tkinter.ttk import Label
# "https://drive.google.com/file/d/1vCAOqLPDK4p1483FndCnOqBPuOzbmOOd/view?usp=sharing"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def create_database():
    global db_name, table_name
    db_name = "DB/betsmart_db.db"
    table_name = "betsmart_table"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #conn.commit()
    conn.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def search_BET():
    global countALL, max_1, max_X, max_2, max_1X, max_12, max_X2, max_1X2, max_TIP, max_TIP_1, max_TIP_X, max_TIP_2  # Déclarer count1 comme une variable globale
    search_BET1 = search_entry_BET1.get()
    search_BETX = search_entry_BETX.get()
    search_BET2 = search_entry_BET2.get()
    conn = sqlite3.connect(db_name)

    c = conn.cursor()
    cursorCount = conn.cursor()

    # Requête d'affichage 
    query = f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,BUT1,BUT2,RESULTAT,PM,BUT FROM {table_name} WHERE 1=1"
    query_redoublants = f"SELECT TEAMS, BETX, BET2, RESULTAT COUNT(*) AS nombre_redoublants FROM {table_name} GROUP BY TEAMS, BETX, BET2, RESULTAT HAVING COUNT(*) > 1;"

    # Requête pour compter
    queryCount = f"SELECT COUNT(*) FROM {table_name} WHERE 1=1"
    # Requête pour compter 1 
    queryCount_1 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%'"
    queryCount_1_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BET1 LIKE '{search_BET1}%'"
    queryCount_1_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BET1 LIKE '{search_BET1}%'"
    queryCount_1_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BET1 LIKE '{search_BET1}%'"
    # Requête pour compter X
    queryCount_X = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%'"
    queryCount_X_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BETX LIKE '{search_BETX}%'"
    queryCount_X_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BETX LIKE '{search_BETX}%'"
    queryCount_X_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BETX LIKE '{search_BETX}%'"
    # Requête pour compter 2
    queryCount_2 = f"SELECT COUNT(*) FROM {table_name} WHERE BET2 LIKE '{search_BET2}%'"
    queryCount_2_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BET2 LIKE '{search_BET2}%'"
    queryCount_2_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BET2 LIKE '{search_BET2}%'"
    queryCount_2_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BET2 LIKE '{search_BET2}%'"

    # Requête pour compter P/M
    queryCount_1_P = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND PM LIKE 'P'"
    queryCount_1_M = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND PM LIKE 'M'"

    queryCount_X_P = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND PM LIKE 'P'"
    queryCount_X_M = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND PM LIKE 'M'"

    queryCount_2_P = f"SELECT COUNT(*) FROM {table_name} WHERE BET2 LIKE '{search_BET2}%' AND PM LIKE 'P'"
    queryCount_2_M = f"SELECT COUNT(*) FROM {table_name} WHERE BET2 LIKE '{search_BET2}%' AND PM LIKE 'M'"

    # Requête pour compter B/SB
    queryCount_1_B = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BUT LIKE 'B'"
    queryCount_1_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BUT LIKE 'SB'"

    queryCount_X_B = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BUT LIKE 'B'"
    queryCount_X_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BUT LIKE 'SB'"

    queryCount_2_B = f"SELECT COUNT(*) FROM {table_name} WHERE BET2 LIKE '{search_BET2}%' AND BUT LIKE 'B'"
    queryCount_2_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BET2 LIKE '{search_BET2}%' AND BUT LIKE 'SB'"
    
    # Requête pour compter 1X
    queryCount_1X = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%'"
    queryCount_1X_1 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND RESULTAT=1"
    queryCount_1X_X = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND RESULTAT='X'"
    queryCount_1X_2 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND RESULTAT=2"
    # Requête pour compter 1X P/M 
    queryCount_1X_P = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND PM LIKE 'P'"
    queryCount_1X_M = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND PM LIKE 'M'"
    # Requête pour compter 1X B/SB
    queryCount_1X_B = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BUT LIKE 'B'"
    queryCount_1X_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BUT LIKE 'SB'"

    # Requête pour compter 12
    queryCount_12 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%'"
    queryCount_12_1 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=1"
    queryCount_12_X = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT='X'"
    queryCount_12_2 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=2"
    # Requête pour compter 12 P/M 
    queryCount_12_P = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'P'"
    queryCount_12_M = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'M'"
    # Requête pour compter 12 B/SB
    queryCount_12_B = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'B'"
    queryCount_12_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'SB'"

    # Requête pour compter X2
    queryCount_X2 = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%'"
    queryCount_X2_1 = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=1"
    queryCount_X2_X = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT='X'"
    queryCount_X2_2 = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=2"
    # Requête pour compter X2 P/M 
    queryCount_X2_P = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'P'"
    queryCount_X2_M = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'M'"
    # Requête pour compter X2 B/SB
    queryCount_X2_B = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'B'"
    queryCount_X2_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'SB'"

    # Requête pour compter 1X2
    queryCount_1X2 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%'"
    queryCount_1X2_1 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=1"
    queryCount_1X2_X = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT='X'"
    queryCount_1X2_2 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND RESULTAT=2"
    # Requête pour compter 1X P/M 
    queryCount_1X2_P = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'P'"
    queryCount_1X2_M = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND PM LIKE 'M'"
    # Requête pour compter 1X B/SB
    queryCount_1X2_B = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'B'"
    queryCount_1X2_SB = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE '{search_BET1}%' AND BETX LIKE '{search_BETX}%' AND BET2 LIKE '{search_BET2}%' AND BUT LIKE 'SB'"

    parameters = []

    if search_BET1:
        query += " AND BET1 LIKE ?"
        queryCount += " AND BET1 LIKE ?"
        parameters.append(f"{search_BET1}%")

    if search_BETX:
        query += " AND BETX LIKE ?"
        queryCount += " AND BETX LIKE ?"
        parameters.append(f"{search_BETX}%")

    if search_BET2:
        query += " AND BET2 LIKE ?"
        queryCount += " AND BET2 LIKE ?"
        parameters.append(f"{search_BET2}%")

    try:
        c.execute(query, parameters)
        rows = c.fetchall()

        # Exécuter la requête de comptage
        cursorCount.execute(queryCount, parameters)
        count_result = cursorCount.fetchone()


        if count_result:  # Vérifier si count_result n'est pas None
            countALL = count_result[0]  # Mettre à jour count1 si la requête de comptage a retourné des résultats
        else:
            countALL = 0  # Sinon, définir count1 à zéro

        
        # Exécuter la requête pour compter 1
        if search_BET1:
            cursorCount.execute(queryCount_1)
            countDic["count_1"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_1_1)
            countDic["count_1_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_X)
            countDic["count_1_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_2)
            countDic["count_1_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 1 PM
            cursorCount.execute(queryCount_1_P)
            countDic["count_1_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_M)
            countDic["count_1_M"] = cursorCount.fetchone()[0]

            # Exécuter la requête pour compter 1 BUT
            cursorCount.execute(queryCount_1_B)
            countDic["count_1_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_SB)
            countDic["count_1_SB"] = cursorCount.fetchone()[0]
        else:
            countDic["count_1"] = 0
            countDic["count_1_1"] = 0
            countDic["count_1_X"] = 0
            countDic["count_1_2"] = 0
            countDic["count_1_P"] = 0
            countDic["count_1_M"] = 0
            countDic["count_1_B"] = 0
            countDic["count_1_SB"] = 0

        if search_BETX:
        # Exécuter la requête pour compter X
            cursorCount.execute(queryCount_X)
            countDic["count_X"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_X_1)
            countDic["count_X_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_X)
            countDic["count_X_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_2)
            countDic["count_X_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter X PM
            cursorCount.execute(queryCount_X_P)
            countDic["count_X_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_M)
            countDic["count_X_M"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter X BUT
            cursorCount.execute(queryCount_X_B)
            countDic["count_X_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_SB)
            countDic["count_X_SB"] = cursorCount.fetchone()[0]

        else:
            countDic["count_X"] = 0
            countDic["count_X_1"] = 0
            countDic["count_X_X"] = 0
            countDic["count_X_2"] = 0
            countDic["count_X_P"] = 0
            countDic["count_X_M"] = 0
            countDic["count_X_B"] = 0
            countDic["count_X_SB"] = 0

        
        # Exécuter la requête pour compter 2
        if search_BET2:
            cursorCount.execute(queryCount_2)
            countDic["count_2"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_2_1)
            countDic["count_2_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_X)
            countDic["count_2_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_2)
            countDic["count_2_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 2 PM
            cursorCount.execute(queryCount_2_P)
            countDic["count_2_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_M)
            countDic["count_2_M"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 2 BUT
            cursorCount.execute(queryCount_2_B)
            countDic["count_2_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_SB)
            countDic["count_2_SB"] = cursorCount.fetchone()[0]

        else:
            countDic["count_2"] = 0
            countDic["count_2_1"] = 0
            countDic["count_2_X"] = 0
            countDic["count_2_2"] = 0
            countDic["count_2_P"] = 0
            countDic["count_2_M"] = 0
            countDic["count_2_B"] = 0
            countDic["count_2_SB"] = 0

        # Exécuter la requête pour compter 1X
        if search_BET1 and search_BETX:
            cursorCount.execute(queryCount_1X)
            countDic["count_1X"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_1X_1)
            countDic["count_1X_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X_X)
            countDic["count_1X_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X_2)
            countDic["count_1X_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 1X PM
            cursorCount.execute(queryCount_1X_P)
            countDic["count_1X_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X_M)
            countDic["count_1X_M"] = cursorCount.fetchone()[0]

            # Exécuter la requête pour compter 1X BUT
            cursorCount.execute(queryCount_1X_B)
            countDic["count_1X_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X_SB)
            countDic["count_1X_SB"] = cursorCount.fetchone()[0]
        else:
            countDic["count_1X"] = 0
            countDic["count_1X_1"] = 0
            countDic["count_1X_X"] = 0
            countDic["count_1X_2"] = 0
            countDic["count_1X_P"] = 0
            countDic["count_1X_M"] = 0
            countDic["count_1X_B"] = 0
            countDic["count_1X_SB"] = 0

        # Exécuter la requête pour compter 12
        if search_BET1 and search_BET2:
            cursorCount.execute(queryCount_12)
            countDic["count_12"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_12_1)
            countDic["count_12_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_12_X)
            countDic["count_12_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_12_2)
            countDic["count_12_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 12 PM
            cursorCount.execute(queryCount_12_P)
            countDic["count_12_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_12_M)
            countDic["count_12_M"] = cursorCount.fetchone()[0]

            # Exécuter la requête pour compter 12 BUT
            cursorCount.execute(queryCount_12_B)
            countDic["count_12_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_12_SB)
            countDic["count_12_SB"] = cursorCount.fetchone()[0]
        else:
            countDic["count_12"] = 0
            countDic["count_12_1"] = 0
            countDic["count_12_X"] = 0
            countDic["count_12_2"] = 0
            countDic["count_12_P"] = 0
            countDic["count_12_M"] = 0
            countDic["count_12_B"] = 0
            countDic["count_12_SB"] = 0

        # Exécuter la requête pour compter X2
        if search_BETX and search_BET2:
            cursorCount.execute(queryCount_X2)
            countDic["count_X2"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_X2_1)
            countDic["count_X2_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X2_X)
            countDic["count_X2_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X2_2)
            countDic["count_X2_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 12 PM
            cursorCount.execute(queryCount_X2_P)
            countDic["count_X2_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X2_M)
            countDic["count_X2_M"] = cursorCount.fetchone()[0]

            # Exécuter la requête pour compter 12 BUT
            cursorCount.execute(queryCount_X2_B)
            countDic["count_X2_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X2_SB)
            countDic["count_X2_SB"] = cursorCount.fetchone()[0]
        else:
            countDic["count_X2"] = 0
            countDic["count_X2_1"] = 0
            countDic["count_X2_X"] = 0
            countDic["count_X2_2"] = 0
            countDic["count_X2_P"] = 0
            countDic["count_X2_M"] = 0
            countDic["count_X2_B"] = 0
            countDic["count_X2_SB"] = 0

        # Exécuter la requête pour compter 1X2
        if search_BET1 and search_BETX and search_BET2:
            cursorCount.execute(queryCount_1X2)
            countDic["count_1X2"] = cursorCount.fetchone()[0]

            cursorCount.execute(queryCount_1X2_1)
            countDic["count_1X2_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X2_X)
            countDic["count_1X2_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X2_2)
            countDic["count_1X2_2"] = cursorCount.fetchone()[0]
            # Exécuter la requête pour compter 1X PM
            cursorCount.execute(queryCount_1X2_P)
            countDic["count_1X2_P"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X2_M)
            countDic["count_1X2_M"] = cursorCount.fetchone()[0]

            # Exécuter la requête pour compter 1X BUT
            cursorCount.execute(queryCount_1X2_B)
            countDic["count_1X2_B"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1X2_SB)
            countDic["count_1X2_SB"] = cursorCount.fetchone()[0]
        else:
            countDic["count_1X2"] = 0
            countDic["count_1X2_1"] = 0
            countDic["count_1X2_X"] = 0
            countDic["count_1X2_2"] = 0
            countDic["count_1X2_P"] = 0
            countDic["count_1X2_M"] = 0
            countDic["count_1X2_B"] = 0
            countDic["count_1X2_SB"] = 0

        # Mettre à jour les textes des labels après avoir obtenu count1
        conn.commit()  # Valider les modifications dans la base de données
        update_treeview(rows)
        conn.close()

        # Mettre à jour TIP1
        countDic["count_TIP_1_1"] = countDic["count_1X_1"] + countDic["count_12_1"]
        countDic["count_TIP_1_X"] = countDic["count_1X_X"] + countDic["count_12_X"]
        countDic["count_TIP_1_2"] = countDic["count_1X_2"] + countDic["count_12_2"]

        # Mettre à jour TIPX
        countDic["count_TIP_X_1"] = countDic["count_1X_1"] + countDic["count_X2_1"]
        countDic["count_TIP_X_X"] = countDic["count_1X_X"] + countDic["count_X2_X"]
        countDic["count_TIP_X_2"] = countDic["count_1X_2"] + countDic["count_X2_2"]

        # Mettre à jour TIP2
        countDic["count_TIP_2_1"] = countDic["count_12_1"] + countDic["count_X2_1"]
        countDic["count_TIP_2_X"] = countDic["count_12_X"] + countDic["count_X2_X"]
        countDic["count_TIP_2_2"] = countDic["count_12_2"] + countDic["count_X2_2"]

        # Mettre à jour TIP
        countDic["count_TIP_1"] = countDic["count_TIP_1_1"] + countDic["count_TIP_X_1"] + countDic["count_TIP_2_1"]
        countDic["count_TIP_X"] = countDic["count_TIP_1_X"] + countDic["count_TIP_X_X"] + countDic["count_TIP_2_X"]
        countDic["count_TIP_2"] = countDic["count_TIP_1_2"] + countDic["count_TIP_X_2"] + countDic["count_TIP_2_2"]

        # dict_max_1
        dict_max_1 = {'1': countDic["count_1_1"], 'X': countDic["count_1_X"], '2': countDic["count_1_2"]}
        dict_max_X = {'1': countDic["count_X_1"], 'X': countDic["count_X_X"], '2': countDic["count_X_2"]}
        dict_max_2 = {'1': countDic["count_2_1"], 'X': countDic["count_2_X"], '2': countDic["count_2_2"]}
        dict_max_1X = {'1': countDic["count_1X_1"], 'X': countDic["count_1X_X"], '2': countDic["count_1X_2"]}
        dict_max_12 = {'1': countDic["count_12_1"], 'X': countDic["count_12_X"], '2': countDic["count_12_2"]}
        dict_max_X2 = {'1': countDic["count_X2_1"], 'X': countDic["count_X2_X"], '2': countDic["count_X2_2"]}
        dict_max_1X2 = {'1': countDic["count_1X2_1"], 'X': countDic["count_1X2_X"], '2': countDic["count_1X2_2"]}
        dict_max_tip_1 = {'1': countDic["count_TIP_1_1"], 'X': countDic["count_TIP_1_X"], '2': countDic["count_TIP_1_2"]}
        dict_max_tip_X = {'1': countDic["count_TIP_X_1"], 'X': countDic["count_TIP_X_X"], '2': countDic["count_TIP_X_2"]}
        dict_max_tip_2 = {'1': countDic["count_TIP_2_1"], 'X': countDic["count_TIP_2_X"], '2': countDic["count_TIP_2_2"]}
        dict_max_tip = {'1': countDic["count_TIP_1"], 'X': countDic["count_TIP_X"], '2': countDic["count_TIP_2"]}

        # Utilisation de la fonction MAX
        max_1 = fonctionMAX.max_of_three_values(dict_max_1)
        max_X = fonctionMAX.max_of_three_values(dict_max_X)
        max_2 = fonctionMAX.max_of_three_values(dict_max_2)
        max_1X = fonctionMAX.max_of_three_values(dict_max_1X)
        max_12 = fonctionMAX.max_of_three_values(dict_max_12)
        max_X2 = fonctionMAX.max_of_three_values(dict_max_X2)
        max_1X2 = fonctionMAX.max_of_three_values(dict_max_1X2)
        max_TIP_1 = fonctionMAX.max_of_three_values(dict_max_tip_1)
        max_TIP_X = fonctionMAX.max_of_three_values(dict_max_tip_X)
        max_TIP_2 = fonctionMAX.max_of_three_values(dict_max_tip_2)
        max_TIP = fonctionMAX.max_of_three_values(dict_max_tip)


        # print("Nombre de lignes dans la colonne 'count1':", countALL)
        # print("Nombre de lignes dans la colonne 'countDic':", countDic["count_1_1"])
        # print("Nombre de lignes dans la colonne 'len(rows)':", len(rows))  # Afficher le nombre de lignes dans rows pour débogage

        
    except sqlite3.Error as e:
        print("Erreur SQLite:", e)
        

    # Mettre à jour les textes des labels après avoir obtenu count1
    update_label_texts()  


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Mettre à jour les textes des labels après avoir obtenu count1

def update_treeview(rows):
    for i in data_tree.get_children():
        data_tree.delete(i)
    for row in rows[:40]:
        data_tree.insert('', 'end', values=row)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def show_previous():
    # Mettre en œuvre la logique pour afficher les données précédentes
    pass

def show_next():
    # Mettre en œuvre la logique pour afficher les données suivantes
    pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
create_database()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Fonction pour créer un label avec un contour
def create_label_with_border(parent, text, row, column):
    labelBET = tk.Label(parent, text=text, relief="solid", borderwidth=1, width=10, height=2)
    labelBET.grid(row=row, column=column, padx=1, pady=1)
    return labelBET
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Exécutez la 1 requête SELECT pour afficher le tableau entier
conn = sqlite3.connect(db_name)
c = conn.cursor()
c.execute(f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,BUT1,BUT2,RESULTAT,PM,BUT FROM {table_name} ORDER BY ID DESC")
rows = c.fetchall()
# Exécutez la requête SELECT pour compter le nombre de lignes
c.execute(f"SELECT COUNT(*) FROM {table_name}")
# Récupérez le résultat de la requête
countALL = c.fetchone()[0]
conn.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# dictionnaire countDic basé sur la liste liste1 avec des valeurs initiales de 0
def initialize_count_dictionary():
    countListe = [
        "count_1_1", "count_1_X", "count_1_2", "count_1_P", "count_1_M", "count_1_B", "count_1_SB", "count_1",
        "count_X_1", "count_X_X", "count_X_2", "count_X_P", "count_X_M", "count_X_B", "count_X_SB", "count_X",
        "count_2_1", "count_2_X", "count_2_2", "count_2_P", "count_2_M", "count_2_B", "count_2_SB", "count_2",
        "count_1X_1", "count_1X_X", "count_1X_2", "count_1X_P", "count_1X_M", "count_1X_B", "count_1X_SB", "count_1X",
        "count_12_1", "count_12_X", "count_12_2", "count_12_P", "count_12_M", "count_12_B", "count_12_SB", "count_12",
        "count_X2_1", "count_X2_X", "count_X2_2", "count_X2_P", "count_X2_M", "count_X2_B", "count_X2_SB", "count_X2",
        "count_1X2_1", "count_1X2_X", "count_1X2_2", "count_1X2_P", "count_1X2_M", "count_1X2_B", "count_1X2_SB", "count_1X2",
        "count_TIP_1_1", "count_TIP_1_X", "count_TIP_1_2", "count_TIP_1_1", "count_TIP_1_1", "count_TIP_1_1",
        "count_TIP_X_1", "count_TIP_X_X", "count_TIP_X_2", "count_TIP_1_1", "count_TIP_1_1", "count_TIP_1_1",
        "count_TIP_2_1", "count_TIP_2_X", "count_TIP_2_2", "count_TIP_1_1", "count_TIP_1_1", "count_TIP_1_1",
        "count_TIP_1", "count_TIP_X", "count_TIP_2", "count_TIP_PM", "count_TIP_BUT", "count_TIP"
    ]
    countDic = {}
    for key in countListe:
        countDic[key] = 0
    return countDic


# Utilisation de la fonction pour initialiser le dictionnaire countDic
countDic = initialize_count_dictionary()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    

# Création de la fenêtre principale
root = tk.Tk()
root.title("BetSmart Betting Analysis Tool")
#largeur_fenetre = root.winfo_screenwidth() // 2   # Largeur de la moitié de l'écran
# Obtenir la taille de l'écran
largeur_ecran = root.winfo_screenwidth()   # Largeur de la moitié de l'écran
hauteur_ecran = root.winfo_screenheight()   # hauteur de la moitié de l'écran
root.geometry(f"{largeur_ecran}x{hauteur_ecran}")  # Taille de la fenêtre
root.iconbitmap("IMG/BetSmart_ICO.ico")
root.config(background="#FFF")

# Ajuster la taille de la fenêtre pour qu'elle prenne la taille de l'écran
root.geometry(f"{largeur_ecran}x{hauteur_ecran}")
root.state('zoomed')  # Pour Windows
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Frame 1 : Logo et Titre 6170B9
frame1 = tk.Frame(root, bg="#115571", width=largeur_ecran // 2) 
frame1.pack(side="left", fill="y")  # Remplir verticalement
# Ajout du logo au premier frame
logo = tk.PhotoImage(file="IMG/BetSmart_LOGO.jpg")
label_logo = tk.Label(frame1, image=logo, bg="#115571")
label_logo.pack()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# Frame 2 : Labels, Entries et Button
frame2 = tk.Frame(root, bg="#115571", width=largeur_ecran)
frame2.pack(padx=1, pady=1, fill="x")  # Remplir horizontalement avec un padding
# Labels
label1 = tk.Label(frame2, text="1")
label1.grid(row=0, column=1, padx=5, pady=5)
label2 = tk.Label(frame2, text="X")
label2.grid(row=0, column=2, padx=5, pady=5)
label3 = tk.Label(frame2, text="2")
label3.grid(row=0, column=3, padx=5, pady=5)
# Entries

search_entry_BET1 = tk.Entry(frame2)
search_entry_BET1.grid(row=1, column=1, padx=5, pady=5)
search_entry_BETX = tk.Entry(frame2)
search_entry_BETX.grid(row=1, column=2, padx=5, pady=5)
search_entry_BET2 = tk.Entry(frame2)
search_entry_BET2.grid(row=1, column=3, padx=5, pady=5)
# Button
button = tk.Button(frame2, text="Valider", command=search_BET)
button.grid(row=3, columnspan=4, pady=10)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Frame 3
frame3 = tk.Frame(root, bg="#115571", width=largeur_ecran // 2)  # Largeur de moitié de la fenêtre
frame3.pack(side="left", padx=1, pady=1,fill="both", expand=True)  # Remplir et étendre dans toutes les directions
#frame1.pack(side="left", fill="y") 
# Création des labels dans un tableau 8x7

def update_label_texts():

    label_texts = [
        "NBR : "+str(countALL), "1", "X", "2", "PM (2.5)", "B/SB", "TOTAL",
        "1 : ( " +str(search_entry_BET1.get())+ ")\n" + "SUM : " + str(countDic["count_1"]), countDic["count_1_1"] , countDic["count_1_X"], countDic["count_1_2"], str(countDic["count_1_P"]) + " P\n" + str(countDic["count_1_M"]) + " M", str(countDic["count_1_B"]) + " B\n" + str(countDic["count_1_SB"]) + " SB", str(max_1),
        "X : ( " +str(search_entry_BETX.get())+ ")\n" + "SUM : " + str(countDic["count_X"]), countDic["count_X_1"] , countDic["count_X_X"], countDic["count_X_2"], str(countDic["count_X_P"]) + " P\n" + str(countDic["count_X_M"]) + " M", str(countDic["count_X_B"]) + " B\n" + str(countDic["count_X_SB"]) + " SB", str(max_X),
        "2 : ( " +str(search_entry_BET2.get())+ ")\n" + "SUM : " + str(countDic["count_2"]), countDic["count_2_1"] , countDic["count_2_X"], countDic["count_2_2"], str(countDic["count_2_P"]) + " P\n" + str(countDic["count_2_M"]) + " M", str(countDic["count_2_B"]) + " B\n" + str(countDic["count_2_SB"]) + " SB", str(max_2),
        "1X\n" + "SUM : " + str(countDic["count_1X"]), countDic["count_1X_1"] , countDic["count_1X_X"], countDic["count_1X_2"], str(countDic["count_1X_P"]) + " P\n" + str(countDic["count_1X_M"]) + " M", str(countDic["count_1X_B"]) + " B\n" + str(countDic["count_1X_SB"]) + " SB", str(max_1X),
        "12\n" + "SUM : " + str(countDic["count_12"]), countDic["count_12_1"] , countDic["count_12_X"], countDic["count_12_2"], str(countDic["count_12_P"]) + " P\n" + str(countDic["count_12_M"]) + " M", str(countDic["count_12_B"]) + " B\n" + str(countDic["count_12_SB"]) + " SB", str(max_12),
        "X2\n" + "SUM : " + str(countDic["count_X2"]), countDic["count_X2_1"] , countDic["count_X2_X"], countDic["count_X2_2"], str(countDic["count_X2_P"]) + " P\n" + str(countDic["count_X2_M"]) + " M", str(countDic["count_X2_B"]) + " B\n" + str(countDic["count_X2_SB"]) + " SB", str(max_X2),
        "1X2\n" + "SUM : " + str(countDic["count_1X2"]), countDic["count_1X2_1"] , countDic["count_1X2_X"], countDic["count_1X2_2"], str(countDic["count_1X2_P"]) + " P\n" + str(countDic["count_1X2_M"]) + " M", str(countDic["count_1X2_B"]) + " B\n" + str(countDic["count_1X2_SB"]) + " SB", str(max_1X2),
        "TOTAL TIP 1", countDic["count_TIP_1_1"], countDic["count_TIP_1_X"], countDic["count_TIP_1_2"], "-", "-", str(max_TIP_1),
        "TOTAL TIP X", countDic["count_TIP_X_1"], countDic["count_TIP_X_X"], countDic["count_TIP_X_2"], "-", "-", str(max_TIP_X),
        "TOTAL TIP 2", countDic["count_TIP_2_1"], countDic["count_TIP_2_X"], countDic["count_TIP_2_2"], "-", "-", str(max_TIP_2),
        "TOTAL TIP", countDic["count_TIP_1"], countDic["count_TIP_X"], countDic["count_TIP_2"], "-", "-", str(max_TIP)
    ]
    # Création des labels dans un tableau 8x7
    labels = []  # Définir labels en dehors de toute fonction pour qu'il soit global
    for i in range(12):
        row_labels = []
        for j in range(7):
            label_text = label_texts[i * 7 + j]
            label = create_label_with_border(frame3, label_text, i, j)
            row_labels.append(label)
        labels.append(row_labels)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
# Frame 4 : Affichage des données MySQL
frame4 = tk.Frame(root, bg="#115571", width=largeur_ecran // 2)
frame4.pack(padx=1, pady=1,fill="both", expand=True)  # Remplir et étendre dans toutes les directions
# Créer un Treeview (remplacer les exemples par vos propres données)
data_tree = ttk.Treeview(frame4, columns=("PAYS", "TEAMS", "1","X", "2", "SCORE", "BUT1", "BUT2","RESULTAT", "PM", "BUT"), show='headings')
# Use integer values for alignment

data_tree.heading("PAYS", text="PAYS")
data_tree.heading("TEAMS", text="TEAMS")
data_tree.heading("1", text="1")
data_tree.heading("X", text="X")
data_tree.heading("2", text="2")
data_tree.heading("SCORE", text="SCORE")
data_tree.heading("BUT1", text="BUT1")
data_tree.heading("BUT2", text="BUT2")
data_tree.heading("RESULTAT", text="RESULTAT")
data_tree.heading("PM", text="PM")
data_tree.heading("BUT", text="BUT")
data_tree.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions

# Ajuster la largeur des colonnes en fonction du contenu
for column in data_tree['columns']:
    data_tree.heading(column, text=column, anchor=tk.CENTER)  # Centrer le texte de l'en-tête
    if column == "TEAMS":
        data_tree.column(column, anchor=tk.CENTER, width=150)  # Définir une largeur fixe pour la colonne "TEAMS"
    else:
        data_tree.column(column, anchor=tk.CENTER, width=tkFont.Font().measure(column))  # Ajuster la largeur de la colonne en fonction de son contenu

# Frame pour les boutons Suivant et Précédent
frame_buttons = tk.Frame(frame4)
frame_buttons.pack()

button_previous = tk.Button(frame_buttons, text="Précédent", command=show_previous)
button_previous.grid(row=0, column=0, padx=5, pady=5)

button_next = tk.Button(frame_buttons, text="Suivant", command=show_next)
button_next.grid(row=0, column=1, padx=5, pady=5)

# Ajouter une barre de défilement horizontal
scrollbar_x = ttk.Scrollbar(frame4, orient="horizontal", command=data_tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
data_tree.configure(xscrollcommand=scrollbar_x.set)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Après la définition des frames, exécutez la recherche initiale
search_BET()

root.mainloop()