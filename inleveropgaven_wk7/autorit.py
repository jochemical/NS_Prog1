
# Opgave 1: Sensor Data

import math
import numpy as np
import matplotlib.pyplot as plt


# Opgave 1A Afgelegde afstand

Lijst_t = []
Lijst_v = []
teller = 0
x = 0

input_filehandle = open('AutoRitData.csv','r')
for line in input_filehandle:
    if teller == 1:    
        data_opgeknipt = line.split(',')
        recordtime = float(data_opgeknipt[2])
        snelheid = float(data_opgeknipt[6])
        Lijst_t.append(recordtime)
        Lijst_v.append(snelheid)
        dx = snelheid * 1
        x = x + dx
    if teller == 0: # Het overslaan van de eerste regel
        teller = teller + 1
input_filehandle.close()

# Grafiek van de snelheid als functie van de tijd:
#plt.plot(Lijst_t, Lijst_v, 'r-')
#plt.show()

# Printen van de afgelegde weg
print "De totale afgelegde weg is %f meter." % (x)


# Opgave 1B Teken de afgelegde route

Lijst_x = []
Lijst_y = []
teller = 0
x = 0

input_filehandle = open('AutoRitData.csv','r')
for line in input_filehandle:
    if teller == 1:    
        data_opgeknipt = line.split(',')
        # Coordinaten lezen uit het excel-bestand
        long = float(data_opgeknipt[4])
        lat = float(data_opgeknipt[3])
        # Coordinaten toevoegen aan de lijsten
        Lijst_x.append(long)
        Lijst_y.append(lat)
        snelheid = float(data_opgeknipt[6])
        vkmh = snelheid / 3.6
        if vkmh > 50:
            plt.plot(long, lat, 'go')
        if vkmh < 50:
            plt.plot(long, lat, 'ro')
    if teller == 0: # Overslaan van de eerste regel
        teller = teller + 1
input_filehandle.close()

plt.show()






# Overige oefeningen (voordat opgave 1 begon):

# Module 4

# Inlezen files en verwerken van data

# versie 1
input_filehandle = open('VanBasten.txt','r')
for line in input_filehandle:
    print line
input_filehandle.close()

# versie 2
input_filehandle = open('VanBasten.txt','r')
for line in input_filehandle:
    print line
    data_opgeknipt = line.split(',')
    print data_opgeknipt
input_filehandle.close()

# stap 3: opslaan van de informatie in variabelen

seizoen = data_opgeknipt[0]
doelpunten = data_opgeknipt[2]

# Issue 1
seizoen = data_opgeknipt[0][0:4]
doelpunten = data_opgeknipt[2]

# Issue 2
seizoen = float(data_opgeknipt[0][0:4])
doelpunten = float(data_opgeknipt[2])

# Stap 4: Het analyseren van data
# Versie 3 programma

input_filehandle = open('VanBasten.txt','r')

Ndoelpunten_tot = 0

for line in input_filehandle:
    data_opgeknipt = line.split(',')
    
    seizoen = float(data_opgeknipt[0][0:4])
    doelpunten = float(data_opgeknipt[2])
    
    Ndoelpunten_tot = Ndoelpunten_tot + doelpunten
    
    if(doelpunten > 20):
        print "In %d scoorde van Basten > 20 doelpunten, nl %d" % (seizoen, doelpunten)

print "TOTAAL: In totaal scoorde van Basten %d clubdoelpunten" % (Ndoelpunten_tot)

# Schrijven naar een file

# Voorbeeld 1: tekst schrijven naar een file
output_filehandle = open('outputfile.txt','w')
output_filehandle.write("Het vak Inleiding Programmeren is bere-interessant")
output_filehandle.close()

# Voorbeeld 2: extra tekst achter bestaande regel plakken 
input_filehandle = open('vanBasten.txt','r')
output_filehandle = open('outputfile.txt','w')
for line in input_filehandle:
    newline = line + "XXXX"
    output_filehandle.write(newline)
    
input_filehandle.close()
output_filehandle.close()









        
            
                    
