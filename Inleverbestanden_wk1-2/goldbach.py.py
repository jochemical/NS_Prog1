
# lijst genereren met alle priemgetallen onder de 1001:

priemgetallen=[] # lijst met priemgetallen
teller=0
for getal in range (2,1001):
    for deler in range (1,getal+1):
        test=getal%deler
        if test==0:
            teller=teller+1
    if teller <3: # Een priemgetal is slecht door 2 getallen deelbaar: 1 en zichzelf               
        priemgetallen.append(getal)
    teller=0
    
# Het vermoeden van Goldbach testen:

y=1001
a=0               
for evengetal in range (4,y,2):                #creeert evengetallen boven de 3
    for lager_getal in range (0,evengetal):     #alle getallen < het evengetal
        if lager_getal in priemgetallen:        # -die binnen de priemgetallen vallen            
            a=evengetal-lager_getal             # het priemgetal van het evengetal aftrekken
            if a in priemgetallen:             # indien het antwoord ook een priemgetal is
                print "%d = %d + %d" % (evengetal, a, lager_getal) # wordt de som opgeschreven
                break # afbreken van de loop
