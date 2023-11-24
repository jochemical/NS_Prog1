
# genereren van de lijst priemgetallen onder de 10000:

priemgetallen=[]
teller=0
for getal in range (2,10000):
    for deler in range (1,getal+1):
        test=getal%deler
        if test==0:
            teller=teller+1
    if teller <3:                
        priemgetallen.append(getal)
    teller=0
    
    
# Het uitrekenen van de langste reeks niet-priemgetallen onder de 10000:

a=0
b=0
rangorde_max=len(priemgetallen)
grootste_rangelengte=0
rangelengte=0
for rangorde in range (1,rangorde_max):
    # bovengrens:
    bovengrens=priemgetallen[rangorde]
    # ondergrens:
    ondergrens=priemgetallen[rangorde-1]
    # rangelengte (lengte reeks niet-priemgetallen):
    rangelengte=bovengrens-ondergrens-1
    # grootste rangelengte filtreren:
    if rangelengte>grootste_rangelengte:
        grootste_rangelengte=rangelengte
        a=ondergrens
        b=bovengrens
        #print grootste_rangelengte    
        rangelengte=0
        
print "De langste aaneengesloten reeks niet priemgetallen onder de 10000 bestaat uit %d cijfers, en bevindt zich tussen de priemgetallen %d en %d." %(grootste_rangelengte, a, b)
