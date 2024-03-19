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
        "TOTAL TIP 1", countDic["count_TIP_1_1"], countDic["count_TIP_1_X"], countDic["count_TIP_1_2"], "0", "0", "0",
        "TOTAL TIP X", countDic["count_TIP_X_1"], countDic["count_TIP_X_X"], countDic["count_TIP_X_2"], "0", "0", "0",
        "TOTAL TIP 2", countDic["count_TIP_2_1"], countDic["count_TIP_2_X"], countDic["count_TIP_2_2"], "0", "0", "0",
        "TOTAL TIP", countDic["count_TIP_1"], countDic["count_TIP_X"], countDic["count_TIP_2"], "0", "0", "0"
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
