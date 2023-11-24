
# Opgave 1: appel valt van de de Dom

import numpy as np

# Grootheden:
tmax = 20 # Maximale hoeveelheid tijd in seconden
dt = 0.01 # Stapgrootte in tijd

M =  5.9722 * 10**24  # Massa Aarde (kg)  
m = 1 # Massa Appel (kg) 
r = 6378000 # Straal Aarde (m) 
G = 6.6742 * 10**(-11) # Gravitatie constante(N*m^2/kg^2)
x = (r + 100) # Hoogte van de appel vanaf centrum van de aarde
v = 0 # Begin snelheid
a = 0 # Begin versnelling
teller = 0

for t in np.arange(0,tmax,dt):    
    Fz = (G * m * M) / x**2
    a = - Fz / m
    v = v + a * dt # v nieuw
    x = x + v * dt # x nieuw
    h = x - r # h nieuw
    vkmh = v * 3.6
    if v <= - 100/3.6 and teller == 0:
        print "De appel heeft na %f seconden een snelheid van 100 km/h." % (t)
        teller = teller + 1
    if h <= 0:
        print "De appel raakt op t = %f s de grond." % (t)
        print "De appel raakt de grond met een snelheid van %f km/h." % (vkmh) 
        break

    
    
    
    