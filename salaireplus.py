print("=== PLATEFORME DE CALCUL DE SALAIRE ===")

# ------------------ ENTREES ------------------
famille = input("Famille d'emploi (Administration / Education-Formation): ")
grade = input("Grade (A3, A4, A5, A6, A7, B3, B1, C3, C2, C1, D2, D1): ")
classe = input("Classe (2, 1, p, e): ")
echelon = input("Échelon: ")
lieu_travail = input("Lieu de travail (Chef-lieu / Autre): ")
situation_matrimoniale = input("Situation matrimoniale: ")
enfants = int(input("Nombre d'enfants: "))

# ------------------ CONSTANTES ------------------
IRD = 233.457
prime_transport = 25000
indemnite_logement = 60000

# ------------------ GRILLES ------------------
grudes = {
    "Administration": {
        "A3": {"2": {"1": 830, "2": 870, "3": 915, "4": 990}},
        "B3": {"2": {"1": 680, "2": 730, "3": 785, "4": 840}},
        "C1": {"2": {"1": 460, "2": 470, "3": 480, "4": 490}}
    },
    "Education-Formation": {
        "A3": {"2": {"1": 1225, "2": 1290, "3": 1385, "4": 1505}},
        "B3": {"2": {"1": 995, "2": 1065, "3": 1145, "4": 1220}}
    }
}

# ------------------ SALAIRE INDICIAIRE ------------------
try:
    indice = grudes[famille][grade][classe][echelon]
except KeyError:
    print("❌ Paramètres invalides")
    exit()

salaire_indiciaire_base = indice * IRD
indemnite_residence = salaire_indiciaire_base * 0.15
salaire_brut_imposable = round(salaire_indiciaire_base + indemnite_residence)

print(f"Salaire indiciaire de base : {round(salaire_indiciaire_base)}")
print(f"Indemnité de résidence : {round(indemnite_residence)}")
print(f"Salaire brut imposable : {salaire_brut_imposable}")

# ------------------ PARTS ------------------
part = 1
if situation_matrimoniale in ["marié", "veuf"]:
    part = 2 + enfants * 0.5
elif situation_matrimoniale in ["célibataire", "divorcé"] and enfants > 0:
    part = 1.5 + enfants * 0.5

print(f"Nombre de parts : {part}")

# ------------------ RICF ------------------
ricf_table = {
    1.5: 5500,
    2: 11000,
    2.5: 16500,
    3: 22000,
    3.5: 27500,
    4: 11000,
    4.5: 33000,
    5: 38500
}

ricf = ricf_table.get(part, 0)

# ------------------ IMPOT BRUT ------------------
if salaire_brut_imposable <= 75000:
    impot_brut_salaire = 0
elif salaire_brut_imposable <= 240000:
    impot_brut_salaire = round((salaire_brut_imposable - 75000) * 0.16)
elif salaire_brut_imposable <= 420000:
    impot_brut_salaire = 26400 + round((salaire_brut_imposable - 240000) * 0.21)
elif salaire_brut_imposable <= 1000000:
    impot_brut_salaire = 64200 + round((salaire_brut_imposable - 420000) * 0.25)
else:
    impot_brut_salaire = 102000 + round((salaire_brut_imposable - 1000000) * 0.28)

print(f"Impôt brut sur salaire : {impot_brut_salaire}")

# ------------------ ITS CORRIGÉ ------------------
its = impot_brut_salaire - ricf

if its < 0:
    for p in sorted(ricf_table.keys(), reverse=True):
        if p < part:
            test_its = impot_brut_salaire - ricf_table[p]
            if test_its >= 0:
                ricf = ricf_table[p]
                its = test_its
                break
    else:
        its = 0

print(f"RICF appliquée : {ricf}")
print(f"ITS : {its}")

# ------------------ RETENUES ------------------
retenue_pension = round(salaire_indiciaire_base * 0.0833)
retenue_mugefci = min(round(salaire_indiciaire_base * 0.03), 7004)
retenue_retraite = round(salaire_indiciaire_base * 0.05)

# ------------------ ALLOCATIONS ------------------
allocation_familiale = enfants * 7500

if lieu_travail == "Abidjan":
    prime_transport -= 5000
elif lieu_travail == "Chef-lieu":
    prime_transport -= 10000
else:
    prime_transport -= 15000

# ------------------ NET ------------------
gains = round(salaire_indiciaire_base) + round(indemnite_residence) + indemnite_logement + prime_transport + allocation_familiale
retenues = its + retenue_pension + retenue_mugefci + retenue_retraite
salaire_net = gains - retenues

print("------ RÉCAPITULATIF ------")
print(f"Gains : {gains}")
print(f"Retenues : {retenues}")
print(f"Salaire net : {salaire_net}")
