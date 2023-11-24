# Oefeningen met Python Module 1
# Jochem Kemp
# 04-09-2015

#Printen
# tekens tussen de aanhalingstekens worden direct geprint indien er print voor staat
print"hallo, wereld!"
print"Hee, hallo daar."
print"Zo tikt het lekker door."
print"grappig"
print'hee, print dit nog?'
print"Ivo's computer doet het vandaag niet."
print'Hij zei:"Hallo."'
# programma rekent automatisch rekensommen uit tenzij het tussen aanhalingtekens wordt gezet
print 1
print 1
print 1 + 1
print 1 + 1 + 1
print 3+2
print 8
print 5+8+8-8
print"5+8+8-8"
# sommen uitrekenen binnen aanhalingstekens kan mbv de volgende verwijzingstekens
print"Het 1e getal van Fibonacci is %d"%1
print"Het 2e getal van Fibonacci is %d" % 1
print"Het 3e getal van Fibonacci is %d" % (1+1)
print"Het 4e getal van Fibonacci is %d" % (1+2)
print"Het 5e getal van Fibonacci is %d" %(2+3)

# Commentaar

# Variabelen
aantal=20
print aantal
aantal=aantal-1
print aantal


# if-statements

x=15
if x >0:
    print "het getal %d is positief" % x
else:
    print "het getal %d is negatief" % x
    
x = 15
x_min = 3
x_max = 39
if x > x_min and x < x_max:
    print "het getal %d bevindt zich tussen %d en %d" % (x, x_min, x_max)

# Loops
for getal in range(1,10):
    []
for getal in range(1,11):
    print getal
print "ik ben klaar"
som = 0
for getal in range (1,21):
    som = som + getal
print "de som van de getallen van 1 tot en met 20 is %d" % (som)

som=0
for getal in range (1,21):
    if getal % 2 == 0:
        print "yes! %d is een even getal" % getal
        som = som + getal
print "De som van de even getallen van 1 tot en met 20 is %d" % (som)



som=0
for getal in range (1,88):
    if getal % 2 == 0:
        print "yes! %d is een even getal" % getal
        som = som + getal
print "De som van de even getallen van 1 tot en met 88 is %d" % (som)

som=0
max_getal = 88
for getal in range (1,max_getal+1):
    if getal % 2 == 0:
        print "yes!", getal, "is een even getal"
        som = som + getal
print "de som van de even getallen van 1 tot en met %d is %d" % (max_getal, som)

for getal in range(1,100,10):
    print getal

# Lijsten

docenten=["Martijn", "Ivo", "Rico", "Nick", "Rick", "Kelly"]
print docenten [2]
#
metingen_science_park = [12.7 , 18.8, 24.9, 14.5, 19.0]
print metingen_science_park
#
metingen_science_park.append(20.5)
print metingen_science_park
#
print"Het eerste element van de lijst is %d" % metingen_science_park [0]
print"Het aantal elementen in de lijst is %d" % len(metingen_science_park)
#
for meting in metingen_science_park:
    print "de meting was %d graden" % meting
#   
teller = 0
for meting in metingen_science_park:
    teller = teller + 1
    print "de %d e meting was %d graden" % (teller, meting)
# 
som = 0
teller = 0
for meting in metingen_science_park:
    teller = teller +1
    som = som + meting
    print "De %d e meting was %d graden." % (teller, meting)
gemiddelde_temp = som / teller
print "De gemiddelde temperatuur was %d graden." % gemiddelde_temp
#
hete_dagen = 0
for meting in metingen_science_park:
    if meting> 20:
        hete_dagen = hete_dagen + 1
print "Op %d was de temperatuur boven de 20 graden" % hete_dagen

import math
x=0.5
print math.sin(x)

#versie 1
for i in range(1,10):
    print i

# versie 2
for i in [1,2,3,4,5,6,7,8,9]:
    print i

import numpy
for x in numpy.arange(2.0,9.0,0.1):
    print x


# Grafieken

import matplotlib.pyplot
# de coordinaten per punt
x_coords = [0,1,2,3,4,5]
y_coords = [0,1,4,9,16,25]

# plot punten (y tegen x) met groene rondjes
matplotlib.pyplot.plot(x_coords, y_coords, 'go')
matplotlib.pyplot.show()

# gebruikmakend van de afkorting 'plt'
import matplotlib.pyplot as plt
# de coordinaten per punt
x_coords = [0,1,2,3,4,5]
y_coords = [0,1,4,9,16,25]

plt.plot(x_coords, y_coords, 'go')
plt.show()

# Het plotten van een lijngrafiek:
import matplotlib.pyplot as plt

x_es = [0,1,2,3,4,5]
x_squared = [0,1,4,9,16,25]
x_cubed = [0,1,8,27,64,125]
# let op: grafiek met twee datasets!
plt.plot(x_es, x_squared,'go', x_es, x_cubed,'r-')

plt.xlabel('de x-as is klein')
plt.ylabel('de y-as ix groot', fontsize = 25)

plt.text(1.00,100.,"mijn eerste plotje", color = 'blue',fontsize= 20)
plt.text(4.00,100., "$x^3$", color = 'red', fontsize= 20)

plt.show()

# Het plotten van een sinus-grafiek:
import numpy as np # numpy mdule: nodig voor arange-functie
import math # math module: nodig voor sin()-functie
import matplotlib.pyplot as plt # pyplot module: nodig voor plotten

L_x = [] # lijst met x-waarden
L_y = [] # lijst met y-waarden

# x loopt van 0 tot 2 pi in stapjes van 0.01
for x in np.arange(0, 2*math.pi, 0.01):
    # bereken bijbehorende y-waarde voor elke x
        y = math.sin(x)
        
    # voeg data toe aan de lijsten
        L_x.append(x)
        L_y.append(y)
        
# teken de hele grafiek
plt.plot(L_x, L_y, 'b-')
plt.xlabel('x',fontsize = 20)
plt.ylabel('sin(x)',fontsize = 20)
plt.text(4.00, 0.50,"f(x)=sin(x)", color = 'black', fontsize = 20)
plt.show()
# De sinus-grafiek is niet heel duidelijk te zien omdat de andere grafieken ook worden geplot.

