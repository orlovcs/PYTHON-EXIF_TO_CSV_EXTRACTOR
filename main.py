import pysrt
import csv




subs = pysrt.open('videos/DJI_0301.SRT')

lengthsrt = len(subs)
print(subs[0].text)

distance  = 50


myData = [["Time in Seconds", "Images within " + str(distance)  + "m"]]


#make csv template with timestamps
for i in range(0, lengthsrt):
     myData.append([str(subs[i].start.seconds) + " - " + str(subs[i].end.seconds) , 'placholder'])
    
  #  print(subs[i].start.seconds)
  #  print(subs[i].end.seconds)
  #  print(subs[i].text)
    
    
    


     
myFile = open('as.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")