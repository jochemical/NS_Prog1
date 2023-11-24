
# Opgave 2: Vrije val van basejumers

import math
import numpy as np
import matplotlib.pyplot as plt

# Tijdvariabelen:
tmax = 200 # Maximale hoeveelheid tijd in seconden
dt = 0.01 # Stapgrootte in tijd
imax = tmax / dt 

# Constanten:
E = 0.24
M = 5.9722 * 10**24  # Massa Aarde (kg)  
m = 72 # Massa Appel (kg) 
r = 6378000 # Straal Aarde (m) 
G = 6.6742 * 10**(-11) # Gravitatie constante(N*m^2/kg^2)

# Variabelen:
x = (r + 828) # Hoogte van de appel vanaf centrum van de aarde
v = 0 # Begin snelheid
a = 0 # Begin versnelling
teller = 0
tellertml = 0

# Lijsten voor de Grafieken:
Lijst_t = [] # Lijst voor de tijdwaarden
Lijst_v = [] # Lijst voor de snelheden
Lijst_h = [] # Lijst voor de hoogten

# Programma voor val met luchtweerstand
for t in np.arange(0,tmax,dt):   
    Lijst_t.append(t) 
    Fz = (G * m * M) / x**2
    Fw = E * v**2
    F = - Fz + Fw
    a = F / m
    v = v + a * dt # v nieuw
    vkmh = v * 3.6
    Lijst_v.append(vkmh)
    x = x + v * dt # x nieuw    
    h = x - r # h nieuw
    Lijst_h.append(h)
    if h <= 100:
        tml = t # De tijd op 100 m hoogte met luchtweerstand
        tellertml = tellertml + 1
    if v <= - 100/3.6 and teller == 0:
        print "De basejumper heeft na %f seconden een snelheid van 100 km/h." % (t)
        teller = teller + 1
    if h <= 0:
        print "De basejumper raakt op t = %f s de grond." % (t)
        print "De basejumper raakt de grond met een snelheid van %f km/h." % (vkmh) 
        break

# Programma voor val zonder luchtweerstand:

# Variabelen 2 (constanten en grootheden veranderen niet):
x2 = (r + 828) # Hoogte van de appel vanaf centrum van de aarde
v2 = 0 # Begin snelheid
a2 = 0 # Begin versnelling
teller2 = 0
tellertzl = 0

# Lijsten voor de Grafieken:
Lijst_t2 = [] # Lijst voor de tijdwaarden
Lijst_h2 = [] # Lijst voor de hoogten

for t2 in np.arange(0,tmax,dt):   
    Lijst_t2.append(t2) 
    Fz2 = (G * m * M) / x2**2   
    a2 = - Fz2 / m
    v2 = v2 + a2 * dt # v nieuw
    vkmh2 = v2 * 3.6
    x2 = x2 + v2 * dt # x nieuw    
    h2 = x2 - r # h nieuw
    Lijst_h2.append(h2)
    if h <= 100:
        tzl = t2 # De tijd op 100 m hoogte met luchtweerstand
        tellertzl = tellertzl + 1
    if v2 <= - 100/3.6 and teller2 == 0:
        print "De basejumper heeft na %f seconden een snelheid van 100 km/h." % (t2)
        teller2 = teller2 + 1
    if h2 <= 0:
        print "De basejumper raakt op t = %f s de grond." % (t2)
        print "De basejumper raakt de grond met een snelheid van %f km/h." % (vkmh2) 
        break                
        
# Grafieken plotten:        
plt.plot(Lijst_t, Lijst_v, 'r-') # Grafiek Snelheid als functie van de tijd
#plt.plot(Lijst_t, Lijst_h, 'g-') # Grafiek Hoogte als functie van de tijd met luchtweerstand
#plt.plot(Lijst_t2, Lijst_h2, 'b-') # Grafiek Hoogte als functie van de tijd zonder luchtweerstand
#plt.ylim(0,1000)
plt.show()    

# Tijdverschil op 100 m tussen met en geen luchtweerstand:
dt100m = tml - tzl
print "Met luchtweerstand duurt de vrije val %f seconden langer." % (dt100m)
    