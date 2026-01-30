print("Soyez les binevenus sur la plateforme du Calcul de salaire")
famille = input("Votre Famille d'Emploi: ")
grade = input("Votre Grade: ")
classe = input("Votre Classe ")
echelon = input("Votre échelon: ")
lieu_travail = input("Votre lieu de travail: ")
situation_matrimoniale = input("Votre situation matrimoniale: ")
enfants = int(input("Le nombre d'enfants: "))

salaire_indiciaire_base = 0
indemnite_residence = 0
salaire_brut_imposable = 0
impot_brut_salaire = 0
allocation_familiale = 0
part = 1
reduction_impot = 0
prime_transport = 20000
indemnite_logement = 60000
ricf = 0
IRD = 233.457
retenue_mugefci_cmu = 0
its = 0


grudes = {"Administration": {
    "A3": {"2": {"1": 830, "2": 870, "3": 915, "4": 990},
           "1": {"1": 1100, "2": 1190, "3": 1255},
           "p": {"1": 1315, "2": 1380, "3": 1575},
           "e": {"1": 1735, "2": 1760, "3": 1790}},
    "A4": {"2": {"1": 895, "2": 940, "3": 1000, "4": 1100},
           "1": {"1": 1220, "2": 1315, "3": 1440},
           "p": {"1": 1605, "2": 1735, "3": 1890},
           "e": {"1": 2015, "2": 2065, "3": 2095}},
    "A5": {"2": {"1": 965, "2": 1005, "3": 1070, "4": 1165},
           "1": {"1": 1295, "2": 1390, "3": 1520},
           "p": {"1": 1680, "2": 1810, "3": 1905},
           "e": {"1": 2040, "2": 2105, "3": 2115}},
    "A6": {"2": {"1": 1315, "2": 1360, "3": 1410, "4": 1485},
           "1": {"1": 1580, "2": 1665, "3": 1765},
           "p": {"1": 1880, "2": 1955, "3": 1980},
           "e": {"1": 2065, "2": 2130, "3": 2145}},
    "A7": {"2": {"1": 1950, "2": 2015, "3": 2060, "4": 2135},
           "1": {"1": 2170, "2": 2265, "3": 2295},
           "p": {"1": 2350, "2": 2350, "3": 2350}},
    "B3": {"2": {"1": 680, "2": 730, "3": 785, "4": 840},
           "1": {"1": 890, "2": 950, "3": 1000},
           "p": {"1": 1065, "2": 1135, "3": 1185},
           "e": {"1": 1270, "2": 1300, "3": 1325}},
    "B1": {"2": {"1": 565, "2": 595, "3": 625, "4": 640},
           "1": {"1": 695, "2": 715, "3": 740},
           "p": {"1": 815, "2": 835, "3": 860},
           "e": {"1": 880, "2": 900, "3": 925}},
    "C3": {"2": {"1": 485, "2": 510, "3": 535, "4": 560},
           "1": {"1": 605, "2": 630, "3": 650},
           "p": {"1": 705, "2": 725, "3": 755},
           "e": {"1": 775, "2": 790, "3": 805}},
    "C2": {"2": {"1": 475, "2": 485, "3": 495, "4": 515},
           "1": {"1": 550, "2": 570, "3": 580},
           "p": {"1": 625, "2": 640, "3": 650},
           "e": {"1": 665, "2": 680, "3": 695}},
    "C1": {"2": {"1": 460, "2": 470, "3": 480, "4": 490},
           "1": {"1": 515, "2": 525, "3": 545},
           "p": {"1": 580, "2": 590, "3": 600},
           "e": {"1": 610, "2": 625, "3": 640}},
    "D2": {"2": {"1": 440, "2": 450, "3": 460, "4": 470},
           "1": {"1": 485, "2": 495, "3": 510},
           "p": {"1": 535, "2": 550, "3": 560},
           "e": {"1": 575, "2": 585, "3": 590}},
    "D1": {"2": {"1": 415, "2": 420, "3": 425, "4": 435},
           "1": {"1": 450, "2": 465, "3": 475},
           "p": {"1": 495, "2": 510, "3": 525},
           "e": {"1": 545, "2": 550, "3": 555}}},

    "Education-Formation": {
        "A3": {"2": {"1": 1225, "2": 1290, "3": 1385, "4": 1505},
               "1": {"1": 1605, "2": 1690, "3": 1825},
               "p": {"1": 1975, "2": 2120, "3": 2285},
               "e": {"1": 2380, "2": 2445, "3": 2500}},
        "A4": {"2": {"1": 1330, "2": 1410, "3": 1515, "4": 1645},
               "1": {"1": 1760, "2": 1855, "3": 2005},
               "p": {"1": 2155, "2": 2300, "3": 2460},
               "e": {"1": 2565, "2": 2630, "3": 2680}}},
    "A5": {"2": {"1": 1710, "2": 1785, "3": 1870, "4": 1975},
           "1": {"1": 2095, "2": 2175, "3": 2315},
           "p": {"1": 2470, "2": 2610, "3": 2785}},
    "A6": {"2": {"1": 2455, "2": 2510, "3": 2600, "4": 2685},
           "1": {"1": 2775, "2": 2845, "3": 2950},
           "p": {"1": 3080, "2": 3360}},

    "A7": {"2": {"1": 2985, "2": 3050, "3": 3140, "4": 3245},
           "1": {"1": 3340, "2": 3400, "3": 3515},
           "p": {"1": 3630, "2": 3630, "3": 3630}},
    "B3": {"2": {"1": 995, "2": 1065, "3": 1145, "4": 1220},
           "1": {"1": 1255, "2": 1315, "3": 1395},
           "p": {"1": 1440, "2": 1515, "3": 1585},
           "e": {"1": 1680, "2": 1705, "3": 1740}},
    "C3": {"2": {"1": 705, "2": 740, "3": 770, "4": 795},
           "1": {"1": 835, "2": 860, "3": 880},
           "p": {"1": 915, "2": 930, "3": 955},
           "e": {"1": 980, "2": 995, "3": 1015}},
    "C2": {"2": {"1": 660, "2": 685, "3": 695, "4": 705},
           "1": {"1": 725, "2": 735, "3": 745},
           "p": {"1": 780, "2": 785, "3": 795},
           "e": {"1": 805, "2": 820, "3": 835}}}


if famille == "Administration":
    if grade == "A3":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A3"]["e"]["3"] * IRD

    elif grade == "A4":
        indemnite_logement = 70000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A4"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A4"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A4"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A4"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A4"]["e"]["3"] * IRD

    elif grade == "A5":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A5"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A5"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A5"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A5"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A5"]["e"]["3"] * IRD

    elif grade == "A6":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A6"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A6"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A6"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A6"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A6"]["e"]["3"] * IRD

    elif grade == "A7":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A7"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A7"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["A7"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["A7"]["p"]["3"] * IRD

    elif grade == "B3":
        allocation_familiale = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B3"]["e"]["3"] * IRD

    elif grade == "B1":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B1"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B1"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B1"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["B1"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["B1"]["e"]["3"] * IRD

    elif grade == "C3":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C3"]["e"]["3"] * IRD

    elif grade == "C2":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C2"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C2"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C2"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C2"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C2"]["e"]["3"] * IRD

    elif grade == "C1":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C1"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C1"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C1"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["C1"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["C1"]["e"]["3"] * IRD

    elif grade == "D2":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["D2"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["D2"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["D2"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["D2"]["p"]["3"] * IRD

        elif grade == "D1":
            indemnite_logement = 60000
            if classe == "2":
                if echelon == "1":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["2"]["1"] * IRD
                elif echelon == "2":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["2"]["2"] * IRD
                elif echelon == "3":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["2"]["3"] * IRD
                else:
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["2"]["4"] * IRD
            if classe == "1":
                if echelon == "1":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["1"]["1"] * IRD
                elif echelon == "2":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["1"]["2"] * IRD
                else:
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["1"]["3"] * IRD
            if classe == "p":
                if echelon == "1":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["p"]["1"] * IRD
                elif echelon == "2":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["p"]["2"] * IRD
                else:
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["p"]["3"] * IRD
            if classe == "e":
                if echelon == "1":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["1"] * IRD
                elif echelon == "2":
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["2"] * IRD
                else:
                    salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Administration"]["D1"]["e"]["3"] * IRD

elif famille == "Education-Formation":
    if grade == "A3":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A3"]["e"]["3"] * IRD

    elif grade == "A4":
        indemnite_logement = 70000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A4"]["e"]["3"] * IRD

    elif grade == "A5":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A5"]["p"]["3"] * IRD


    elif grade == "A6":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A6"]["p"]["2"] * IRD

    elif grade == "A7":
        indemnite_logement = 90000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["A7"]["p"]["3"] * IRD

    elif grade == "B3":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["B3"]["e"]["3"] * IRD

    elif grade == "C3":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C3"]["e"]["3"] * IRD

    elif grade == "C2":
        indemnite_logement = 60000
        if classe == "2":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["2"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["2"]["2"] * IRD
            elif echelon == "3":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["2"]["3"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["2"]["4"] * IRD
        if classe == "1":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["1"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["1"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["1"]["3"] * IRD
        if classe == "p":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["p"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["p"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["p"]["3"] * IRD
        if classe == "e":
            if echelon == "1":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["e"]["1"] * IRD
            elif echelon == "2":
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["e"]["2"] * IRD
            else:
                salaire_indiciaire_base += grudes["Education-Formation"]["C2"]["e"]["3"] * IRD

indemnite_residence = salaire_indiciaire_base * 0.15
print(f"Votre indemnité de résidence est:  {round(indemnite_residence)}")
print(f"Votre Salaire Indiciaire de Base est: {round(salaire_indiciaire_base)}")
print(f"Votre Indemmité de logement est: {indemnite_logement}")
salaire_brut_imposable = round(salaire_indiciaire_base) + round(indemnite_residence)
print(f"Votre salaire brut imposable est:  {salaire_brut_imposable}")
if situation_matrimoniale == "marié" or situation_matrimoniale == "veuf":
    part = 2 + enfants * 0.5
elif situation_matrimoniale == "célibataire" or situation_matrimoniale == "divorcé" or situation_matrimoniale == "veuf":
    if enfants != 0:
        part = 1.5 + enfants * 0.5
print(f"Votre nombre de part est: {int(part)}")
allocation_familiale += 7500 * enfants

print(f"Votre allocation familiale est: {allocation_familiale}")
if part == 1.5:
    ricf = 5500
elif part == 2:
    ricf = 11000
elif part == 2.5:
    ricf = 16500
elif part == 3:
    ricf = 22000
elif part == 3.5:
    ricf = 27500
elif part == 4:
    ricf = 11000
elif part == 4.5:
    ricf = 33000
elif part == 5:
    ricf = 38500

print(f"Votre réduction d'impôt pour charge familiale est de:  {int(ricf)}")
if lieu_travail == "Chef-lieu":
    prime_transport -= 5000
elif lieu_travail == "Autre":
    prime_transport -= 10000
print(f"Votre prime de transport est: {prime_transport}")
if salaire_brut_imposable <= 75000:
    impot_brut_salaire = 0
elif 75000 < salaire_brut_imposable <= 240000:
    impot_brut_salaire = round((salaire_brut_imposable - 75000) * 0.16)
elif 240000 < salaire_brut_imposable <= 420000:
    impot_brut_salaire = 26400 + round((salaire_brut_imposable - 240000) * 0.21)
elif 420000 < salaire_brut_imposable <= 1000000:
    impot_brut_salaire = 64200 + round((salaire_brut_imposable - 420000) * 0.25)
elif 1000000 < salaire_brut_imposable <= 2700000:
    impot_brut_salaire = 102000 + round((salaire_brut_imposable - 1000000) * 0.28)
print(f"Votre impôt brut sur salaire est: {impot_brut_salaire}")
print(f"Votre allocation familiale est: {allocation_familiale}")
its = impot_brut_salaire - ricf

print(f"Votre impôt sur traitement de salaire est:  {its}")
retenue_pour_pension = round(salaire_indiciaire_base * 0.0833)
print(f"Votre retenue pour pension est:  {retenue_pour_pension}")
if round(salaire_indiciaire_base * 0.03) < 7004:
    retenue_mugefci_cmu += round(salaire_indiciaire_base * 0.03)
else:
    retenue_mugefci_cmu += 7004
print(f"Votre retenue pour MUGEFCI-CMU est:  {retenue_mugefci_cmu}")
retenue_retraite_complementaire = round(salaire_indiciaire_base * 0.05)
print(f"Votre retenue retraite complementaire est:  {retenue_retraite_complementaire}")
gains = round(salaire_indiciaire_base)+prime_transport+allocation_familiale+indemnite_logement+round(indemnite_residence)
retenues = its+retenue_pour_pension+retenue_mugefci_cmu+retenue_retraite_complementaire
salaire_net = gains - retenues
print(f"Total gains: {gains}")
print(f"Total retenues: {retenues}")

print(f"Votre salaire Net est de: {salaire_net}")

