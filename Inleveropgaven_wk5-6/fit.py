
# Fitten van data en foutenbepaling

import math
import matplotlib.pyplot as plt
import numpy as np


# Lijst met x, y, o(sigma), en chi^2 waarden:
Lijst_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lijst met x-waarden
Lijst_y = [55, 50, 39, 58, 54, 57, 78, 66, 62, 82] # Lijst met y-waarden
Lijst_o = [5, 4, 9, 4, 5, 5, 7, 3, 6, 6] # Lijst met sigma-waarden
Lijst_X2 = [] # Lijst met chi^2-waarden
Lijst_o2 = [] # Lijst met o waarden vermenigdvuldigd met factor 2

# Lijst_o2 vullen met o2-waarden:
for o in Lijst_o:
    o2 = o * 2
    Lijst_o2.append(o2)

# Lijst_X2 vullen met chi^2-waarden voor verschillende waarden van c:

X2 = 0 # Om chi^2 te berekenen wordt deze eerst op 0 gezet (omdat we te maken hebben met een optelsom)
dc = 0.1 # Stapgrootte voor c-waarden
cbegin = 0
ceind = 82

for c in np.arange(cbegin, ceind, dc):
    for i in np.arange(0, 10, 1): # i wordt gebruikt als rangorde getal in de lijsten y en o.
        componentX = ((float(Lijst_y[i]) - c) / Lijst_o[i])**2
        X2 = X2 + componentX # De uiteindelijke X2 voor een bepaalde c is de som van alle deelsommen/componenten
    Lijst_X2.append(X2)
    X2 = 0 # Voor iedere c-waarde moet de X2-waarde weer op 0 worden gezet.


# Minimum berekenen voor X2(chi^2):

l = len(Lijst_X2) # De lengte van de lijst wordt aangegeven met variabele 'l'.
X2min = Lijst_X2[0] # Omdat er sprake is van een dalparabool kan als hoogste waarde de eerste chi-waarde uit de lijst worden genomen.

for c2 in np.arange(0, l-1, 1): # c2-waarden zijn nog geen c-waarden maar rangorde getallen. Er geldt c2 = c / dc - cbegin.
    X2_2 = Lijst_X2[c2] # X2_2 zijn de chi^2-waarden(dit keer met X2_2 aangegeven om verwarring met eerdere variabelen te voorkomen.
    if X2_2 < X2min: # De minimum waarde voor chi^2 wordt uitgerekend.
        X2min = X2_2 # De minimum waarde voor chi^2 wordt onthouden.
        c2min = c2 # De bijbehorende c2 waarde wordt onthouden
        
# De onzekerheid op c berekenen

cmindc2 = 0
teller = 0

for c3 in np.arange(1, l-1, 1): # Let op: Ook voor deze c-waarde geldt c3 = c / dc - cbegin
    X2_3 = Lijst_X2[c3] # X2_3 zijn de chi^2-waarden dit keer aangegeven met X2_3 om verwarring met eerdere variabelen te voorkomen. 
    if X2_3 < (X2min + 1) and teller == 0:
        teller = teller + 1 # Er wordt een teller bijgehouden omdat dit punt maar een keer onthouden moet worden.
        c2mindc2 = c3 # De bijbehorende c3 wordt onthouden 
        dc2 = (c2min - c2mindc2) * dc # dc2 is de waarde tussen de c-waarde waarvoor geldt chi^2 = minimaal, en de c-waarde waarvoor geldt chi^2 = minimaal + 1
        # dc2 is tevens aangegeven met een 2 om verwarring te verkomen met de eerdere dc voor de stapgrootte van c.
        # De verschilwaarde moet worden vermenigdvuldigt met dc omdat de Lijst_X2 gebaseerd is op c waarden met stapgrootte dc.
        break        
                
c_X2min = c2min * dc + cbegin # De c-waarde waarvoor geldt chi^2 = minimaal wordt ook berekend door de schaal te corrigeren (cbegin = 0)
print "De minmale X^2-waarde is %f." % (X2min)
print "De c-waarde waarbij X^2 minimaal is is c=%f." % (c_X2min)
print "De onzekerheid van c is +/-%f." % (dc2)

# Grafiek plotten:
plt.figure()
plt.errorbar(Lijst_x, Lijst_y, yerr=Lijst_o, fmt='o') # fmt = 'o' geeft de opdracht om blauwe stipjes te plotten.
plt.xlim(0, 11)
plt.ylim(0, 100)
plt.show()

# Als binnen dit programma op de regels 69 en 30 de Lijst_o vervangen wordt door Lijst-o2, dan zal:
# -De minimale X^2-waarde is 9.718348.
# -De c-waarde waarbij X^2 minimaal is is c=60.300000.
# -De onzekerheid van c is +/-3.000000.



