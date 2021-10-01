#first download Swift Observations sheet to a tsv file, read it to get coordinates, then plot those coordinates
#plot on both an aitoff projection and a 2d longitude latitude plot with circles of 12 arcminute radius, to visualize overlap btwn points
#caveat - observations are all at different times/dates. is it still accurate to plot all photons on the same axes then? 
import numpy as np
import csv
import astropy.io.fits
import matplotlib
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
from astropy.io import ascii
from astropy.coordinates import ICRS, Galactic, FK4, FK5
from astropy.coordinates import Angle, Latitude, Longitude
import math

longitudes = []
latitudes = []

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

for line in open('SwiftObservationsGW170823.tsv'):
    x = line.split('\t')
    #'\t'
    y=len(x)
    if(y==12):
        first = x[3]
        second = x[4]
        if((check_float(first)==True) and (check_float(second)==True)):
            f=(float(first))
            s=(float(second))
            longitudes.append(f)
            latitudes.append(s)
gal = SkyCoord(longitudes,latitudes, frame='galactic', unit=u.deg)

#Plotting
first_figure = matplotlib.pyplot.figure()
first_figure_axis = first_figure.add_subplot(111,projection='aitoff')
first_figure_axis.grid(True)

first_figure_axis.scatter(gal.l.wrap_at('180d').radian,gal.b.radian,s=1)
'''
first_figure_axis.scatter(gal2.l.wrap_at('180d').radian,gal2.b.radian,s=1)
first_figure_axis.scatter(gal3.l.wrap_at('180d').radian,gal3.b.radian,s=1)
first_figure_axis.scatter(gal4.l.wrap_at('180d').radian,gal4.b.radian,s=10)
first_figure_axis.scatter(gal5.l.wrap_at('180d').radian,gal5.b.radian,s=10)
'''
plt.title("HEASARC Search Results", y=1.08)
matplotlib.pyplot.xlabel('Long. in deg')
matplotlib.pyplot.ylabel('Lat. in deg')

second_figure=plt.figure(figsize=(8,6))
second_figure_axis = second_figure.add_subplot(111, projection=None)
second_figure_axis.grid(True)
second_figure_axis.set(xlim=(345, 352), ylim = (-4, 4))
i=0

while i<324:
    circle1=plt.Circle((longitudes[int(i)],latitudes[int(i)]),.2,fill=False)
    second_figure_axis.add_artist(circle1)
    i=i+1

second_figure_axis.scatter(longitudes,latitudes,s=10,color='red',zorder=1)
matplotlib.pyplot.xlabel('Long. in deg')
matplotlib.pyplot.ylabel('Lat. in deg')

plt.show()