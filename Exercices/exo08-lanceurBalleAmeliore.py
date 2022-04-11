pret = bool(int(input("Etes-vous prêt ? 1 = oui / 0 = non ")))
panier_vide = bool(int(input("Le panier est-il vide ?  1 = oui / 0 = non ")))
if pret and not panier_vide :
	print("Lancer balle")
else : 	
	print("Ne pas lancer balle")
	if not pret :
		print("Vous n'êtes pas prêt")
	if panier_vide :
		print("Le panier est vide")
input("Appuyez sur Enter")