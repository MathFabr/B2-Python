#!/usr/bin/python3.6

################################################################################################

import os
import re
import signal
import sys

from time import sleep
from random import randrange

###############################################################################################

random_number = randrange(1,100)
pattern = re.compile('^[0-9]*$')
nbr = 0
sortie = "q"
old_nbr = ""

###############################################################################################

def youcant(sig, frame):
    writeToFile("Aurevoir, merci d avoir jouer, la reponse etait: " + str(random_number))
    sys.exit(0)


def writeToFile(message):
      write = open("jeu.txt", "w")
      write.write(message)
      write.close()

def readToFile():
      read = open("jeu.txt", "r")
      proposition = read.read()
      read.close()
      return proposition

###############################################################################################

signal.signal(signal.SIGINT, youcant)

writeToFile("Bonjour et bienvenu dans le jeu du plus ou moins, vous devez trouver une valeurs entre 0 et 100, allez y, proposer. \n (Effacer la ligne et ecriver juste votre nombre a la place)") 



while (nbr != random_number or nbr !=sortie) :
 
  nbr = readToFile()

  if nbr != old_nbr:
        continue
  else:      

      old_nbr = nbr

      print(nbr)





      if (nbr == sortie):#si on mets un "q"
            random_number = (str(random_number))
            
            writeToFile("Merci d avoir tente votre chance, la reponse etait: " + random_number)
            
            sys.exit(0)






      if pattern.match(nbr):#si on as bien entré un nombre
            nbr=(int(nbr))
            if (nbr<random_number):
                        print("Le nombre à trouver est plus grand")
            elif (nbr>random_number):
                        print("Le nombre à trouver est plus petit")
            else:
                  print("Vous avez trouver la réponse!!")
                  sys.exit(0)
      else:
                  print("erreur, vous n'avez pas rentré des chiffres")