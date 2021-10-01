#Finds the intersection between the NH4PI galactic plane regions and the 90% credible region. Does not fully work because of rounding errors. 
import healpy as hp
import numpy as np
import pandas as pd
import csv
import astropy.io.fits
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord


hpx = hp.read_map('GW170823_skymap.fits')
# h=True, verbose=False)
#2d image of the map:
#hp.mollview(hpx)
npix = len(hpx)
sky_area = 4 * 180**2 / np.pi
#print(npix)
#print(sky_area)
print('average pixels per square degree:',sky_area / npix)
nside = hp.npix2nside(npix)
#print(nside)

#90% credible region code: 
i = np.flipud(np.argsort(hpx))
sorted_credible_levels = np.cumsum(hpx[i])
credible_levels = np.empty_like(sorted_credible_levels)
credible_levels[i] = sorted_credible_levels
#print(credible_levels)
#use this code to check the probability for a specific pixel: 
#print(credible_levels[128])
#if ipix is a specific pixel,  print its probability level:
#print(credible_levels[ipix])
#print(np.sum(credible_levels <= 0.9) * hp.nside2pixarea(nside, degrees=True))

#code to find most probable coordinate on the sky: 
#ipix_max = np.argmax(hpx)
#print(hpx[ipix_max] / hp.nside2pixarea(nside, degrees=True))
#theta, phi = hp.pix2ang(nside, ipix_max)
#ra = np.rad2deg(phi)
#dec = np.rad2deg(0.5 * np.pi - theta)
#print('ra = ',ra)
#print('dec = ',dec)
coordTuple = tuple()
coordSet = set()
racolumn = []
deccolumn = []
probcolumn = []
i=0
#round ra dec values to 5 decimal pts, before comparing with neutral hydrogen density coords 
def truncate(n):
    n = int(n * 10) / 10
#786432 is the value of npix, total number of pixels 
while(i<786432):
    #print(i)
    theta, phi = hp.pix2ang(nside, i)
    ra = np.rad2deg(phi)
    dec = np.rad2deg(0.5 * np.pi - theta)
    ra1=int(float(ra))
    dec1=int(float(dec))
    ra2=float(ra)
    dec2=float(dec)
    ra3=truncate(ra2)
    dec3=truncate(dec2)
    coordTuple = (ra1, dec1)
    #if it's in the 90% credible region, append it to the arrays, if not, do nothing
    if credible_levels[i] <= 0.9:
        #racolumn.append(ra)
        #deccolumn.append(dec)
        coordSet.add(coordTuple)
       # probcolumn.append(credible_levels[i])   
    i+=1

#code for finding most probable coordinate - but it doesn't intersect the galactic plane :(
'''
ipix_max = np.argmax(hpx)
theta1, phi1 = hp.pix2ang(nside, ipix_max)
ra1 = np.rad2deg(phi)
dec1 = np.rad2deg(0.5 * np.pi - theta)
print(ra1, dec1)
'''
coordSetGPlane = set()
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

for line in open('asu.tsv'):
    x = line.split('\t')
    #'\t'
    y=len(x)
    if(y==5):
        first = x[2]
        second = x[3].replace("+", "")
        if((check_float(first)==True) and (check_float(second)==True)):
            f=int(float(first))
            #truncate(f)
            s=int(float(second))
            #truncate(s)
            coordTupleGPlane = tuple((f,s))
            #coordTupleGPlane = tuple(x[2:4])
            coordSetGPlane.add(coordTupleGPlane)

print(len(coordSetGPlane))
if ('194', '22') in coordSetGPlane:
    print("Yes, coordinate is in this set")

c=coordSet.intersection(coordSetGPlane)
print(len(c))

mydf = pd.DataFrame(list(c))
mydf.to_excel("intersection.xlsx")

#writer = pd.ExcelWriter('intersection.xlsx')
 
# Write your DataFrame to a file     
#c.to_excel(writer, 'Sheet1')
 
# Save the result 
#writer.save()