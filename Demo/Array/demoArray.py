ints = [8, 4, 0, -5, 6, 1, 0]
#       0  1  2   3  4  5  6

print(ints)


# Retourer la taille du tableau => le nombre d'éléments dans le tableau
print("Taille du tableau :", len(ints)) # output : 7

# Opérateur d'accès : []

# utilisation de l'opérateur d'accès avec indice

print("ints[0]", ints[0]) # output : 8
# print(ints[7]) # output : IndexError: list index out of range
print("ints[-2]", ints[-2]) # output : 1

# utilisation de l'opérateur d'accès avec une range
# nom_tableau[ position de départ (inclus) : position d'arrivée (exclue) : pas ]
print("ints[2:5]", ints[2:5]) # output : [0, -5, 6]

# [:] => [0:len(ints)]
ints_copy = ints[:]

print("ints", ints)
print("ints_copy", ints_copy)

print("ints[:5]", ints[:5]) # output : [8, 4, 0, -5, 6]
print("ints[:5]", ints[5:]) # output : [1, 0]

# [::] => [0 : len(ints) : 1]
print("ints[::1]", ints[::1]) # output : [8, 4, 0, -5, 6, 1, 0]
print("ints[::1]", ints[::2]) # output : [8, 0, 6, 0]
print("ints[::1]", ints[::-1]) # output : [0, 1, 6, -5, 0, 4, 8]

# --- Méthodes ---

t = []

print(t)

# Ajouter une valeur au tableau (à la fin)
# Array.append() 

# t.append(3)
# t.append("Bonjour")
# t.append(True)
# t.append(["Bonjour à tous"])

# Ajouter une valeur au tableau à la position donnée
# Array.insert(index, valeur)

t.insert(0, "Alain")
t.insert(2, "Delphine")
t.insert(2, "Lucas")
t.insert(2, "Willy")

t.insert(len(t), "Didier")

# Retirer une valeur au tableau (à la fin)
# Array.pop(index = -1)

removedItem = t.pop()
print(removedItem)
# t => ['Alain', 'Delphine', 'Willy', 'Lucas']

# Retourner un tableau
# t.reverse()

t_copy = t[::-1]
print(t_copy)
print(t)

# Fusionner deux tableaux ensemble
# Array.extend(Array)

t1 = [1, 2, 3]
t2 = [4, 5, 6]

print(t1)
print(t2)

# t1.extend(t2)

# print(t1)
# print(t2)

t3 = t1 + t2

print(t3)

# Initialiser un tableau avec au préalable 10 éléments

t4 = [0] * 10

print(t4)

# --- Parcours de tableau ---

# Initialisation
i = 0

# Condition
while i < len(t4):
  print(t4[i])

  # Incrémentation
  i += 1

print("")

for i in range(len(t4)):
  print(i, t4[i])

for i, v in enumerate(t4):
  print(i, v)

for v in t4:
  print(v)
