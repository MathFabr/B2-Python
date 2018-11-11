#!/usr/bin/python3.6


import os
import re
import signal
import sys

from random import randrange
from time import sleep

##########################################################################################

random_number = randrange(1,100)
pattern = re.compile('^[0-9]*$')
nbr = 0
sortie = "q"
old_nbr = "a"

#########################################################################################

def youcant(sig, frame):#Message a afficher en "ctrl+C"
    print("Aurevoir, merci d'avoir jouer, la réponse était: " + str(random_number))
    sys.exit(0)


def writeToFile (message): #Ecrire dans le fichier
    f = open("jeu.txt","w")
    f.write(message)
    f.close()

def readToFile ():#Lire le fichier
    f=open("jeu.txt","r")
    proposition = f.read()
    f.close()
    return proposition

#############################################################################################

signal.signal(signal.SIGINT, youcant)

print("Pour commencer à jouer rdv dans le fichier jeu.txt")

writeToFile("Bonjour, bienvenue dans le jeu du plus ou moins, pour commencer effacer le contenue du fichier afin d entrer votre proposition \n Le nombre a trouver se situe entre 0 et 100")

sleep(10)

nbr = old_nbr

while (nbr != random_number or nbr !=sortie) :
  nbr = readToFile()
  

  if nbr == old_nbr :
     sleep(1)   
     continue

  nbr = old_nbr

  if (nbr == sortie):
      random_number = (str(random_number))
      writeToFile("Merci d'avoir jouer, la reponse etait: "+ random_number)
      sys.exit(0)

  
  if pattern.match(nbr):
     nbr=(int(nbr))
     if (nbr<random_number):
       writeToFile("Le nombre à trouver ets plus grand")
     elif (nbr>random_number):
       writeToFile("Le nombre à trouver est plus petit")
     else:
       writeToFile("Vous avez trouver la bonne réponse")
       sys.exit(0)
  else:
       writeToFile("erreur, vous n'avez pas rentré des chiffres")