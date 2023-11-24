
import numpy as np # numpy module is nodig voor arange-functie
import math # math module is nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafiek

L_x = [] # lijst met x-waarden
L_y = [] # lijst met y-waarden

# 0 <= x < 1.5, in stapjes van 0.01:
for x in np.arange(0, 1.5, 0.01):    
        y = math.pow(x,x) # berekent de y-waarde voor elke x-waarde
        L_x.append(x)
        L_y.append(y)
        # de x- en y-waarden worden aan de lijsten toegevoegd
        
# plotten van de grafiek:
plt.plot(L_x, L_y, 'b-')
plt.text(1.00, 0.80,"f(x)=x^x", color = 'black', fontsize = 20)
plt.xlabel('x',fontsize = 20)
plt.ylabel('x^x',fontsize = 20)
plt.show()

# minimum bepalen:
ymin=100000000000000000
for y in L_y:
    if y <ymin:
        ymin=y

xmin=0
for x in L_x:
    if math.pow(x,x)==ymin:
        xmin=x
        break

# tekst printen van het minimum:
print "het minium bevindt zich in het punt (%f,%f)" %(xmin,ymin)        

# top van de grafiek plotten:
plt.plot(xmin, ymin,'ro')
plt.text(0.2, 0.8,(round(xmin,2),round(ymin,2)), color = 'black', fontsize = 20)

