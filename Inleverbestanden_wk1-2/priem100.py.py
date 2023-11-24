# Genereren van de lijst priemgetallen onder de 100.
priemgetallen=[]
teller=0
for getal in range (2,101):
    for deler in range (1,getal+1):
        test=getal%deler
        if test==0:
            teller=teller+1
    if teller <3:   # Een priemgetal is slechts door twee getallen deelbaar, namelijk 1 en zichzelf.             
        priemgetallen.append(getal)
    teller=0
    
print "Lijst van priemgetallen onder de 100:"
print priemgetallen

print "Deze lijst bestaat uit %d priemgetallen." % len(priemgetallen)


