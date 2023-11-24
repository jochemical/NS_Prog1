
import math

# Opgave 1

L = [2, 3, 7, 6, 0, 12, 3, 7, 9, 6]
L1 = [7,7,7,7,7,7,8,9,6,5] # Testen met een andere inputlijst

def Opgave(Lijst):
    # Startvariabelen
    bovengem = 0
    ondergem = 0
    Lijst_afw = []
    som = 0
    for n in Lijst:
        som = som + n
    gem = float(som) / len(Lijst) # gemiddelde berekenen
    for m in Lijst:
        afw = m - gem
        Lijst_afw.append(afw)
        if m < gem:
            ondergem = ondergem + 1
        if m > gem:
            bovengem = bovengem + 1
    print "Het gemiddelde van de lijst getallen is %f" % (gem)
    print "Er zijn %d waarden onder het gemiddelde en %d erboven" %(ondergem, bovengem)
    print "Afwijkingslijst =", Lijst_afw 

Opgave(L)

# Opgave 2

import random

def Opgave2(h):
    imax = 100
    fdopje = 0
    # Kubus defenieren
    xmin = -20
    xmax =  20
    ymin = -20
    ymax =  20
    zmin = -20
    zmax =  20
    kx = xmax - xmin
    ky = ymax - ymin
    kz = zmax - zmin
    # Inhoud kubus
    inhoud_kubus = kx * ky * kz

    for i in range(0, imax): 
        # Random stapgroottes
        dx = random.random() * (xmax - xmin)
        dy = random.random() * (ymax - ymax)
        dz = random.random() * (zmax - zmin)
    
        # Coordinaten Random punt
        x = xmin + dx
        y = ymin + dy
        z = zmin + dz
        
        # Straal uitrekenen voor random punt
        test = (x**2) + (y**2) + (z**2)
        if test < 1 and y > (1 - h): # Testen of het punt binnen het dopje valt
            fdopje = fdopje + 1
    inhoud_dopje = inhoud_kubus * (float(fdopje) / imax)
    print "Inhoud dop (h = %f) is: %f" %(h, inhoud_dopje)
    
Opgave2(0.25)


# Opgave 3

def Opgave3(a, b, c, d, e):
    # abc-formule
    D = (b-d)**2 - 4*a*(c-e) # Discriminant
    if D > 0:
        x1 = (- (b-d) - math.sqrt(D)) / (2*a) 
        x2 = (- (b-d) + math.sqrt(D)) / (2*a)
        print "Er zijn twee snijpunten: x1 = %f en x2 = %f" % (x1, x2)
    if D == 0:
        x = - (b-d) / (2*a)
        print "Er is een snijpunt: x = %f" % (x)
    if D < 0:
        print "Er zijn geen snijpunten"
Opgave3(1,2,3,4,5)        
Opgave3(5,4,3,2,1)


# Opgave 4

def Opgave4():
    for a in range(1,101):
        for b in range(1,101):
            c = math.sqrt(a**2 + b**2)
            geheeltest = c - int(c) # Testen of c een geheel getal is
            if c < 100 and geheeltest == 0:
                print "(%d, %d, %d)" % (a, b, c)
Opgave4()


# Opgave 5

# Lijn:
def Opgave5():
    som = 0
    f12 = 0
    f89 = 0
    N = 1000 # Aantal paar random punten
    xmin = 0
    xmax = 1
    for n in range(0,N):
        dx1 = random.random() * (xmax - xmin)
        dx2 = random.random() * (xmax - xmin)
        x1 = xmin + dx1
        x2 = xmin + dx2
        if x1 > x2:    
            delta = x1 - x2
        if x2 > x1:
            delta = x2 - x1
        som = som + delta
        if delta < 0.2 and delta > 0.1:
            f12 = f12 + 1 
        if delta < 0.9 and delta > 0.8:
            f89 = f89 + 1
    # Kansen en gemiddlde berekenen
    kansf89 = float(f89) / N 
    kansf12 = float(f12) / N
    gem_delta = som / N
    if f89 > 0:    
        relatief = float(kansf12) / kansf89
        print "De relatieve kans f12/f89 = %f" % (relatief)
    if f89 == 0: # Delen door geeft probleem bij kleine waardes van N
        print "f89 = 0"
    print "De gemiddelde afstand tussen 2 punten op een lijn = %f" % (gem_delta)
    
Opgave5()
   
        
            

                    
                                        
                                                            
                                                                                
                                                                                                    
                                                                                                                        
                                                                                                                                                                