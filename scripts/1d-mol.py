#!/usr/bin/python3.6


import os
import re

from random import randrange
r = randrange(1,100)
pattern = re.compile('^[0-9]*$')
nbr = 0


 
while (nbr != r) :
  nbr = input("Entrer une valeurs entre 0 et 100: ")
  if pattern.match(nbr):
    nbr=(int(nbr))
  else:
      print("erreur, vous n'avez pas rentré des chiffres")
  if (nbr<r):
          print("Le nombre à trouver est plus grand")
  elif (nbr>r):
            print("Le nombre à trouver est plus petit")
  else:
            print("Vous avez trouver la réponse!!")


 
