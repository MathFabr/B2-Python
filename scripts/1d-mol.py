#!/usr/bin/python3.6


import os
import re

from random import randrange
r = randrange(1,100)
pattern = re.compile('^[0-9]*$')
nbr = 0
sortie = "q"


 
while (nbr != r or nbr !=sortie) :
  nbr = input("Entrer une valeurs entre 0 et 100: ")

  if (nbr == sortie):
      r = (str(r))
      print("Merci d'avoir tenté votre chance, la réponse était: " + r)

  else:
      if pattern.match(nbr):
        nbr=(int(nbr))

        if (nbr<r):
          print("Le nombre à trouver est plus grand")
        elif (nbr>r):
            print("Le nombre à trouver est plus petit")
        else:
            print("Vous avez trouver la réponse!!")
      else:
        print("erreur, vous n'avez pas rentré des chiffres")
 


 
