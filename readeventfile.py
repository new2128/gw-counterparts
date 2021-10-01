#not currently working
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.table import Table 
from matplotlib.colors import LogNorm
import os
import subprocess

path = 'sw00811235000xpcw3po_cl.evt'
data = open(path, 'r')

hdu_list = fits.open(path, memmap=True)
hdu_list.info()
print(hdu_list[1].columns)
evt_data = Table(hdu_list[1].data)
print(evt_data)
'''

NBINS = 500
energy_hist = plt.hist(evt_data['PI'], NBINS)

NBINS = (100,100)
img_zero_mpl = plt.hist2d(evt_data['X'], evt_data['Y'], NBINS, cmap='viridis', norm=LogNorm())

cbar = plt.colorbar(ticks=[1.0,3.0,6.0])
#cbar.ax.set_yticklabels(['1','3','6'])

plt.xlabel('x')
plt.ylabel('y')
plt.show()

os.system('dmcoords sw00811235000xpcw3po_cl.evt none option=sky x=4096.5 y=4096.5 celfmt=deg')
os.system('pget dmcoords ra')
'''

xskycoordinates = [] 
xskycoordinates= evt_data['X']

yskycoordinates = []
yskycoordinates= evt_data['Y']

ralist=[]
declist=[]

i=0
while(i<10204):
    x=float(xskycoordinates[i])
    y=float(yskycoordinates[i])
    os.system('dmcoords sw00811235000xpcw3po_cl.evt none option=sky x=x y=y celfmt=deg')
    ra = subprocess.check_output('pget dmcoords ra', shell=True) 
    #dec = os.system('pget dmcoords dec')
    ralist.append(ra)
    #declist.append(dec)
    i=i+1