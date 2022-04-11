pret = bool(int(input("Etes-vous prêt ? 1 = oui / 0 = non ")))
panier_vide = bool(int(input("Le panier est-il vide ?  1 = oui / 0 = non ")))
if pret and not panier_vide :
	print("Lancer balle")
else : 
	print("Ne pas lancer balle")
input("Appuyez sur Enter")
