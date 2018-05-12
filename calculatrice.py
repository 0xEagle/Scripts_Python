calcul = input("Que voulez vous calculer ? Addition, Soustraction, Multiplication ou Division ? ")

if calcul == "Soustraction":
	nb1 = int(input("Nombre a: "))
	nb2 = int(input("Nombre b: "))
	print("Resultat: ", nb1-nb2)
	
if calcul == "Addition":
	nb1 = int(input("Nombre a: "))
	nb2 = int(input("Nombre b: "))
	print("Resultat: ", nb1+nb2)
	
if calcul == "Multiplication":
	nb1 = int(input("Nombre a: "))
	nb2 = int(input("Nombre b: "))
	print("Resultat: ", nb1*nb2)
	
if calcul == "Division":
	nb1 = int(input("Nombre a: "))
	nb2 = int(input("Nombre b: "))
	print("Resultat: ", nb1/nb2)