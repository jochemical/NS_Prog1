
import math # voor de math.sqrt en math.pow functie

# waarden vector v1:
v1x=2
v1y=5

# waarden vector v2:
v2x=1
v2y=2

# lengtes uitrekenen (absolute waarden):
lengte_v1= math.sqrt(math.pow(v1x,2) + math.pow(v1y,2))
lengte_v2= math.sqrt(math.pow(v2x,2) + math.pow(v2y,2))

# producten uitrekenen:
lengteproduct= lengte_v1*lengte_v2
vectorproduct=v1x*v2x+v1y*v2y

# hoek berekenen:
deelsom=vectorproduct/lengteproduct
a=math.acos(deelsom)

# omrekenen naar graden
b=math.degrees(a)

# tekst printen
print "De hoek tussen (%d , %d) en (%d , %d) is %f graden." %(v1x,v1y,v2x,v2y,b)
