etudiant = {
    'Nom':'Bico',
    'Age':49
}
# print(etudiant) # {'Nom': 'Bico', 'Age': 49}
# print(etudiant.get("Nom")) # Bico
# print(etudiant.keys()) # dict_keys(['Nom', 'Age'])
# print(etudiant.values()) # dict_values(['Bico', 49])
# print(etudiant.items()) # dict_items([('Nom', 'Bico'), ('Age', 49)])
# print(etudiant.update({'Age':50}))
# print(etudiant)
# print(etudiant.pop('Age'))
# print(etudiant)
# print(etudiant.popitem())
# print(etudiant)
# etudiant['Matière']="Informatique"
# etudiant['cout']=3000
# print(etudiant)
from functools import reduce
liste = [1, 2, 3, 4, 5,17,20, 31]
somme = 0
produit = 1
for i in liste:
    produit *= i
    somme += i
print(produit)
print(somme)
carre = list(map(lambda som: som**2, liste))
pairs = list(filter(lambda x: x%2==0, liste))
impairs = list(filter(lambda x: x%2==1, liste))
imp = list(filter(lambda x: x%2!=0, liste))
print(carre)
print(pairs)
print(impairs)
print(imp)

print(reduce(lambda x,y: x*y, liste))
print(reduce(lambda x,y: x+y, liste))