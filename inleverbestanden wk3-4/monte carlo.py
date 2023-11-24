# Monte Carlo

import numpy as np # numpy module is nodig voor arange-functie
import math # math module is o.a. nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafieken
import random # random module is nodig voor de random-functie
import matplotlib.pyplot as plt


# Opgave 7
print "Opgave 7:"

# Rechthoek maken:
xmin = 0
xmax = 1
ymin = 0
ymax = 1
dx = xmax - xmin
dy = ymax - ymin


# Lijsten met x respectievelijk y -waarden opstellen:

L_x = []
L_y = []
d = 0.01
for x in np.arange(0, 1+d, d):  
    y = x**x
    L_y.append(y)
    L_x.append(x)
imax=len(L_y)


# Random punten bombarderen in het vierkant en tellen welke er binnen de integraal vallen

n = 1000
teller = 0
for i in range(0,n):
    randomx = xmin + random.random() * dx
    randomy = ymin + random.random() * dy
    y2 = randomx ** randomx
    if y2 >= randomy:
        teller = teller + 1

# De integraalbenadering berekenen
fgoed = float(teller) / n
integraal = fgoed * (xmax - xmin) * (ymax - ymin)
print "De integraalbenadering van x^x in het domein 0 tot 1 is %f." % (integraal)


# Opgave 8
print "Opgave 8:"

import numpy as np # numpy module is nodig voor arange-functie
import math # math module is o.a. nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafieken
import random
import matplotlib.pyplot as plt


# Rechthoek maken:
xmin = 0.1
xmax = 2
ymin = 0
ymax = 1
dx = xmax - xmin
dy = ymax - ymin


# Random punten bombarderen in het vierkant en tellen welke er binnen de integraal vallen
n = 100000
teller = 0
for i in range(0,n):
    randomx = xmin + random.random() * dx
    randomy = ymin + random.random() * dy
    y2 = math.sin(randomx)
    if abs(y2) >= abs(randomy):
        teller = teller + 1

# De integraalbenadering berekenen
fgoed = float(teller) / n
integraal = fgoed * (xmax-xmin) * (ymax-ymin)
print "De integraalbenadering van sin(x) in het domein 0.1 tot 2 is %f." % (integraal)


# Opgave 9
print "Opgave 9:"

import numpy as np # numpy module is nodig voor arange-functie
import math # math module is o.a. nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafieken
import random

# Rechthoek maken:
xmin = 0
xmax = math.pi
ymin = -1
ymax = 1
dx = xmax - xmin
dy = ymax - ymin


# Random punten bombarderen in het vierkant en tellen welke er binnen de integraal vallen
n = 100000
tellerpos = 0
tellerneg = 0
for i in range(0,n):
    randomx = xmin + (random.random() * dx)
    randomy = ymin + (random.random() * dy)
    y2 = math.sin(randomx ** 2)
    signtest = y2 / randomy
    if signtest >= 0 and y2 > 0:
        if abs(y2) >= abs(randomy):
            tellerpos = tellerpos + 1
    if signtest >= 0 and y2 < 0:
        if abs(y2) >= abs(randomy):
            tellerneg = tellerneg + 1

# De integraalbenadering berekenen                                            
teller = tellerpos - tellerneg       
fgoed = float(teller) / n
integraal = fgoed * dx * dy
print "De integraalbenadering van sin(x^2) in het domein 0 tot pi is %f." % (integraal)


# Opgave 10: het Twitter-ei
print "Opgave 10:"
print "Zie grafiek 1 en 2"

import numpy as np # numpy module is nodig voor arange-functie
import math # math module is o.a. nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafieken
import random # random is nodig voor de random-functie


# Rechthoek maken voor de integraal benadering:
xmin = -0.5
xmax = 0.5
ymin = -0.5
ymax = 1
dx = xmax - xmin
dy = ymax - ymin

# lijst die de hoeveelheid punten opslaat in honderdtallen:
lijst_p = []
# lijst van de intergraal benaderingen per honderdtal punten:
lijst_integraal = []

# aantal punten p = n x 100 (let op met de hoeveelheid!):
n = 100
teller = 0

# Random punten bombarderen in het vierkant en tellen welke er binnen de integraal vallen
for i in range(1,n+1):
    for j in range(0,100):
        x = xmin + random.random() * dx
        y = ymin + random.random() * dy
        test = math.sqrt(x**2 + y**2) + (float(2)/3) * math.sqrt(x**2 + ((float(5)/6) - y)**2)
        # Hier wordt het ei geplot (grafiek 1):
        if test > 1:
            plt.plot(x,y,'bo')
        # met de teller wordt later de integraal berekend:
        if test < 1:
            teller = teller + 1
    # Om de honderd punten wordt de integraal berekend en in lijst gezet. 
    # Ook de p-waarde wordt in een lijst gezet.
    fgoedtussen = (float(teller) / (100 * i)) * dy * dx
    lijst_integraal.append(fgoedtussen)
    lijst_p.append(100 * i)
     
# De volgende grafiek (2) beschrijft de benadering van de integraal als functie van het aantal punten:
plt.plot(lijst_p, lijst_integraal, 'b-')
plt.show()
# Let op: Bij het plotten worden de twee grafiek door elkaar geplot waardoor de grafiek onduidelijk wordt.
# Om de grafieken goed te zien moet een van de twee grafieken niet worden geplot.

