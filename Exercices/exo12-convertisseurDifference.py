j1 = int(input("Nb j1 : "))
h1 = int(input("Nb h1 : "))
m1 = int(input("Nb m1 : "))
s1 = int(input("Nb s1 : "))
j2 = int(input("Nb j2 : "))
h2 = int(input("Nb h2 : "))
m2 = int(input("Nb m2 : "))
s2 = int(input("Nb s2 : "))

temps1 = j1*86400 + h1*3600 + m1*60 + s1
temps2 = j2*86400 + h2*3600 + m2*60 + s2

if temps1 > temps2 :
	secondes = temps1-temps2
else :
	secondes = temps2 - temps1


nbJours = secondes // 86400
nbHeures = secondes %86400 // 3600
nbMinutes = secondes %86400%3600//60
nbSecondes = secondes %86400%3600%60%60

print(nbJours," jours ",nbHeures," heures",nbMinutes," minutes ",nbSecondes," secondes")
input("Appuyez sur Enter")
