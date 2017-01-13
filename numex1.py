from math import *
print ("Equation du second degré")
a= int(input ("la valeur de a "))
b= int(input ("la valeur de b "))
c= int(input ("la valeur de c "))
delta = b*b -4*a*c
print (delta)
if delta <0:
    print ("pas de racines")
elif delta==0:
    print ("racine double ", -b/2*a)
elif delta >0:
   x1 =(-b + sqrt(delta))/2*a
   x2 =(-b - sqrt(delta))/2*a
   print ("les deux réponses sont: ",x1, "et ",x2)

"""   
   Il faut bien préciser pour que le programme fonctionne
   qu'il faut charger la bibliothèque mathématique:
   from math import *
"""