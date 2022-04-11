# Projet : juste_prix
# • Améliorez encore le juste_prix : l'utilisateur a droit à 10 essais après ces 10 essais, il a perdu.
# • L'ordinateur affiche le juste_prix
# • Ajouter un niveau :
# – facile : entre 1 et 10
# – moyen : entre 1 et 100
# – difficile : entre 1 et 1000
# • Tant que la personne veut rejouer, redemandez le niveau et générez un
# nombre.
# • Vérifiez que tout caractère entré est correct, c'est-à-dire pour que le
# programme ne plante jamais.

# Imports
from random import randint
from os import system

# Déclaration & initialisation
MAX_ATTEMPS = 10
play_again = True

while play_again:
  attemps = 0

  # -- Menu

  system("cls")
  choice = 0

  while choice != "1" and choice != "2" and choice != "3":
    print("~ Juste Prix ~")
    print("1. Facile : Entre 1 et 10")
    print("2. Moyen : Entre 1 et 100")
    print("3. Difficile : Entre 1 et 1000")

    choice = input("Choisissez un niveau : ")

  # -- Choix du niveau
  if choice == "1":
    print('Facile')
    level = 10

  elif choice == "2":
    print('Moyen')
    level = 100
    
  else:
    print('Difficile')
    level = 1000

  price = randint(1, level)

  print("Le juste prix à deviner est :", price)

  # -- Propositions
  proposal = 0
  while proposal != price and attemps < MAX_ATTEMPS:

    # Vérification de la validité de la proposition
    isValid = False
    while not isValid:
      proposal = input("Entrez une proposition : ")
      while not proposal.isdigit():
        proposal = input("Proposition incorrecte, entrez un nombre entier : ")
      
      proposal = int(proposal)

      if 1 <= proposal <= level:
        isValid = True
      else:
        print("Vous devez entrez un nombre entre 1 et", level)

    attemps += 1
    # attemps = attemps + 1

    if proposal != price:
      if proposal < price: print("C'est plus.")
      else: print("C'est moins.")

  if proposal == price:
    print("C'est gagné en", attemps, "tentative(s).")
  else:
    print("Vous avez perdu, le juste prix était : ", price)

  play_again = input("Voulez-vous rejouer ? (oui / non) : ").lower() == 'oui'
  