from random import *
lancer, pile, face = 0, 0, 0
for loop in range(10):
    lancer = randint(0,1)
    if lancer == 0:
        pile = pile + 1
    else:
        face = face + 1
print("Nombre de pile = {} ; nombre de face = {}".format(pile, face))