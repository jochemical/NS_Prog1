
# Opgave 1: animatie van spiraliserende stip (de andere beginoefeningen staan onderaan)

import math
import numpy as np
import matplotlib.pyplot as plt

L_x = []
L_y = []

# Programma Spiraal
for a in np.arange(0, 20, 0.1):
    R = 10 - 0.5 * a # Waarde van de straal afhankelijk van hoek a
    y = R * math.sin(a)
    x = R * math.cos(a)
    
    L_x.append(x)
    L_y.append(y)
    
    # Grafiek plotten:
    plt.plot(L_x, L_y, 'bo', markersize = 10) # blauwe stip
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.draw() # Update grafiek
    plt.pause(0.001)





# Visualisaties en animaties (De oefenopgaves voordat de spiraalopdracht begon)

L_x = []
L_x2 = []
L_sinx = []
L_cosx = []

for x in np.arange(0., 2*math.pi, 0.01):
    L_x.append(x)
    L_x2.append(x*x)
    L_sinx.append(math.sin(x))
    L_cosx.append(math.cos(x))
# Gemeenschappelijk figuur (bevat beide sub-figuren)

plt.figure(1)

plt.subplot(121) # Subplot 1
plt.plot(L_x, L_sinx, 'b', L_x, L_cosx,'r--')
plt.subplot(122) # Subplot 2
plt.plot(L_x, L_x2, 'g-') # Plot beide grafieken
plt.show()


# Animaties

# Een bewegend punt

# 0.05 stappen in x tussen 0 en 2pi
for x in np.arange(0,2*math.pi, 0.05):    
    y = math.sin(x)
    # Plot grafiek
    plt.plot(x, y,'bo', markersize = 10) # Blauwe punt
    plt.xlim(0,2*math.pi)
    plt.ylim(-1,1)
    plt.draw() # Update grafiek
    plt.pause(0.001)
    plt.clf() # Clear grafiek
    
# Een bewegende lijn

L_x = []
L_y = []


for x in np.arange(0,2*math.pi, 0.05):    
    y = math.sin(x)
    L_x.append(x)
    L_y.append(y)    
    # Plot grafiek
    plt.plot(L_x, L_y,'r-') # Rode lijn
    plt.xlim(0,2*math.pi)
    plt.ylim(-1,1)   
    plt.pause(0.001)
    plt.clf() # Clear grafiek
    
# Een stip, een lijn en tekst op het scherm

L_x = []
L_y = []

for x in np.arange(0,2*math.pi, 0.05):
    y = math.sin(x)
    L_x.append(x)
    L_y.append(y)    
    # Plot grafiek
    plt.plot(L_x, L_y,'r-') # Rode lijn
    plt.plot(x, y, 'bo', markersize = 10) # Blauwe stip
    plt.xlim(0,2*math.pi)
    plt.ylim(-1,1)
    plt.text(0.25,-0.8,"(%.2f,%.2f)" % (x,y))
    plt.draw() # Update grafiek
    plt.pause(0.001)
    plt.clf() # Clear grafiek
    

    


