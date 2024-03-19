import sqlite3
import tkinter as tk
from tkinter import ttk
# from tkinter.ttk import Treeview
# from tkinter.ttk import Label
# "https://drive.google.com/file/d/1vCAOqLPDK4p1483FndCnOqBPuOzbmOOd/view?usp=sharing"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def create_database():
    global db_name, table_name
    db_name = "DB/primatips.sqlite"
    table_name = "primatips_table"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    #conn.commit()
    conn.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def search_BET():
    global countALL, countDic  # Déclarer count1 comme une variable globale
    search_BET1 = search_entry_BET1.get()
    search_BETX = search_entry_BETX.get()
    search_BET2 = search_entry_BET2.get()
    conn = sqlite3.connect(db_name)

    c = conn.cursor()
    cursorCount = conn.cursor()

    # Requête d'affichage 
    query = f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,BUT1,BUT2,RESULTAT,PM,BUT FROM {table_name} WHERE 1=1"

    # Requête pour compter
    queryCount = f"SELECT COUNT(*) FROM {table_name} WHERE 1=1"
    # Requête pour compter 1 
    
    queryCount_1_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BET1 LIKE '{search_BET1}%'"
    queryCount_1_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BET1 LIKE '{search_BET1}%'"
    queryCount_1_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BET1 LIKE '{search_BET1}%'"
    # Requête pour compter X
    queryCount_X_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BETX LIKE '{search_BETX}%'"
    queryCount_X_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BETX LIKE '{search_BETX}%'"
    queryCount_X_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BETX LIKE '{search_BETX}%'"
    # Requête pour compter 2
    queryCount_2_1 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=1  AND BET2 LIKE '{search_BET2}%'"
    queryCount_2_X = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT='X'  AND BET2 LIKE '{search_BET2}%'"
    queryCount_2_2 = f"SELECT COUNT(*) FROM {table_name} WHERE RESULTAT=2  AND BET2 LIKE '{search_BET2}%'"

    parameters = []

    if search_entry_BET1:
        query += " AND BET1 LIKE ?"
        queryCount += " AND BET1 LIKE ?"
        parameters.append(f"{search_BET1}%")

    if search_entry_BETX:
        query += " AND BETX LIKE ?"
        queryCount += " AND BETX LIKE ?"
        parameters.append(f"{search_BETX}%")

    if search_entry_BET2:
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

        parameters2 = []
        # Exécuter la requête de comptage 1X
        if (search_BET1 and search_BETX):
            queryCount1X = queryCount + " AND BET1 LIKE ? AND BETX LIKE ?"
            parameters2.append(f"{search_BET1}%")
            parameters2.append(f"{search_BETX}%")
            cursorCount.execute(queryCount1X, parameters2)
            countDic["count_1X"] = cursorCount.fetchone()[0]

        # Exécuter la requête de comptage 12
        if (search_BET1 and search_BET2):
            queryCount12 = queryCount + " AND BET1 LIKE ? AND BET2 LIKE ?"
            parameters2.append(f"{search_BET1}%")
            parameters2.append(f"{search_BET2}%")
            cursorCount.execute(queryCount12, parameters2)
            countDic["count_12"] = cursorCount.fetchone()[0]

        # Exécuter la requête de comptage X2
        if (search_BETX and search_BET2):
            queryCountX2 = queryCount + " AND BETX LIKE ? AND BET2 LIKE ?"
            parameters2.append(f"{search_BETX}%")
            parameters2.append(f"{search_BET2}%")
            cursorCount.execute(queryCountX2, parameters2)
            countDic["count_X2"] = cursorCount.fetchone()[0]


        # Exécuter la requête pour compter 1X2
        if search_BET1 and search_BETX and search_BET2:
            queryCount1X2 = queryCount + " AND BET1 LIKE ? AND BETX LIKE ? AND BET2 LIKE ?"
            parameters2.append(f"{search_BET1}%")
            parameters2.append(f"{search_BETX}%")
            parameters2.append(f"{search_BET2}%")
            cursorCount.execute(queryCount1X2, parameters2)
            countDic["count_1X2"] = cursorCount.fetchone()[0]

        # Exécuter la requête pour compter 1
        if search_BET1:
            cursorCount.execute(queryCount_1_1)
            countDic["count_1_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_X)
            countDic["count_1_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_1_2)
            countDic["count_1_2"] = cursorCount.fetchone()[0]
        else:
            countDic["count_1_1"] = 0
            countDic["count_1_X"] = 0
            countDic["count_1_2"] = 0

        # Exécuter la requête pour compter X
        if search_BETX:
            cursorCount.execute(queryCount_X_1)
            countDic["count_X_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_X)
            countDic["count_X_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_X_2)
            countDic["count_X_2"] = cursorCount.fetchone()[0]
        else:
            countDic["count_X_1"] = 0
            countDic["count_X_X"] = 0
            countDic["count_X_2"] = 0

        # Exécuter la requête pour compter 2
        if search_BET2:
            cursorCount.execute(queryCount_2_1)
            countDic["count_2_1"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_X)
            countDic["count_2_X"] = cursorCount.fetchone()[0]
            cursorCount.execute(queryCount_2_2)
            countDic["count_2_2"] = cursorCount.fetchone()[0]
        else:
            countDic["count_2_1"] = 0
            countDic["count_2_X"] = 0
            countDic["count_2_2"] = 0

        # Mettre à jour les textes des labels après avoir obtenu count1
        conn.commit()  # Valider les modifications dans la base de données
        update_treeview(rows)
        conn.close()

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
    for row in rows[:20]:
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
        "count_1_1", "count_1_X", "count_1_2", "count_1_PM", "count_1_BUT", "count_1",
        "count_X_1", "count_X_X", "count_X_2", "count_X_PM", "count_X_BUT", "count_X",
        "count_2_1", "count_2_X", "count_2_2", "count_2_PM", "count_2_BUT", "count_2",
        "count_1X_1", "count_1X_X", "count_1X_2", "count_1X_PM", "count_1X_BUT", "count_1X",
        "count_12_1", "count_12_X", "count_12_2", "count_12_PM", "count_12_BUT", "count_12",
        "count_X2_1", "count_X2_X", "count_X2_2", "count_X2_PM", "count_X2_BUT", "count_X2",
        "count_1X2_1", "count_1X2_X", "count_1X2_2", "count_1X2_PM", "count_1X2_BUT", "count_1X2"
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
root.title("PRIMATIPS BET")
#largeur_fenetre = root.winfo_screenwidth() // 2   # Largeur de la moitié de l'écran
# Obtenir la taille de l'écran
largeur_ecran = root.winfo_screenwidth()   # Largeur de la moitié de l'écran
hauteur_ecran = root.winfo_screenheight()   # hauteur de la moitié de l'écran
root.geometry(f"{largeur_ecran}x{hauteur_ecran}")  # Taille de la fenêtre
root.iconbitmap("IMG/PRIMATIPS_ICO.ico")
root.config(background="#002f5e")

# Ajuster la taille de la fenêtre pour qu'elle prenne la taille de l'écran
root.geometry(f"{largeur_ecran}x{hauteur_ecran}")
root.state('zoomed')  # Pour Windows
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Frame 1 : Logo et Titre
frame1 = tk.Frame(root, bg="#007acc")
frame1.pack(fill="x")  # Remplir horizontalement
# Ajout du logo au premier frame
logo = tk.PhotoImage(file="IMG/PRIMATIPS_LOGO.png")
label_logo = tk.Label(frame1, image=logo, bg="#007acc")
label_logo.pack()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Frame 2 : Labels, Entries et Button
frame2 = tk.Frame(root, bg="#007acc", width=largeur_ecran)
frame2.pack(padx=5, pady=5, fill="x")  # Remplir horizontalement avec un padding
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


# Frame 3 : Vide de couleur rouge
frame3 = tk.Frame(root, bg="#007acc", width=largeur_ecran // 2)  # Largeur de moitié de la fenêtre
frame3.pack(side="left", fill="y")  # Remplir verticalement

# Création des labels dans un tableau 8x7

def update_label_texts():

    label_texts = [
        "NBR : "+str(countALL), "1", "X", "2", "PM", "B/SB", "TOTAL",
        "1 : ( " +str(search_entry_BET1.get())+")", countDic["count_1_1"] , countDic["count_1_X"], countDic["count_1_2"], countDic["count_1_PM"], countDic["count_1_BUT"], countDic["count_1"],
        "X : ( " +str(search_entry_BETX.get())+")", countDic["count_X_1"] , countDic["count_X_X"], countDic["count_X_2"], countDic["count_X_PM"], countDic["count_X_BUT"], countDic["count_X"],
        "2 : ( " +str(search_entry_BET2.get())+")", countDic["count_2_1"] , countDic["count_2_X"], countDic["count_2_2"], countDic["count_2_PM"], countDic["count_2_BUT"], countDic["count_2"],
        "1X", countDic["count_1X_1"] , countDic["count_1X_X"], countDic["count_1X_2"], countDic["count_1X_PM"], countDic["count_1X_BUT"], countDic["count_1X"],
        "12", countDic["count_12_1"] , countDic["count_12_X"], countDic["count_12_2"], countDic["count_12_PM"], countDic["count_12_BUT"], countDic["count_12"],
        "X2", countDic["count_X2_1"] , countDic["count_X2_X"], countDic["count_X2_2"], countDic["count_X2_PM"], countDic["count_X2_BUT"], countDic["count_X2"],
        "1X2", countDic["count_1X2_1"] , countDic["count_1X2_X"], countDic["count_1X2_2"], countDic["count_1X2_PM"], countDic["count_1X2_BUT"], countDic["count_1X2"]
    ]
    # Création des labels dans un tableau 8x7
    labels = []  # Définir labels en dehors de toute fonction pour qu'il soit global
    for i in range(8):
        row_labels = []
        for j in range(7):
            label_text = label_texts[i * 7 + j]
            label = create_label_with_border(frame3, label_text, i, j)
            row_labels.append(label)
        labels.append(row_labels)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        
# Frame 4 : Affichage des données MySQL
frame4 = tk.Frame(root)
frame4.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions
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
update_treeview(rows)
root.mainloop()