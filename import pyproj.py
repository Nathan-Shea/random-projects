import pyproj
from math import sqrt

lon = 141.995920 
lat = -35.996778
size = 2000

endlon, endlat, _ = pyproj.Geod(ellps='WGS84').fwd(lon, lat, 135, sqrt(size**2 + size**2))

print (f'{endlon:.6f}, {endlat:.6f}')

