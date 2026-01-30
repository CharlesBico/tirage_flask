import customtkinter as ctk

# Données des salaires
grades = {"Administration": {
    "A3": {"2": {"1": 830, "2": 870, "3": 915, "4": 990},
           "1": {"1": 1100, "2": 1190, "3": 1255},
           "p": {"1": 1315, "2": 1380, "3": 1575},
           "e": {"1": 1735, "2": 1760, "3": 1790}},
}}


# Fonction de calcul du salaire
def calculer_salaire():
    famille = famille_var.get()
    grade = grade_var.get()
    classe = classe_var.get()
    echelon = echelon_var.get()

    try:
        salaire = grades[famille][grade][classe][echelon]
        resultat_var.set(f"Salaire net: {salaire} FCFA")
    except KeyError:
        resultat_var.set("Données non disponibles")


# Création de la fenêtre principale
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Calculateur de salaire net")
app.geometry("400x300")

# Variables
famille_var = ctk.StringVar(value="Administration")
grade_var = ctk.StringVar(value="A3")
classe_var = ctk.StringVar(value="2")
echelon_var = ctk.StringVar(value="1")
resultat_var = ctk.StringVar()

# Widgets
ctk.CTkLabel(app, text="Famille d'emploi:").pack()
ctk.CTkComboBox(app, values=list(grades.keys()), variable=famille_var).pack()

ctk.CTkLabel(app, text="Grade:").pack()
ctk.CTkComboBox(app, values=list(grades["Administration"].keys()), variable=grade_var).pack()

ctk.CTkLabel(app, text="Classe:").pack()
ctk.CTkComboBox(app, values=["2", "1", "p", "e"], variable=classe_var).pack()

ctk.CTkLabel(app, text="Échelon:").pack()
ctk.CTkComboBox(app, values=["1", "2", "3", "4"], variable=echelon_var).pack()

ctk.CTkButton(app, text="Calculer", command=calculer_salaire).pack()
ctk.CTkLabel(app, textvariable=resultat_var).pack()

# Lancer l'application
app.mainloop()
