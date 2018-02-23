import pysrt
import csv
import piexif

from os import walk
import geopy.distance





distance  = 35
distancePOI  = 50





videolist = []
for filenames in walk('videos/'):
     
     for i in filenames[2]:
          if (isinstance(i, str) and  i[-3:] == 'SRT'):
     
               videolist.append(i)
               
               
               
for srtfile in videolist:

     
     
     
     #get list of image names
     imagelist = []
     for filenames in walk('images/'):
          
          for i in filenames[2]:
               if (isinstance(i, str) and  i[-3:] == 'JPG'):
          
                    imagelist.append(i)
               
               
               
     # from https://gist.github.com/erans/983821
     def _convert_to_degress(value):
         """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
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
     #-------------------------------------
     
     
     
     
     
     
     
     subs = pysrt.open('videos/'+srtfile)
     lengthsrt = len(subs)
     
     
     myData = [["Time in Seconds", "Images within " + str(distance)  + "m"]]
     
     
     #make csv template with timestamps
     for i in range(0, lengthsrt):
      
          srtlong = [x.strip() for x in subs[i].text.split(',')] [0]
          srtlat = [x.strip() for x in subs[i].text.split(',')] [1]
          correctimglist = []
          
          
          for j in imagelist:
               
            
              file_path = ('images/'+j)  
              data = piexif.load(file_path)
              for key in ['Exif', '0th', '1st', 'GPS', 'Interop']:
                   key = 'GPS'
                   subdata = data[key]
                   if( piexif.GPSIFD.GPSLatitude  in subdata  and piexif.GPSIFD.GPSLongitude in subdata):
                        
                        
                  
                         
                        coords_1 = (_convert_to_degress(subdata[piexif.GPSIFD.GPSLatitude]), _convert_to_degress(subdata[piexif.GPSIFD.GPSLongitude]))
                        coords_2 = (srtlat, srtlong)
                      
                        distance_in_m = geopy.distance.vincenty(coords_1, coords_2).m
                      
                        if (distance_in_m <= distance):
                            correctimglist.append(j)
     
               
          
            
        
          myData.append([str(subs[i].start.seconds) + " - " + str(subs[i].end.seconds) , correctimglist])
          
          
     
         
         
     
     
          
     myFile = open('a.csv', 'w')
     with myFile:
         writer = csv.writer(myFile)
         writer.writerows(myData)
         
         
         

