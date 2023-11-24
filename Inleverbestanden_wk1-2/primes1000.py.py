# Genereren van een lijst bestaande uit de eerste 1000 priemgetallen:

priemgetallen=[]
xe_priemgetal=1000
teller=0
for getal in range (2,8001):
    for deler in range (1,getal+1):
        test=getal%deler
        if test==0:
            teller=teller+1
    if teller <3:                
        priemgetallen.append(getal)
    teller=0 
    lengte=len(priemgetallen)
    if lengte==xe_priemgetal:
        print "Het 1000e priemgetal is %d" %priemgetallen[999]
        break

print "Lijst van de eerste 1000 priemgetallen:"
print priemgetallen

