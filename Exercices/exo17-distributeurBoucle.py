stock_coca = 0
stock_eau = 2
desire_boire = True

while desire_boire :
	print("Choisissez votre boisson. 1 : coca / 2 : eau ")
	choix = int(input("Mon choix : "))
	if choix == 1:
		if stock_coca > 0:
			print("Voici votre coca")
			stock_coca-=1
		else:
			print("Il n'y a plus de coca")
	elif choix == 2:
		if stock_eau > 0:
			print("Voici votre eau")
			stock_eau-=1
		else:
			print("Il n'y a plus d'eau")
	desire_boire = bool(int(input("Voulez-vous une autre boisson ? 1: oui / 0 : non")))

input("Appuyez sur Enter")