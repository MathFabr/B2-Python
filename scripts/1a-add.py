#!/usr/bin/python3.6



#---------------------ADDITION-------------------



#---------------------FONCTION-------------------

def addi(oprnd1, oprnd2):

  import re

  pattern = re.compile('^[0-9]*$')

  if pattern.match(oprnd1):
    if pattern.match(oprnd2):

      oprnd1=(int(oprnd1))
      oprnd2=(int(oprnd2))

      print("Le résultat est: ", oprnd1+oprnd2)
    else:
      print("erreur, vous n'avez pas rentré des chiffres")
  else:
    print("erreur, vous n'avez pas entré des chiffres")




#-------------------------MAIN-------------------------


oprnd1=input("Entrer votre première valeur: ")

oprnd2=input("Entrer votre seconde valeur : ")


addi(oprnd1, oprnd2)