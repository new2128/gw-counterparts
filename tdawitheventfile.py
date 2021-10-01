#TDA code, modified to include the FITS file 

from sklearn import datasets
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams
import numpy as np
from astropy.io import fits

fits_table_filename = fits.util.get_testdata_filepath('btable.fits')

hdul = fits.open('/Users/nicolewolff/eventfiles/second_event_fits_file.evt')  # open a FITS file
data2 = hdul[1].data  # assume the first extension is a table
first_two_rows = data2[:2]

#print(hdul[1].header['TTYPE2'])
xdata = hdul[1].data['X']
ydata = hdul[1].data['Y']
coords = []
for i, coord in enumerate(xdata):
    #mystring = ([str(coord)+ " "+ str(ydata[i])])
    #mylist = [coord, ydata[i]]
    #print(type(coord))
    coor_array=np.array([coord,ydata[i]], dtype=float)
    #print(coor_array)
    #coords.append(" ".join(map(str, mylist)))
    coords.append(coor_array)
#print(coords[0])
all_coors=np.array(coords)
print(len(all_coors))


data = datasets.make_circles(n_samples=80, factor=0.99)[0]
print(len(data))
#print((data))
#print(type(data[1][1]))
#print(type(data[1]))
#print(type(data[1]))
#print(coords[3])
plt.scatter(all_coors[:,0], all_coors[:,1])
diagrams = ripser(data)['dgms']
plot_diagrams(diagrams, show=True)
'''
for j, coord in enumerate(coords):
    plt.scatter(coords[j], coords[1])
    '''
'''
extra_circle_data = np.concatenate([datasets.make_circles(n_samples=80, factor=0.99)[0],
              3+0.03*datasets.make_circles(n_samples=80, factor=0.99)[0]])
plt.scatter(extra_circle_data[:,0], extra_circle_data[:,1])
'''
#diagrams = ripser(data)['dgms']
#plot_diagrams(diagrams, show=True)
plt.show()