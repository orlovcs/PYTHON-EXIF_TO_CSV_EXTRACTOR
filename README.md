# PYTHON-EXIF_TO_CSV_EXTRACTOR


main.py creates a list of compatible image and video names using walk, it then then processes a srt file using pysrt and compares the geolocation of the subtitles in the srt file with the geolocation of every EXIF data extracted from each picture using piexif. geopy is then used to get the distance between the two locations and the compatible images are then pushed to a CSV file using the csv library.

mainPOI.py functions almost identically, however it interprets data from a CSV file into a 2D array, gathers the compatible images using the ordrered dictionaries longitude and latitude for comparisons for each row in the 2D array and then writes back exactly the same information to the CSV file adding the compatible image names to the last column.



! the _convert_to_degrees function is borrowed and is only used to convert values !
