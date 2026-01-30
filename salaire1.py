# import customtkinter as ctk
from datetime import datetime
# import math
#
#
# # Données des salaires
# grades = {"Administration": {
#     "A3": {"2": {"1": 830, "2": 870, "3": 915, "4": 990},
#            "1": {"1": 1100, "2": 1190, "3": 1255},
#            "p": {"1": 1315, "2": 1380, "3": 1575},
#            "e": {"1": 1735, "2": 1760, "3": 1790}},
#     "A4": {"2": {"1": 895, "2": 940, "3": 1000, "4": 1100},
#            "1": {"1": 1220, "2": 1315, "3": 1440},
#            "p": {"1": 1605, "2": 1735, "3": 1890},
#            "e": {"1": 2015, "2": 2065, "3": 2095}},
#     "A5": {"2": {"1": 965, "2": 1005, "3": 1070, "4": 1165},
#            "1": {"1": 1295, "2": 1390, "3": 1520},
#            "p": {"1": 1680, "2": 1810, "3": 1905},
#            "e": {"1": 2040, "2": 2105, "3": 2115}},
#     "A6": {"2": {"1": 1315, "2": 1360, "3": 1410, "4": 1485},
#            "1": {"1": 1580, "2": 1665, "3": 1765},
#            "p": {"1": 1880, "2": 1955, "3": 1980},
#            "e": {"1": 2065, "2": 2130, "3": 2145}},
#     "A7": {"2": {"1": 1950, "2": 2015, "3": 2060, "4": 2135},
#            "1": {"1": 2170, "2": 2265, "3": 2295},
#            "p": {"1": 2350, "2": 2350, "3": 2350}},
#     "B3": {"2": {"1": 680, "2": 730, "3": 785, "4": 840},
#            "1": {"1": 890, "2": 950, "3": 1000},
#            "p": {"1": 1065, "2": 1135, "3": 1185},
#            "e": {"1": 1270, "2": 1300, "3": 1325}},
#     "B1": {"2": {"1": 565, "2": 595, "3": 625, "4": 640},
#            "1": {"1": 695, "2": 715, "3": 740},
#            "p": {"1": 815, "2": 835, "3": 860},
#            "e": {"1": 880, "2": 900, "3": 925}},
#     "C3": {"2": {"1": 485, "2": 510, "3": 535, "4": 560},
#            "1": {"1": 605, "2": 630, "3": 650},
#            "p": {"1": 705, "2": 725, "3": 755},
#            "e": {"1": 775, "2": 790, "3": 805}},
#     "C2": {"2": {"1": 475, "2": 485, "3": 495, "4": 515},
#            "1": {"1": 550, "2": 570, "3": 580},
#            "p": {"1": 625, "2": 640, "3": 650},
#            "e": {"1": 665, "2": 680, "3": 695}},
#     "C1": {"2": {"1": 460, "2": 470, "3": 480, "4": 490},
#            "1": {"1": 515, "2": 525, "3": 545},
#            "p": {"1": 580, "2": 590, "3": 600},
#            "e": {"1": 610, "2": 625, "3": 640}},
#     "D2": {"2": {"1": 440, "2": 450, "3": 460, "4": 470},
#            "1": {"1": 485, "2": 495, "3": 510},
#            "p": {"1": 535, "2": 550, "3": 560},
#            "e": {"1": 575, "2": 585, "3": 590}},
#     "D1": {"2": {"1": 415, "2": 420, "3": 425, "4": 435},
#            "1": {"1": 450, "2": 465, "3": 475},
#            "p": {"1": 495, "2": 510, "3": 525},
#            "e": {"1": 545, "2": 550, "3": 555}}},
#
#     "Education-Formation": {
#         "A3": {"2": {"1": 1225, "2": 1290, "3": 1385, "4": 1505},
#                "1": {"1": 1605, "2": 1690, "3": 1825},
#                "p": {"1": 1975, "2": 2120, "3": 2285},
#                "e": {"1": 2380, "2": 2445, "3": 2500}},
#         "A4": {"2": {"1": 1330, "2": 1410, "3": 1515, "4": 1645},
#                "1": {"1": 1760, "2": 1855, "3": 2005},
#                "p": {"1": 2155, "2": 2300, "3": 2460},
#                "e": {"1": 2565, "2": 2630, "3": 2680}},
#         "A5": {"2": {"1": 1710, "2": 1785, "3": 1870, "4": 1975},
#                "1": {"1": 2095, "2": 2175, "3": 2315},
#                "p": {"1": 2470, "2": 2610, "3": 2785}},
#         "A6": {"2": {"1": 2455, "2": 2510, "3": 2600, "4": 2685},
#                "1": {"1": 2775, "2": 2845, "3": 2950},
#                "p": {"1": 3080, "2": 3360}},
#
#         "A7": {"2": {"1": 2985, "2": 3050, "3": 3140, "4": 3245},
#                "1": {"1": 3340, "2": 3400, "3": 3515},
#                "p": {"1": 3630, "2": 3630, "3": 3630}},
#         "B3": {"2": {"1": 995, "2": 1065, "3": 1145, "4": 1220},
#                "1": {"1": 1255, "2": 1315, "3": 1395},
#                "p": {"1": 1440, "2": 1515, "3": 1585},
#                "e": {"1": 1680, "2": 1705, "3": 1740}},
#         "C3": {"2": {"1": 705, "2": 740, "3": 770, "4": 795},
#                "1": {"1": 835, "2": 860, "3": 880},
#                "p": {"1": 915, "2": 930, "3": 955},
#                "e": {"1": 980, "2": 995, "3": 1015}},
#         "C2": {"2": {"1": 660, "2": 685, "3": 695, "4": 705},
#                "1": {"1": 725, "2": 735, "3": 745},
#                "p": {"1": 780, "2": 785, "3": 795},
#                "e": {"1": 805, "2": 820, "3": 835}}}
# }
#
#
# # Fonction de calcul du salaire
# def calculer_salaire():
#     famille = famille_var.get()
#     grade = grade_var.get()
#     classe = classe_var.get()
#     echelon = echelon_var.get()
#
#     try:
#         salaire = grades[famille][grade][classe][echelon] * 233.457
#         resultat_var.set(f"Votre Salaire Indiciaire de Base est: {round(salaire)} FCFA")
#     except KeyError:
#         resultat_var.set("Données non disponibles")
#
#
# # Fonction pour mettre à jour les grades selon la famille
# def update_grades(*args):
#     grade_combobox.configure(values=list(grades[famille_var.get()].keys()))
#     grade_var.set(list(grades[famille_var.get()].keys())[0])
#     update_classes()
#
#
# # Fonction pour mettre à jour les classes selon le grade
# def update_classes(*args):
#     classe_combobox.configure(values=list(grades[famille_var.get()][grade_var.get()].keys()))
#     classe_var.set(list(grades[famille_var.get()][grade_var.get()].keys())[0])
#     update_echelons()
#
#
# # Fonction pour mettre à jour les échelons selon la classe
# def update_echelons(*args):
#     echelon_combobox.configure(values=list(grades[famille_var.get()][grade_var.get()][classe_var.get()].keys()))
#     echelon_var.set(list(grades[famille_var.get()][grade_var.get()][classe_var.get()].keys())[0])
#
#
# # Création de la fenêtre principale
# ctk.set_appearance_mode("light")
# app = ctk.CTk()
# app.title("Calculateur de salaire net des Fonctionnaires de Côte d'Ivoire")
# app.geometry("500x430")
#
# # Variables
# famille_var = ctk.StringVar(value=list(grades.keys())[0])
# grade_var = ctk.StringVar()
# classe_var = ctk.StringVar()
# echelon_var = ctk.StringVar()
# resultat_var = ctk.StringVar()
#
# # Widgets
# ctk.CTkLabel(app, text="Famille d'emploi:").pack()
# famille_combobox = ctk.CTkComboBox(app, values=list(grades.keys()), variable=famille_var, command=update_grades)
# famille_combobox.pack()
#
# ctk.CTkLabel(app, text="Grade:").pack()
# grade_combobox = ctk.CTkComboBox(app, variable=grade_var, command=update_classes)
# grade_combobox.pack()
#
# ctk.CTkLabel(app, text="Classe:").pack()
# classe_combobox = ctk.CTkComboBox(app, variable=classe_var, command=update_echelons)
# classe_combobox.pack()
#
# ctk.CTkLabel(app, text="Échelon:").pack()
# echelon_combobox = ctk.CTkComboBox(app, variable=echelon_var)
# echelon_combobox.pack()
#
# ctk.CTkButton(app, text="Calculer", command=calculer_salaire).pack()
# ctk.CTkLabel(app, textvariable=resultat_var).pack()
#
# # Mise à jour des options
# # grade_var.trace_add("write", update_classes)
# # classe_var.trace_add("write", update_echelons)
# update_grades()
#
# # Lancer l'application
# app.mainloop()

grades = {"Administration": {
    "A3": {"2": {"1": 830, "2": 870, "3": 915, "4": 990},
           "1": {"1": 1100, "2": 1190, "3": 1255},
           "p": {"1": 1315, "2": 1380, "3": 1575},
           "e": {"1": 1735, "2": 1760, "3": 1790}}}}
print(list(grades.keys())[0])
date_debut = input("Date de debut de carrière: ")
date_debut_carriere = datetime.strptime(date_debut, "%d/%m/%Y")
print(date_debut_carriere)
date_fin = input("Date de fin de carrière: ")
date_fin_carriere = datetime.strptime(date_fin, "%d/%m/%Y")
an = date_fin_carriere - date_debut_carriere
ans = round(an.days / 365.25)
print(f"la durée est {ans}")
# annee = float(input("Nombre d'années: "))
indice_dernier = int(input("Dernier indice: "))
pension = ans * indice_dernier * 0.0175 * 2801.48
print(f"la pension est: {round(pension)}")
enfants = int(input("Nombre d'enfants entre 16 et 21 ans: "))
if enfants <= 3:
    pension_mensuelle = pension / 12 * 1.1 + enfants * 7500
else:
    pension_mensuelle = pension / 12 * (1 + (enfants - 3) * 0.05 + 0.1) + 22500

print(f"la pension mensuelle est: {round(pension_mensuelle)}")
# 30 (Années de services) * 1.75 (Taux d'annuité liquidable) * 2445 (Dernier indice détenu durant au moins 6 mois) *2801.48(valeur du onit d'indice)= 3596050)


# jour = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi']
# a, b = 0, 0
# while a < 25:
#     a = a + 1
#     b = a % 7
#     print(a, jour[b])
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['jan', 'fev', 'mar', 'avr', 'mai', 'jui', 'jul', 'aou', 'sep', 'oct', 'nov', 'dec']
# t3 = []
# i = 0
# while i < len(t1):
#     t3.append(t2[i])
#     t3.append(t1[i])
#     i = i + 1
# print(t3)
#


# try:
#     nombre = int(input("Entrez un nombre : "))
#     racine = math.isqrt(nombre)  # Renvoie la partie entière de la racine carrée
#
#     if racine ** 2 == nombre:
#         print(f"La racine carrée parfaite de {nombre} est {racine}.")
#     else:
#         print(f"{nombre} n'a pas de racine carrée parfaite.")
# except ValueError:
#     print("Veuillez entrer un nombre entier valide.")
# except OverflowError:
#     print("Le nombre est trop grand.")

# nombre = int(input("Entrez un nombre : "))
# racine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# carre = [i ** 2 for i in racine]
# couple = []
# n = 0
# while n < len(racine):
#     couple.append(racine[n])
#     couple.append(carre[n])
#     n += 1
# print(couple)


# districts = {"Woroba": {
#     "Worodougou": ["Séguéla", "Kani"],
#     "Bafing": ["Touba", "Koro", "Ouaninou"],
#     "Béré": ["Mankono", "Dianra", "Kounahiri"]},
#     "Savanes": {
#         "Poro": ["Korhogo", "Sinematiali", "M'Bengué"],
#         "Tchologo": ["Ferkéssedougou", "Ouangolodougou", "Kong"],
#         "Bagoué": ["Boundiali", "Kouto", "Tengrela"]}}
#
# for item in districts.items():
#     if item[0].endswith("s"):
#         print(f"le Chef-lieu du district des {item[0].upper()} est le {list(item[1].keys())[0].capitalize()}")
#     else:
#         print(f"le Chef-lieu du district du {item[0].upper()} est le {list(item[1].keys())[0].capitalize()}")


    # print(districts["Woroba"]["Worodougou"][0])

# print(districts.values())
# print(districts.items())
