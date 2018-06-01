import os
import time
from random import randrange
from math import ceil

money = 1000 # On démarre avec 1000$
game = True # La partie démarre et ne s'arrête pas tant que pas en False

print("Vous avez à votre disposition", money, "$.")

# On établit les mises
while game:
	nombre_mise = -1
	while nombre_mise < 0 or nombre_mise > 49:
		nombre_mise = input("Tapez le nombre sur lequel vous souhaitez miser (entre 0 et 49) :")
		try:
			nombre_mise = int(nombre_mise)
		except ValueError:
			print("Vous n'avez pas saisi de nombre, saisissez un nombre s'il vous plaît")
			nombre_mise = -1
			continue
		if nombre_mise < 0:
			print("Ce nombre est négatif")
		if nombre_mise > 49:
			print ("ce nombre est supérieur à 49")
			
# Sélection de la somme à miser
	mise = 0
	while mise <= 0 or mise > money:
		mise = input("Tapez le montant de votre mise: ")
		#On Convertit la mise
		try:
			mise = int(mise)
		except ValueError:
			print("Vous n'avez pas saisi de nombre, saisissez un nombre s'il vous plaît")
			mise = -1
			continue
		if mise <= 0:
			print("La mise saisie ne peux pas être inférieure à 0")
		if mise > money:
			print ("vous ne pouvez pas miser autant, vous ne possédez que", money, "$")
		
	numero_gagnant = randrange(50)
	print("La roulette tourne...")
	time.sleep(1)
	print("Et s'arrête sur...", numero_gagnant)
	time.sleep(1)
	

# On établit le gain du joueur
	if numero_gagnant == nombre_mise:
		print("Félicitations, vous obtenez", mise * 3, "$ !")
		money += mise * 3
	elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
		mise = ceil(mise * 0.5)
		print("Vous avez misé sur la bonne couleur, vous obtenez", mise, "$ !")
		money += mise
	else:
		print("Vous perdez votre mise.")
		money -= mise
	
# On arrête la partie si le joueur n'a plus d'money.
	if money <= 0:
		print("Vous n'avez plus d'argent, la partie s'arrête !")
		game = False
	else:
		# On affiche l'money du joueur
		print("vous avez à présent", money, "$")
		quitter = input("Souhaitez-vous quitter le casino (o/n) ?" )
		if quitter == "o" or quitter == "O":
			print("Vous quittez le casino avec vos gains.")
			game = False # La partie s'arrête
		
os.system("pause")