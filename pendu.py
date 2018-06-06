import random
import time
import os

# Incomplet car je n'y arrive pas, maybe un jour il le sera

nombre_coups = 0
score = 0
minuscules = "abcdefghijqlmnopqrstuvwz"
lettre_trouve = []
game = True
liste_mots = ["potiron", "carotte", "quenelle"]
mot = random.choice(liste_mots)
etoile = "*"

nom_joueur = input("Entrez votre nom: ")

time.sleep(1)

os.system('cls')

menu = input("""Bienvenue sur le jeu du Pendu.

{}, Que veux-tu faire ?
1- Jouer
2- Score joueur
3- Quitter
""".format(nom_joueur))

while nombre_coups < 10:

	if menu == "1":
		os.system('cls')
		print("Début de la partie.")

		while game == True:

			pendu = input("\nEntrez une lettre s'il vous plaît: \n")
			nombre_coups += 1

			os.system('cls')

			if etoile == 0:
				print("Vous avez gagné")

			if len(pendu) != 1 or pendu not in minuscules:
				print("Veuillez entrer Une seule lettre en minuscule s'il vous plaît")

			for lettre in mot:

				if lettre in lettre_trouve:
					print("{}".format(lettre), end="")
				else: 
					print("*", end="")

			lettre_trouve.append(pendu)

	elif menu == "2":
		print("{}, votre score est de {} points".format(nom_joueur, score))
		continue

	elif menu == "3":
		print("A bientôt")
		break
if nombre_coups == 10:
	print("Vous avez perdu")