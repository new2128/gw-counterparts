#the first plot is an aitoff projection of the 90% credible region from the txt file, the -3 to 3 latitude lines, and the average coordinate(s).
#the second plot is a 2d plot of longitude and latitude with the 90% credible regions from -3 to 3, the average point, and circles of radius 3.15deg
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


coordinates = []
mytup = tuple()
longitudes = []
latitudes = []
# open file and read the content in a list

with open('galactic.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        #currentPlace = line[:-1]

        # add item to the list
        if("SkyCoord" in line):
            next
        else:
            x = line.split(',')
            first = x[0].replace("( ", "")
            second = x[1].replace(")>","")
            l=float(first)
            b=float(second)
            mytup = tuple((l,b))
            coordinates.append(mytup)
            longitudes.append(l)
            latitudes.append(b)
longitudesrad=np.deg2rad(longitudes)
gal = SkyCoord(longitudes,latitudes, frame='galactic', unit=u.deg)
totallong=[]
k=0
while(k<360):
    totallong.append(k)
    k=k+1
gal2=SkyCoord(totallong,-3.000,frame='galactic',unit=u.deg)
gal3=SkyCoord(totallong, 3.000,frame='galactic',unit=u.deg)

from galacticavg import avgl
from galacticavg import avgb

avgcoord=SkyCoord(avgl,avgb,frame='galactic',unit=u.deg)


#plt.xticks(ticks=np.radians([-150, -120, -90, -60, -30, 0, \
                             #30, 60, 90, 120, 150]),
           #labels=['30°', '60°', '90°', '120°', '150°', '180°', \
                   #'210°', '240°', '270°', '300°', '330°'])

#change longitude from 0-360 to -180-180:

convertedcoord=SkyCoord(longitudes,latitudes,frame='galactic',unit=u.deg)
convertedlongitude = (convertedcoord.l.wrap_at('180d'))
convertedlongitudelist = []
convertedlongitudelist = convertedlongitude.degree
newlongitudes = convertedlongitudelist.tolist()
mystring = ""
for z in newlongitudes:
    zx = str(z) + " "
    mystring+=zx
f=0
if f < len(longitudes):
    k = mystring.split(" ")
    f=f+1
k.pop(31753)


filteredlatitudes = []
filteredlongitudes = []
firstlongitudelist = []
secondlongitudelist = []
firstlatitudelist = []
secondlatitudelist = []
m=0
#31753 is length of latitudes/longitudes list 
while m<31753:
    l=float(k[m])
    b=float(latitudes[m])
    if(-3<= b <=3):
        
        filteredlatitudes.append(b)
        filteredlongitudes.append(l)
        if(-50<=l<=50):
            firstlongitudelist.append(l)
            firstlatitudelist.append(b)
        else:
            secondlongitudelist.append(l)
            secondlatitudelist.append(b)
        
    m=m+1

firstavglongitude = sum(firstlongitudelist)/len(firstlongitudelist)
secondavglongitude = sum(secondlongitudelist)/len(secondlongitudelist)
firstavglatitude = sum(firstlatitudelist)/len(firstlatitudelist)
secondavglatitude = sum(secondlatitudelist)/len(secondlatitudelist)
gal4=SkyCoord(firstavglongitude,firstavglatitude,frame='galactic',unit=u.deg)
gal5=SkyCoord(secondavglongitude,secondavglatitude,frame='galactic',unit=u.deg)

print("firstavglongitude = ", firstavglongitude)
print("secondavglongitude = ", secondavglongitude)
print("firstavglatitude = ", firstavglatitude)
print("secondavglatitude = ", secondavglatitude)

#Plotting:
#fig=plt.figure(figsize=(8,6))
first_figure = matplotlib.pyplot.figure()
first_figure_axis = first_figure.add_subplot(111,projection='aitoff')
first_figure_axis.grid(True)
first_figure_axis.scatter(gal.l.wrap_at('180d').radian,gal.b.radian,s=1)
first_figure_axis.scatter(gal2.l.wrap_at('180d').radian,gal2.b.radian,s=1)
first_figure_axis.scatter(gal3.l.wrap_at('180d').radian,gal3.b.radian,s=1)
first_figure_axis.scatter(gal4.l.wrap_at('180d').radian,gal4.b.radian,s=10)
first_figure_axis.scatter(gal5.l.wrap_at('180d').radian,gal5.b.radian,s=10)
plt.title("Aitoff projection of 90% credible region of GW", y=1.08)
matplotlib.pyplot.xlabel('Long. in deg')
matplotlib.pyplot.ylabel('Lat. in deg')

#second_figure = matplotlib.pyplot.figure()
second_figure=plt.figure(figsize=(8,6))
second_figure_axis = second_figure.add_subplot(111, projection=None)
second_figure_axis.grid(True)
second_figure_axis.set(xlim=(-30, 180), ylim = (-10, 10))
second_figure_axis.scatter(firstavglongitude,firstavglatitude)
second_figure_axis.scatter(secondavglongitude,secondavglatitude)
circle1=plt.Circle((firstavglongitude,firstavglatitude),3.15)
circle2=plt.Circle((secondavglongitude,secondavglatitude),3.15)
second_figure_axis.add_artist(circle1)
second_figure_axis.add_artist(circle2)
second_figure_axis.scatter(filteredlongitudes,filteredlatitudes,s=1)


#first_figure.show()
#second_figure.show()
plt.show()





