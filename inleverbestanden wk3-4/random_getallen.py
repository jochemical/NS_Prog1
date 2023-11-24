# Random getallen en datavisualisatie

print "oefeningen:"
import random
x = random.random()
print x

import random
for i in range(1,11):
    x = random.random()
    print x

import random
for i in range(1,11):
    x = random.random()
    y = 2 * x
    print y


# Opgave 1

import random

def MijnRandomGetal(a,b):
    verschil = b - a 
    randomdelta = verschil * random.random()
    getal = a + randomdelta 
    return getal
    
#-- hier begint het programma
print
print "Een rij randomgetallen tussen a en b:"
a = 2
b = 5
for i in range(1,11):
    x = MijnRandomGetal(a,b)
    print x  
 
 
# Opgave 2  
 
import random
import math

# Vierkant:
N = 10000

x = 1
y = 1

def Vierkant (a,b,c,d):    
    diagonaal = math.sqrt((c - a)**2 + (d - b)**2)
    return diagonaal

som = 0
for i in range (0,N):
    x1 = random.random() * x
    y1 = random.random() * y
    x2 = random.random() * x
    y2 = random.random() * y
    afstand = Vierkant(x1, y1, x2, y2)
    som = som + afstand   

gemiddelde = som / N
print
print "De gemiddelde afstand tussen twee random punten in het vierkant is %f" % (gemiddelde)


# Opgave 3

import random
import matplotlib.pyplot as plt

#lijst random getallen
random_getallen = []
# genereren van 10.000 random getallen
n = 10000
for getal in range(0,n):
      getal = random.random()
      random_getallen.append(getal)  
      
#frequentie-distributie plotten
plt.xlim(-0.1, 1.1)
plt.hist(random_getallen,bins=50)
plt.show()

    
import random
import matplotlib.pyplot as plt

LijstSomRandom = []
for T in range (0, 10000):
    optelsom = 0
    for i in range (0, 100):
        a = random.random()
        optelsom = optelsom + a
    LijstSomRandom.append(optelsom)
print
print "LijstSomRandom:"
print LijstSomRandom

#frequentie-distributie plotten
plt.xlim(30, 70)
plt.hist(LijstSomRandom,bins=40)
plt.show()

teller40 = 0
teller60 = 0
for getal in LijstSomRandom:
    if getal < 40:
        teller40 = teller40 + 1
    if getal > 60:
        teller60 = teller60 + 1
l = len(LijstSomRandom)
procent40 = (float(teller40) / l) * 100 
procent60 = (float(teller60) / l) * 100    
print "Het percentage getallen onder de 40 is %f" % (procent40)      
print "Het percentage getallen boven de 60 is %f" % (procent60)       
          
              
    