from climacell.api import ClimaCellApi as Clima

# Initiate with location name (using opencage api)
c = Clima("Thessaloniki")

# Or pass the coordinates yourself
c = Clima(coords=(44.54, 22.24))

# Check the daily forcast
c.daily()