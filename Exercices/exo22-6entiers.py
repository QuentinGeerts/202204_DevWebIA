# Écrire un algorithme qui saisit 6 entiers et les stocke dans un tableau, 
# puis affiche le contenu de ce tableau une fois qu’il est rempli.

from random import randint

LENGTH = 6

# -- 1ere façon --

# tab = [0, 0, 0, 0, 0, 0]
# ou
tab = [0] * LENGTH

for i in range(len(tab)):
  tab[i] = randint(1, 10)

print(tab)


# -- 2eme façon --

tab2 = []

for i in range(LENGTH):
  tab2.append(randint(1, 10))

print(tab2)