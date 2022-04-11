nombre = int(input("Choisissez le nombre à exposer 10 "))
result = 1
compt = 0

while compt < 10 :
	result = result * nombre
	compt +=1


print(nombre, "exp 10 = ", result)
input("Appuyez sur Enter")