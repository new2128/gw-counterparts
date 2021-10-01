#create a list of points from heasarc archived data that are in the 90% credible region for the gw event: 

import healpy as hp
import numpy as np
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
from os.path import expanduser as ospath


url = "https://dcc.ligo.org/public/0157/P1800381/007/GW170823_skymap.fits.gz"

#setting up information from the gw file: 
prob= hp.read_map(url)
npix = len(prob)
nside = hp.npix2nside(npix)

#testing credibility:
i = np.flipud(np.argsort(prob))
sorted_credible_levels = np.cumsum(prob[i])
credible_levels = np.empty_like(sorted_credible_levels)
credible_levels[i] = sorted_credible_levels


data = pd.read_excel(ospath('/Users/nicolewolff/Desktop/ds9/browse_results.xlsx'), sheet_name)

ra = data['ra']
dec = data['dec']

theta = 0.5 * np.pi - np.deg2rad(dec)
phi = np.deg2rad(ra)
ipix = hp.ang2pix(nside, theta, phi)

data['status'] = credible_levels[ipix] <= 0.9

data.to_excel('/Users/nicolewolff/Desktop/ds9/GW170823_credible_region.xls')
