
# Opgave 4a: Angry Birds

import math
import matplotlib.pyplot as plt
import numpy as np 

# Invoervariabelen
tmax = 20 # Maximale hoeveelheid tijd in seconden
dt = 0.1 # Stapgrootte in tijd

x = 0
h = 20 # Begin hoogte
v = 3 # Afvuursnelheid in m/s
alpha = 30 # Hoek alpha in graden
animatie = 1 # De vraag of er een animatie getoond moet worden: 1 = ja; 0 = nee.

# Constanten
M =  5.9722 * 10**24  # Massa Aarde (kg)  
m = 0.001 # Massa Angry bird (kg) 
r = 6378000 # Straal Aarde (m) 
G = 6.6742 * 10**(-11) # Gravitatie constante(N*m^2/kg^2)

# Systeemvariabelen
rad = (float(alpha) / 360) * 2 * math.pi
y = r + h # Hoogte van de appel vanaf centrum van de aarde
vx = v * math.cos(rad) # begin snelheid in de x-richting
vy = v * math.sin(rad) # begin snelheid in de y richting


# Lijsten voor de Grafieken (niet noodzakelijk voor de animatie):
Lijst_t = [] # Lijst voor de tijdwaarden
Lijst_x = [] # Lijst met x-waarden
Lijst_h = [] # Lijst met h-waarden
# Lijst_v = [] # Lijst met v-waarden

for t in np.arange(0,tmax,dt): 
    Lijst_t.append(t)
    # Verplaatsing in de y-richting
    Fz = (G * m * M) / y**2
    a = - Fz / m
    vy = vy + a * dt # v nieuw
    h = h + vy * dt # h nieuw
    Lijst_h.append(h)
    if h <= 0:
        vy = -1 * vy
    #vkmh = v * 3.6
    #Lijst_v.append(vkmh)
    # Verplaatsing in de x-richting:
    x = x + vx * dt # x nieuw
    Lijst_x.append(x)
    
# Grafieken plotten:        
    if animatie == 1:
        plt.show() 
        #plt.plot(Lijst_x, Lijst_h,'r-') # Rode lijn
        plt.plot(x, h, 'bo', markersize = 10) # Grafiek van de positie van de angry bird
        plt.xlim(0,20)
        plt.ylim(0,40)
        plt.draw() # Update grafiek
        plt.pause(0.001)
        plt.clf() # Clear grafiek
        

# Opgave 4b: Angry Birds

# Invoervariabelen:

tmax = 200 # Maximale hoeveelheid tijd in seconden
dt = 0.01 # Stapgrootte in tijd
x = 0
h = 20
v = 16 # Afvuursnelheid in m/s
animatie = 0 # De vraag of er een animatie getoond moet worden: 1 = ja; 0 = nee.


# Constanten:
M =  5.9722 * 10**24  # Massa Aarde (kg)  
m = 0.001 # Massa Angry bird (kg) 
r = 6378000 # Straal Aarde (m) 
G = 6.6742 * 10**(-11) # Gravitatie constante(N*m^2/kg^2)
y = r + h # Hoogte van de appel vanaf centrum van de aarde


# Functie die test of de druksensor wordt geraakt door de angrybird:
def Angrybird(alpha):
    rad = (float(alpha) / 360) * 2 * math.pi
    v = 16 # Afvuursnelheid in m/s
    vx = v * math.cos(rad) # begin snelheid in de x-richting
    vy = v * math.sin(rad) # begin snelheid in de y richting 
    x = 0
    h = 20
    hfirst = 0
    teller = 0
    hit = 0
    for t in np.arange(0,tmax,dt): 
        # Verplaatsing in de y-richting:
        Fz = (G * m * M) / y**2
        a = - Fz / m
        vy = vy + a * dt     # v nieuw
        h = h + vy * dt     # h nieuw
        if h <= 0:         # Stuiteren
            vy = -1 * vy
        # Verplaatsing in de x-richting:
        x = x + vx * dt # x nieuw
        if x > 18:
            break
        # Grafieken plotten:        
        if animatie == 1: 
            plt.show() 
            plt.plot(x, h, 'bo', markersize = 10) # Grafiek van de positie van de angry bird
            plt.plot([12,14],[20,20],'r-') # Druksensor
            plt.xlim(0,20)
            plt.ylim(0,40)
            plt.draw() # Update grafiek
            plt.pause(0.001)
            plt.clf() # Clear grafiek
        if x > 12 and x < 14:
            if teller == 0:
                teller = teller + 1
                hfirst = hfirst + h # het programma onthoudt de eerste h-waarde in het domein 12 < x < 14.
            if hfirst > 20 and h < 20: # test of de lijn y = 20 wordt gesneden van boven naar beneneden.
                hit = hit + 1
                break
            if hfirst < 20 and h > 20: # test of de lijn y = 20 wordt gesneden van beneden naar boven.
                hit = hit + 1
                break 
    return hit # Als de lijn y = 20 niet wordt gesneden geeft de functie een 0, anders een 1.    


# Test voor welke alpha de druksensor wordt geraakt:                        
Lijst_alpha = []
Lijst_hits = []
for alpha in np.arange(-87, 87, 1):
    Lijst_alpha.append(alpha)
    raaktest = Angrybird(alpha)
    if raaktest == 1:
        print alpha
    Lijst_hits.append(raaktest)

# Grafiek waarin duidelijk wordt voor welke hoeken alpha de druksensor wordt geraakt:
plt.plot(Lijst_alpha, Lijst_hits, 'r-')
plt.show()       
# (druksensor raken geeft een 1, druksensor missen geeft een 0)

# In de grafiek is bv. te zien dat bij een hoek van -66 graden de druksensor wordt geraakt.
# Met de volgende test is dat bv. te zien:
#Angrybird(16)   



