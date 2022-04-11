stock_balles = 3
while (stock_balles > 0) :
	pret = bool(int(input("Etes-vous prêt ? 1 = oui / 0 = non ")))
	if pret  :
		print("Lancer balle")
		stock_balles -= 1
	else : 	
		print("Ne pas lancer balle")

print("Il n'y a plus de balles, partie terminée")

input("Appuyez sur Enter")