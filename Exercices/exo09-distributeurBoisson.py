stock_coca = 0
stock_eau = 2

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
input("Appuyez sur Enter")