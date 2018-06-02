import random

carac = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789,?;.:/!§ù%*µ^¨$£~é'(-è_çà)@=+" # Listes des caractères
longueur = 10 # MDP a 10 caractères
mdp = "" # Mot de passe
nb_lettres = 0 # Nombre de lettres à 0

while nb_lettres < longueur:
    lettre = carac[random.randint(0, len(carac)-1)] # Un carac sélectionné au hasard
    mdp += lettre # Ajout de la lettre au mdp
    nb_lettres += 1 # On incrémente le nombre de lettres de 1
 
print("Voici votre MDP:", mdp)