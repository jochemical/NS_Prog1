
# Numeriek integreren met Riemann

import numpy as np # numpy module is nodig voor arange-functie
import math # math module is o.a. nodig voor math.pow-functie
import matplotlib.pyplot as plt # pyplot module is nodig voor plotten van grafieken



# Opgave 4

dx = 0.01
# Lijsten met x respectievelijk y -waarden opstellen
L_x = []
L_y = []
for x in np.arange(0, 1+dx, dx):  
    y = x ** x
    L_y.append(y)
    L_x.append(x)
imax = len(L_y)

# Riemannsom opgave 4
som = 0
for i in range(1,imax-1):
    som = som + L_y[i]
Int4 = dx * som + (dx / 2) * (L_y[0] + L_y[imax - 1])

print "De integraalbenadering van x^x in het domein 0 tot 1 is %f." % (Int4)

# Opgave 5
dx = 0.01
# Lijsten met x respectievelijk y -waarden opstellen
L_x = []
L_y = []
for x in np.arange(0.1, 2+dx, dx):  
    y = math.sin(x)
    L_y.append(y)
    L_x.append(x)
imax = len(L_y)

# Riemannsom opgave 5

som = 0
for i in range(1,imax-1):
    som = som + L_y[i]
Int5 = dx * som + (dx / 2) * (L_y[0] + L_y[imax - 1])

print "De integraalbenadering van sin(x) in het domein 0.1 tot 2 is %f." % (Int5)


# Opgave 6

dx = 0.0001
# Lijsten met x respectievelijk y -waarden opstellen
L_x = []
L_y = []
for x in np.arange(0, math.pi+dx, dx):  
    y = math.sin(x ** 2)
    L_y.append(y)
    L_x.append(x)
imax = len(L_y)

# Riemannsom opgave 6

som = 0
for i in range(1,imax-1):
    som = som + L_y[i]
Int6 = dx * som + (dx / 2) * (L_y[0] + L_y[imax - 1])

print "De integraalbenadering van sin(x^) in het domein 0 tot pi is %f." % (Int6)

