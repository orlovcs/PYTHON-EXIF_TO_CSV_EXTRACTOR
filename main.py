import pysrt
import csv
import piexif

from os import walk
import geopy.distance



#get list of image names
imagelist = []
for filenames in walk('images/'):
     if (filenames[:3] == 'JPG' or filenames[:3] == 'PNG'):
          imagelist.append(filenames)
          
          
          
# from https://gist.github.com/erans/983821
def _convert_to_degress(value):
    d0 = value[0][0]
    d1 = value[0][1]
    d = float(d0) / float(d1)

    m0 = value[1][0]
    m1 = value[1][1]
    m = float(m0) / float(m1)

    s0 = value[2][0]
    s1 = value[2][1]
    s = float(s0) / float(s1)

    return d + (m / 60.0) + (s / 3600.0)

              
exifObj = piexif.load("images/DJI_0258.JPG")

               
eexifObj = piexif.load("images/DJI_0004.JPG")


coords_1 = (_convert_to_degress(exifObj["GPS"][piexif.GPSIFD.GPSLatitude]), _convert_to_degress(exifObj["GPS"][piexif.GPSIFD.GPSLongitude]))

coords_2 = (_convert_to_degress(eexifObj["GPS"][piexif.GPSIFD.GPSLatitude]), _convert_to_degress(eexifObj["GPS"][piexif.GPSIFD.GPSLongitude]))

distance_in_m = geopy.distance.vincenty(coords_1, coords_2).m
print(distance_in_m)



for srtgps in 






subs = pysrt.open('videos/DJI_0301.SRT')
lengthsrt = len(subs)

distance  = 50


myData = [["Time in Seconds", "Images within " + str(distance)  + "m"]]


#make csv template with timestamps
for i in range(0, lengthsrt):
     myData.append([str(subs[i].start.seconds) + " - " + str(subs[i].end.seconds) , 'placholder'])
  #  print(subs[i].text)
    
    
    


     
myFile = open('as.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")