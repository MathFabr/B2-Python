#!/usr/bin/python3.6


import re
import sys

liste = []
sortie = "a"
pattern = re.compile('^[A-z]*$')




while sortie != "q":
  sortie = input("Entrer un prénom: ")
  if pattern.match(sortie):
   if sortie != "q": 
    liste.append(sortie)
    liste.sort()
    print(liste)
   else:
    print("Merci de votre visite, à bientôt")
    sys.exit(0)
  else:
   print("Vous n'avez pas saisie un vrai prénom")

