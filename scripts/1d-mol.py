#!/usr/bin/python3.6


import os
import re
import signal
import sys

from random import randrange


random_number = randrange(1,100)
pattern = re.compile('^[0-9]*$')
nbr = 0
sortie = "q"

def youcant(sig, frame):
    print("Aurevoir, merci d'avoir jouer, la réponse était: " + str(random_number))
    sys.exit(0)


signal.signal(signal.SIGINT, youcant)


while (nbr != random_number or nbr !=sortie) :
  nbr = input("Entrer une valeurs entre 0 et 100: ")
  
  if (nbr == sortie):
      random_number = (str(random_number))
      print("Merci d'avoir tenté votre chance, la réponse était: " + r)

  else:
      if pattern.match(nbr):
        nbr=(int(nbr))

        if (nbr<random_number):
          print("Le nombre à trouver est plus grand")
        elif (nbr>random_number):
            print("Le nombre à trouver est plus petit")
        else:
            print("Vous avez trouver la réponse!!")
      else:
        print("erreur, vous n'avez pas rentré des chiffres")
 


 
