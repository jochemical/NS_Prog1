
# Opgave 2: De Dronken Student

import math
import numpy as np
import matplotlib.pyplot as plt
import random

# Lijsten voor x- en y-waarden van beide studenten
L_x1 = []
L_y1 = []
L_x2 = []
L_y2 = []

# Positie dronken student 1:
x1 = 0
y1 = 0

# Positie dronken student 2:
x2 = 0
y2 = 0 

# Stapgrootte van beide studenten:
R = 1

# Aantal stappen
imax = 200

for i in np.arange(0, imax):
    
    # Verplaatsting dronken student 1:
    a1 = random.random() * 2 * math.pi
    dx1 = R * math.cos(a1)
    dy1 = R * math.sin(a1)
    x1 = x1 + dx1
    y1 = y1 + dy1
    L_x1.append(x1)
    L_y1.append(y1)
      
    # Verplaatsing dronken student 2:
    a2 = random.random() * 2 * math.pi
    dx2 = R * math.cos(a2)
    dy2 = R * math.sin(a2)
    x2 = x2 + dx2
    y2 = y2 + dy2
    L_x2.append(x2)
    L_y2.append(y2)
    
    # Dronken student 1 plotten:
    plt.plot(L_x1, L_y1,'b-') # Blauwe lijn
    plt.plot(x1, y1, 'bo', markersize = 10) # Dronken student 1 - blauwe stip
    
    # Dronken student 2 plotten:
    plt.plot(L_x2, L_y2,'g-') # Groene lijn
    plt.plot(x2, y2, 'go', markersize = 10) # Dronken student 2 - groene stip
    
    # De lijn plotten tussen de 2 studenten
    plt.plot([x1,x2], [y1,y2] ,'y-') # Gele lijn
    
    # Grafiek plotten:
    plt.xlim(-15,15)
    plt.ylim(-15,15)
    plt.text(-14,-14,"step %d/%d" % (i,imax)) # Het plotten van het aantal stappen
    plt.draw() # Update grafiek
    plt.pause(0.001)
    plt.clf() # Clear grafiek
    
    
    
    
    