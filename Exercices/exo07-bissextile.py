annee = int(input("Saisissez une année : "))
if annee % 4 == 0 and annee %100 != 0 or annee%400 ==0:
	print("Annee bissexile")
else :
	print("Année non bissextile")
input("Appuyez sur Enter")