import random
import time

game = True
objets = 0 # On commence avec 0 objets

while game == True: # Tant que le jeu est "vrai"
	pecher = input("""Que voulez vous faire ?

1- Pêcher
2- Inventaire
3- Quitter

> """)

	if pecher == "1":
		reply = ["une canette", "une poisson", "un poisson rare", "une chaussure", "une algue", "une chaussette", "la tristesse"]
		elements = random.choice(reply) # Permet de piocher un objet aléatoirement dans la liste ci dessus.

		time.sleep(1)

		print("Vous avez pêché {} !".format(elements))
		objets += 1

		time.sleep(0.3)
		continue
		
	if pecher == "2":
		time.sleep(1)
		print("Vous avez {} objets dans votre inventaire.".format(objets))

		time.sleep(0.3)
		continue
		
	
	if pecher == "3":
		time.sleep(0.3)
		print("Vous avez terminé la partie avec {}. A bientôt".format(objets))

		game = False # Fin du jeu.