nombre = int(input("Choisissez le nombre à exposer "))
exposant  = int(input("Choisissez l'exposant "))
result = 1
compt = 0

while compt < exposant :
	result = result * nombre
	compt +=1


print(nombre, "exp ", exposant," = ", result)
input("Appuyez sur Enter")