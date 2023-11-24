# Van het volgende getal x moet getest worden of het een priemgetal is:
x=37

som=0
teller=0
for getal in range (1,x+1):
    som = x % getal
    if som == 0:
        teller=teller+1

if teller < 3:    
    print "Het getal %f is een priemgetal." %x
if teller > 2:
    print "Het getal %f is geen priemgetal." %x




