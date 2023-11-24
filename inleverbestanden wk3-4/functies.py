x = 100
print "x heeft de waarde %d" % (x)

breuk = 3./17.
print "breuk = %d" % (breuk)

breuk = 3./17.
print "breuk = %f" % (breuk)

breuk = 3./17.
print "breuk = %.2f" % (breuk)

x = 4
y = 3
z = x/y
print z

x = float(4)
y = 3
z = x/y
print z

L_x = []
for x in range(1,10):
    print "x heeft nu de waarde %d" % (x)
    L_x.append(x)
print L_x

import numpy as np #numpy module: nodig voor arange-functie
import math        #math module: nodig voor sin()-functie
L_x = []
L_y = []
for x in np.arange(0, 2*math.pi, 0.01):   # x loopt van 0 tot 2pi in stapjes van 0,01
    y = math.sin(x)
    L_x.append(x)
    L_y.append(y)


import numpy as np
x_begin = 2
x_eind = 3
dx = 0.02
for x in np.arange(x_begin, x_eind, dx):
    print x


import math

for x in range(1,21):
    x_kwadraat = math.pow(x, 2)
    print "%d in het kwadraat = %d" % (x, x_kwadraat)

def MijnKwadraatFunctie(getal):
    antwoord = getal * getal
    return antwoord
    
#-- hier begint het programma
for x in range (1,21):
    x_kwadraat = MijnKwadraatFunctie(x)
    print "%d in het kwadraat = %d" % (x, x_kwadraat)

def GrootsteGetal(a,b):
    grootste=0
    if a>b:
        grootste=a
    else:
        grootste=b
    return grootste
    
#-- hier begint met programma
getal_1=126
getal_2=14
largest_number=GrootsteGetal(getal_1, getal_2)
print "het grootste getal = %d" % (largest_number)


import matplotlib.pyplot as plt

def MijnPolynoom(L_x):
    L_y=[]
    for x in L_x:
        y = 8*x*x-5*x+9
        L_y.append(y)
    return L_y
    
#-- hier begin het programma
L_xwaardes=[1,2,3,4,5,6]
L_ywaardes=MijnPolynoom(L_xwaardes)

# Eventueel kan de volgende grafiek ook worden geplot:
#plt.plot(L_xwaardes, L_ywaardes, 'g-')
plt.show()    

print

# Opgave 1
print "Opgave 1:"

import matplotlib.pyplot as plt
import numpy as np
import math

a = 1
b = 2
c = -10
D = b**2 - 4*a*c
# Input = L_x , Output = L_y

def Polynoomopgave1(L_x):
    L_y = []
    for x in L_x:
        y = a*x*x+b*x+c
        L_y.append(y)
    return L_y

# programma:

x = np.arange(-10,10,0.01)
L_y = Polynoomopgave1(x)
    
#print x
#print Polynoomopgave1(L_x)
#x01=0
#x02=0
#D=0
def Nulpunten(a,b,c):
    L_x0 = []
    x01 = 0
    x02 = 0
    D = b**2 - 4*a*c
    if D > 0:
        # abc formule:
        x01 = (-b - math.sqrt(D) ) / (2*a)
        x02 = (-b + math.sqrt(D) ) / (2*a)
        L_x0.append(x01)
        L_x0.append(x02)
        return L_x0
    if D < 0:
        return L_x0
    if D == 0:
        x01 = -b / (2 * a)
        L_x0.append(x01)
        return L_x0
    #break
    
    
L_x0 = Nulpunten (a,b,c)
L_y0 = Polynoomopgave1(L_x0)   
#print "%d" % (4)

# Grafiek plotten:
plt.plot(x, L_y , 'b-')
plt.show()
plt.text(0.00, 100,"f(x)=%dx^2+%dx+%d" %(a,b,c), color = 'black', fontsize = 20)

if D == 0:
    print "Er is 1 snijpunt met de x-as, namelijk:"
    print L_x0[0]
    plt.plot(L_x0[0], L_y0[0], 'ro')
    plt.text(L_x0[0],  L_y0[0]+2, "$x1=%.2f$" % (L_x0[0]), color = 'black', fontsize = 10)
if D < 0:
    print "Er zijn geen snijpunten met de x-as"
if D > 0:
    print "Er zijn 2 snijpunten met de x-as, namelijk:"
    print L_x0[0]
    print L_x0[1]
    plt.plot(L_x0[0], L_y0[0], 'ro')
    plt.plot(L_x0[1], L_y0[1], 'ro')
    plt.text(L_x0[0], L_y0[0]+2, "$x1=%.2f$" % (L_x0[0]), color = 'black', fontsize = 10)
    plt.text(L_x0[1]-2,  L_y0[1]+2, "$x1=%.2f$" % (L_x0[1]), color = 'black', fontsize = 10)









