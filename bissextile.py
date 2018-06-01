# Programme testant si une année saisie est bissextile ou non

import os

annee = input("Saisissez une année : ") # On attend qu'une année à tester soit fournit

annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre


if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):

    print("L'année saisie est bissextile.")

else:

    print("L'année saisie n'est pas bissextile.")
	
os.system("pause")