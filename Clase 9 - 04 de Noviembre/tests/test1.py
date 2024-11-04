from Clases import Position, Waypoint, Trackpoint, Distance

def testDistance(latitud1, longitud1, altitud1, latitud2, longitud2, altitud2):
    distance = Distance.km(())

santiago = Position(-33.45694, -70.64827, 520)
concepcion = Position(-36.82699, -73.04977, 12)

testDistance(
    -33.45694, 
    -70.64827, 
    520,
    -36.82699, 
    -73.04977, 
    12
)
