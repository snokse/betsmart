import tkinter as tk
import mysql.connector
import tkinter.ttk as ttk


# MySQL connection details (replace with your credentials)
db_host = "localhost"
db_user = "root"
db_password = ""
db_name = "primatips"
table_name = "primatips_table"
# Connect to MySQL database
def connect_to_database():
    global connection,cursor 
    try:
        connection = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = connection.cursor()
        print("Connected to MySQL database successfully!")
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")

# Fetch data from MySQL table
def fetch_data():
    global data, cursor 
    try:
        # Replace "your_table_name" and "your_columns" with your actual table and columns
        requete = f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM {table_name}"
        cursor.execute(requete)
        data = cursor.fetchall()
        # Fermeture du curseur
        # cursor.close()
        
    except mysql.connector.Error as err:
        print(f"Error fetching data from MySQL table: {err}")

# Fonction de recherche
def rechercher():
    global data, cursor, data1
    try:
        valeur_saisie = int(entry1.get())
        # Exécution de la requête de recherche
        requete = f"SELECT PAYS,TEAMS,BET1,BETX,BET2,SCORE,RESULTAT,PM,BUT FROM {table_name} WHERE BET1 {valeur_saisie}"
        requete1 = f"SELECT COUNT(*) FROM {table_name} WHERE BET1 LIKE {valeur_saisie}"
        cursor.execute(requete)
        cursor.execute(requete1)
        data = cursor.fetchall()
        data1 = cursor.fetchone()
        print(data1)
        # Fermeture du curseur
        # cursor.close()

    except mysql.connector.Error as err:
        print(f"Error fetching data from MySQL table: {err}")


# Fonction pour créer un label avec un contour
def create_label_with_border(parent, text, row, column):
    labelBET = tk.Label(parent, text=text, relief="solid", borderwidth=1, width=10, height=2)
    labelBET.grid(row=row, column=column, padx=1, pady=1)
    return labelBET

# Création de la fenêtre principale
root = tk.Tk()
root.title("PRIMATIPS BET")
#largeur_fenetre = root.winfo_screenwidth() // 2   # Largeur de la moitié de l'écran
largeur_fenetre = root.winfo_screenwidth()   # Largeur de la moitié de l'écran
hauteur_fenetre = root.winfo_screenheight()   # hauteur de la moitié de l'écran
root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")  # Taille de la fenêtre
root.iconbitmap("IMG/PRIMATIPS_ICO.ico")
root.config(background="#002f5e")

# Frame 1 : Logo et Titre
frame1 = tk.Frame(root, bg="#007acc")
frame1.pack(fill="x")  # Remplir horizontalement
# Ajout du logo au premier frame
logo = tk.PhotoImage(file="IMG/PRIMATIPS_LOGO.png")
label_logo = tk.Label(frame1, image=logo, bg="#007acc")
label_logo.pack()

# Frame 2 : Labels, Entries et Button
frame2 = tk.Frame(root, bg="#007acc", width=largeur_fenetre // 2)
frame2.pack(padx=10, pady=10, fill="x")  # Remplir horizontalement avec un padding
# Labels
label1 = tk.Label(frame2, text="1")
label1.grid(row=0, column=1, padx=5, pady=5)
label2 = tk.Label(frame2, text="X")
label2.grid(row=0, column=2, padx=5, pady=5)
label3 = tk.Label(frame2, text="2")
label3.grid(row=0, column=3, padx=5, pady=5)
# Entries
global entry1
entry1 = tk.Entry(frame2)
entry1.grid(row=1, column=1, padx=5, pady=5)
entry2 = tk.Entry(frame2)
entry2.grid(row=1, column=2, padx=5, pady=5)
entry3 = tk.Entry(frame2)
entry3.grid(row=1, column=3, padx=5, pady=5)
# Button
button = tk.Button(frame2, text="Valider", command=rechercher)
button.grid(row=3, columnspan=4, pady=10)

# Frame 3 : Vide de couleur rouge
frame3 = tk.Frame(root, bg="#007acc", width=largeur_fenetre // 2)  # Largeur de moitié de la fenêtre
frame3.pack(side="left", fill="y")  # Remplir verticalement

# Création des labels dans un tableau 8x7
label_texts = [
    "COTE", "1", "X", "2", "PM", "B/SB", "TOTAL",
    "1", "Label 9", "Label 10", "Label 11", "Label 12", "Label 13", "Label 14",
    "X", "Label 16", "Label 17", "Label 18", "Label 19", "Label 20", "Label 21",
    "2", "Label 23", "Label 24", "Label 25", "Label 26", "Label 27", "Label 28",
    "1X", "Label 30", "Label 31", "Label 32", "Label 33", "Label 34", "Label 35",
    "12", "Label 37", "Label 38", "Label 39", "Label 40", "Label 41", "Label 42",
    "X2", "Label 44", "Label 45", "Label 46", "Label 47", "Label 48", "Label 49",
    "1X2", "Label 51", "Label 52", "Label 53", "Label 54", "Label 55", "Label 56"
]

labels = []
for i in range(8):
    row_labels = []
    for j in range(7):
        label_text = label_texts[i * 7 + j]
        label = create_label_with_border(frame3, label_text, i, j)
        row_labels.append(label)
    labels.append(row_labels)


# Frame 4 : Affichage des données MySQL
frame4 = tk.Frame(root)
frame4.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions
# Créer un Treeview (remplacer les exemples par vos propres données)
data_tree = ttk.Treeview(frame4, columns=("PAYS", "TEAMS", "1","X", "2", "SCORE","RESULTAT", "PM", "BUT"))
data_tree.heading("PAYS", text="PAYS")
data_tree.heading("TEAMS", text="TEAMS")
data_tree.heading("1", text="1")
data_tree.heading("X", text="X")
data_tree.heading("2", text="2")
data_tree.heading("SCORE", text="SCORE")
data_tree.heading("RESULTAT", text="RESULTAT")
data_tree.heading("PM", text="PM")
data_tree.heading("BUT", text="BUT")
data_tree.pack(fill="both", expand=True)  # Remplir et étendre dans toutes les directions

# Populate the Treeview with fetched data
def populate_treeview():
    for row in data:
        data_tree.insert("", tk.END, values=row)

# Ajouter une barre de défilement horizontal
scrollbar_x = ttk.Scrollbar(frame4, orient="horizontal", command=data_tree.xview)
scrollbar_x.pack(side="bottom", fill="x")
data_tree.configure(xscrollcommand=scrollbar_x.set)

# Main program loop
def main():
    connect_to_database()
    fetch_data()
    populate_treeview()
    root.mainloop()


if __name__ == "__main__":
    main()
