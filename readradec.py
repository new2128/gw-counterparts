import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy.coordinates import ICRS, Galactic, FK4, FK5
from astropy.coordinates import Angle, Latitude, Longitude
import math

ras=[]
decs=[]
filename = 'data.lis'
with open(filename) as f:
    for line in f:
        x=line.split()
        first = x[0]
        second = x[1]
        ra=float(first)
        dec=float(second)
        ras.append(ra)
        decs.append(dec)
print(ras)
print(decs)
gal = SkyCoord(ras,decs, frame='fk5', unit=u.deg)

first_figure = matplotlib.pyplot.figure()
first_figure_axis = first_figure.add_subplot(111,projection='aitoff')
first_figure_axis.grid(True)
first_figure_axis.scatter(gal.ra.wrap_at('180d'),gal.dec,s=10) 
plt.show()