import numpy as np
import matplotlib.pyplot as plt
from Tools.scripts.make_ctype import values
from numpy.linalg import eig
from numpy.linalg import det

A = np.array([[5,-3],[6,-4]])
lambda0, vect0 = eig(A)
print('Valeurs propres',lambda0)
print('Vecteurs propres',vect0)


# def calcul_base10(n):
#     L= []
#     while n>0:
#         q= n//10
#         r= n%10
#         L.append(r)
#         n=q
#     L.reverse()
#     return L
# n=int(input('Taper un entier strictement positif : '))
# print('Décomposition en base 10:',calcul_base10(n))

# déterminer la somme des cubes des chiffres d'un nombre strictement positif
# def somcube(n):
#     som=0
#     for i in range(len(n)):
#         som += (int(n[i]))**3
#
#     return som
#
# no=input('Taper un entier strictement positif : ')
# print(somcube(no))


L1=np.array([1,2,3]) # Cette fonction transforme la liste en tableau numpy
print(L1)
L1[0] # retourne l'élément 0 du tableau, c'est-à-dire la valeur 1
print(L1[0])
np.size(L1) # la fonction retourne la taille du tableau : 3
print(np.size(L1))
L2=np.array([[1,2,3,4],[5,6,7,8]])
# L2 est une matrice contenant 2 lignes et 4 colonnes
print(L2)
np.shape(L2) # la fonction retourne (2,4) soit 2 lignes et 4 colonnes
print(np.shape(L2))
# L2[i,j] # la fonction qui retourne l'élément de la ligne i et
# de la colonne j de la matrice L2
L2[0,0] # la fonction retourne 1
print(L2[0,0])
L2[0,1] # la fonction retourne 2
print(L2[0,1])
L2[1,3] # la fonction retourne 8
print(L2[1,3])
L2[0,:] # la fonction retourne la ligne : [1,2,3,4]
print(L2[0,:])
L2[:,1] # la fonction retourne la colonne : [2,6]
print(L2[:,1])
print(np.shape(L2[:,1]))
np.zeros(3) # crée le tableau [0,0,0]
print(np.zeros(3))
np.zeros((2,4)) # crée la matrice :
print(np.zeros((3,3)))

# np.linspace(1,3,5) # la fonction retourne : [1, 1.5, 2, 2.5, 3]
# print(np.linspace(1,3,5))
# np.arange(0,10) #
# print(np.arange(0,10))

R=np.array([[1,2,3],[4,5,6]])
print(R)
S=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(S)

def test(M):
    nbligne,nbcolonne=M.shape # on récupère nbligne et nbcolonne de la matrice M
    if nbligne == nbcolonne:
        return nbligne
    else:
        return 0
print('Fonction test pour R : ',test(R)) # renvoie 0
print('Fonction test pour S : ',test(S)) # renvoie 3


nums = [1,2,2,3,4,4]
print(list(set(nums)))
print(list(dict.fromkeys(nums)))