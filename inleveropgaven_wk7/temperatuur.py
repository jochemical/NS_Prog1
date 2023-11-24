
# Opgave 2: Klimaat in Nederland

# Vraag 2A) extreme temperaturen:
# Vraag 2B) koud kouder koudst
# Vraag 2C) zomerse en tropische dagen
# Vraag 2D) hittegolf in 2015

import math
import numpy as np
import matplotlib.pyplot as plt

# De Lijst van Maximale temperaturen

# Variabelen voor maximale temperatuur
Lijst_maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
Lijst_data = []
Lijst_Tmax = []
Tmax = -10 ** 99

# Variabelen voor langste vriesperiode
vriesteller = 0 # telt het aantal aaneengesloten vriesdagen
langste_vriesperiode = 0 # onthoudt de langste vriesperiode
vorige_dag = 0 # Onthoudt of het de voorgaande dag vroor

# Variabele voor zomerse en tropische dagen
Lijst_jaar = []
Lijst_zomdagjaar = []
Lijst_tropdagjaar = []
jaarhuidig = 0 # Om jaarwisselingen bij te houden
zomdagjaar = 0 # Aantal zomerdagen per jaar
tropdagjaar = 0 # Aantal tropische dagen per jaar

# Variabelen voor hittegolven
Lijst_hittegolf = [] # Geeft de jaartallen waarin er sprake was van hittegolven
hittegolftellerzom = 0 # Teller voor aaneengesloten zomerse dagen
hittegolftellertrop = 0 # Teller voor aaneengesloten tropische dagen
toegevoegd = 0 # Om te voorkomen dat dezelfde hittegolf meerdere keren wordt genoteerd

# De Lijst van Maximale temperaturen inlezen en verwerken
teller = 1 # Om eerste 30 regels over te slaan
input_filehandle = open('DeBiltTempMax.txt','r')
for line in input_filehandle:
    if teller == 31: # 30 regels overslaan   
        data_opgeknipt = line.split(',')
        datum = data_opgeknipt[2]
        temperatuur = float(data_opgeknipt[3]) * 0.1
        Lijst_data.append(datum)
        Lijst_Tmax.append(temperatuur)
        
        # Uitrekenen maximale temperatuur
        if temperatuur > Tmax:
            Tmax = temperatuur
            jaarTmax = float(datum[0:4])
            maandTmax = int(datum[4:6])
            maandTmaxw = Lijst_maanden[maandTmax-1]
            dagTmax = float(datum[6:8])
            
        # Gedeelte voor langste vriesperiode
        if temperatuur < 0:
            vorige_dag = 1
        if temperatuur < 0 and vorige_dag > 0:
            vriesteller = vriesteller + 1
            vriesdatum = datum
        if temperatuur >= 0:
            if vriesteller > langste_vriesperiode:
                langste_vriesperiode = vriesteller
            vriesteller = 0
            vorige_dag = 0
            
        # Gedeelte voor zomerdagen en tropische dagen
        if  float(datum[0:4]) > jaarhuidig: # jaarwisseling
            Lijst_jaar.append(jaarhuidig)
            Lijst_zomdagjaar.append(zomdagjaar)
            Lijst_tropdagjaar.append(tropdagjaar)
            zomdagjaar = 0
            tropdagjaar = 0
        jaarhuidig = float(datum[0:4])
        if temperatuur < 25:
            hittegolftellerzom = 0
            hittegolftellertrop = 0
            toegevoegd = 0
        if temperatuur >= 25 and temperatuur < 30: # zomerse dagen
            zomdagjaar = zomdagjaar + 1 
            hittegolftellerzom = hittegolftellerzom + 1 # opeenvolgende zomerse dagen
        if temperatuur >= 30: # tropische dagen
            tropdagjaar = tropdagjaar + 1
            hittegolftellertrop = hittegolftellertrop + 1 # aantal tropische dagen binnen een potentiele hittegolf
        som = hittegolftellertrop + hittegolftellerzom 
        if som >= 5 and hittegolftellertrop >= 3 and toegevoegd == 0:
            Lijst_hittegolf.append(jaarhuidig)
            toegevoegd = toegevoegd + 1
    if teller < 31: # eerste 30 regels overslaan
        teller = teller + 1
input_filehandle.close()


# De Lijst van Minimale temperaturen

# Variabelen voor minimale temperatuur
Lijst_Tmin = []
Tmin = 10 ** 99
datumTmin = 0

# De Lijst van Minimale temperaturen inlezen en verwerken
teller2 = 1 # Om eerste 30 regels over te slaan
input_filehandle = open('DeBiltTempMin.txt','r')
for line2 in input_filehandle:
    if teller2 == 31:    
        data_opgeknipt = line2.split(',')
        datum2 = data_opgeknipt[2]
        temperatuur2 = float(data_opgeknipt[3]) * 0.1
        Lijst_Tmin.append(temperatuur)
        # Uitrekenen minimale temperatuur
        if temperatuur2 < Tmin:
            Tmin = temperatuur2
            jaarTmin = float(datum2[0:4])
            maandTmin = int(float(datum2[4:6]))
            maandTminw = Lijst_maanden[maandTmin-1]
            dagTmin = float(datum2[6:8])                
    if teller2 < 31: # eerste 30 regels overslaan
        teller2 = teller2 + 1
input_filehandle.close()


# Laatste Vriesdag uitwerken
vriesdag = float(vriesdatum[6:8])
vriesmaand = int(vriesdatum[4:6])
vriesmaandw = Lijst_maanden[vriesmaand-1]
vriesjaar = float(vriesdatum[0:4]) 

# Grafiek plotten van tropische en zomerdagen
plt.xlim(1900,2020)
plt.ylim(-40,50)
plt.plot(Lijst_jaar, Lijst_zomdagjaar, 'g-')
plt.plot(Lijst_jaar, Lijst_tropdagjaar, 'r-')
plt.show()

# Printen van de oplossingen
print "De hoogste temperatuur was %f graden Celcius en werd gemeten op %d %s %d." % (Tmax, dagTmax, maandTmaxw, jaarTmax)
print "De laagste temperatuur was %f graden Celcius en werd gemeten op %d %s %d." % (Tmin, dagTmin, maandTminw, jaarTmin) 
print "De langste vriesperiode was %d dagen en de laatste vriesdag van deze periode viel op %d %s %d." % (langste_vriesperiode, vriesdag, vriesmaandw, vriesjaar)
print "Er was sprake van een hittegolf in de volgende jaartallen:"
print Lijst_hittegolf # De lijst geeft aan in welke jaartallen er sprake was van een hittegolf
# Het jaar 2015 valt binnen deze lijst dus was er toen sprake van een hittegolf.