secondes = 4561
nbJours = secondes // 86400
nbHeures = secondes %86400 // 3600
nbMinutes = secondes %86400%3600//60
nbSecondes = secondes %86400%3600%60%60

print(nbJours," jours ",nbHeures," heures",nbMinutes," minutes ",nbSecondes," secondes")

input("Appuyez sur Enter")

