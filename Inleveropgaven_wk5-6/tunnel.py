
# Opgave 3: de ultieme free-fall

import math
import numpy as np
import matplotlib.pyplot as plt

# Grootheden:
tmax = 20000 # Maximale hoeveelheid tijd in seconden
dt = 100 # Stapgrootte in tijd

# Constanten
M =  5.9722 * 10**24  # Massa Aarde (kg)  
m = 1 # Massa Appel (kg) 
r = 6378000 # Straal Aarde (m) 
G = 6.6742 * 10**(-11) # Gravitatie constante(N*m^2/kg^2)

# Variabelen
x = r # Hoogte van de appel vanaf centrum van de aarde
v = 0 # Begin snelheid
a = 0 # Begin versnelling
teller = 0
teller2 = 0

# Lijsten voor de Grafieken:
Lijst_t = [] # Lijst voor de tijdwaarden
Lijst_v = [] # Lijst voor de snelheden
Lijst_x = [] # Lijst voor de hoogten

for t in np.arange(0,tmax,dt): 
    Lijst_t.append(t)
    Meff = M * (x / r)**3 # Effectieve massa van de aarde  
    Fz = (G * m * Meff) / x**2
    a = - Fz / m
    v = v + a * dt # v nieuw
    x = x + v * dt # x nieuw
    Lijst_x.append(x)
    vkmh = v * 3.6
    Lijst_v.append(vkmh)
    # Het printen van de hoogste snelheid van de appel:
    if x <= 0 and teller == 0:
        print "De hoogste snelheid die de appel bereikt is %f km/h." % (vkmh)
        teller = teller + 1
    # Het berekenen van de tijd waarop de appel weer terug is op zijn oude positie:
    if v > 0 and teller2 == 0:
        # Wanneer de snelheid van de appel van richting verandert wordt dit geregistreert.
        teller2 = teller2 + 1 
    if v < 0 and teller2 == 1:
        # Wanneer de snelheid van de appel opnieuw van richting verandert wordt dit geregistreert en de tijd geprint.
        print "Na %f seconden is de appel weer op de plaats waar hij is losgelaten." % (t)
        teller2 = teller2 + 1 # De teller voorkomt dat de  bovenstaande zin meer dan een keer wordt geprint.
        
# Grafieken plotten:        
#plt.plot(Lijst_t, Lijst_v, 'r-') # Grafiek Snelheid als functie van de tijd
plt.plot(Lijst_t, Lijst_x, 'g-') # Grafiek Hoogte als functie van de tijd
#plt.ylim(-6500000,6500000)
plt.show() 

    
