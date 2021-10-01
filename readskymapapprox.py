#This code works, finds the credible region for a GW event, converts to galactic, and exports to a txt file that's read in other Python files 
import healpy as hp
import numpy as np
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord
import csv

hpx = hp.read_map('GW170823_skymap.fits')
npix = len(hpx)
sky_area = 4 * 180**2 / np.pi
nside = hp.npix2nside(npix)
#90% credible region code: 
i = np.flipud(np.argsort(hpx))
sorted_credible_levels = np.cumsum(hpx[i])
credible_levels = np.empty_like(sorted_credible_levels)
credible_levels[i] = sorted_credible_levels

coordTuple = tuple()
coordSet = set()
racolumn = []
deccolumn = []
probcolumn = []
i=0
#round ra dec values to 5 decimal pts, before comparing with neutral hydrogen density coords 
def truncate(n):
    n = int(n * 100000) / 100000
#786432 is the value of npix, total number of pixels 


while(i<786432):
    #print(i)
    theta, phi = hp.pix2ang(nside, i)
    ra1 = np.rad2deg(phi)
    dec1 = np.rad2deg(0.5 * np.pi - theta)
    
    #print(credible_levels[i])
    #print(d)
    #truncate(ra)
    #truncate(dec)
    #coordTuple = (ra, dec)
    #if it's in the 90% credible region, append it to the arrays, if not, do nothing
    if credible_levels[i] <= 0.9:
        #racolumn.append(ra)
        #deccolumn.append(dec)
        c = SkyCoord(ra=ra1*u.degree, dec=dec1*u.degree, frame='icrs')
    
        d = c.galactic
        coordSet.add(d)
        #print(credible_levels[i])
       # probcolumn.append(credible_levels[i])   
    i+=1
print(len(coordSet))
with open('galactic.txt', 'w') as filehandle:
    for listitem in coordSet:
        filehandle.write('%s\n' % listitem)