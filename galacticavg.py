#fundamental code for finding an average coordinate. first should plot the 90% credible regions, because if there are two regions this will not work.
#if there is only one region, generate this average and then plot it in the region to make sure it is a good approximation of the center 

coordinates = []
mytup = tuple()
longitudes = []
latitudes = []
# open file and read the content in a list

with open('galactic.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        

        # add item to the list
        if("SkyCoord" in line):
            next
        else:
            x = line.split(',')
            first = x[0].replace("( ", "")
            second = x[1].replace(")>","")
            l=float(first)
            b=float(second)
            if(-3<= b <=3):
                mytup = tuple((l,b))
                coordinates.append(mytup)
                longitudes.append(l)
                latitudes.append(b)
print(len(coordinates))
print(sum(longitudes)/len(longitudes))
avgl=sum(longitudes)/len(longitudes)
print(sum(latitudes)/len(latitudes))
avgb=sum(latitudes)/len(latitudes)
