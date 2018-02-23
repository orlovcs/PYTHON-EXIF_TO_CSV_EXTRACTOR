import pysrt
import csv
import piexif

from os import walk
import geopy.distance





distancePOI  = 50



#POI
results = []
with open('assets.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
        print(row)

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

    r = results[0]
    myData = [list(r.keys())]
    
    #make csv template with timestamps
    for i in results:
     
         srtlong = i['longitude']
         srtlat = i['latitude']
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
                       
                     
                       if (distance_in_m <= distancePOI):
                           correctimglist.append(j)
    
              
         
           
       
         i["image_names"]=correctimglist
         
         myData.append([i["asset_name"], i['longitude'],  i['latitude'],  i["image_names"]])
         
         
    
        
        
    
    
         
    myFile = open('assets.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)


