from math import radians, sin, cos, sqrt, atan2
import pandas as pd
def distanceCalc(lat1, lon1, lat2, lon2):
    # Function to calculate distance (in kilometers) between two points given their latitude and longitude
    R = 6371.0 
    # Earth's radius in kilometers 
    
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def compare(catalog1, catalog2):
    matches = 0
    numInCat1 = 0
    numInCat2 = 0
    
    for event1 in catalog1:
        matchFound = False
        print(event1)
        for event2 in catalog2:
            timeDiff = abs(event1['time'] - event2['time']) #cant subtract 2 time strings
            distance = distanceCalc(event1['latitude'], event1['longitude'], event2['latitude'], event2['longitude'])
            
            if timeDiff <= 5 and distance <= 25:
                matches+=1 #++ does not work in python 
                matchFound = True
                break
        
        if not matchFound:
            numInCat1+=1
            
    numInCat2 = len(cat2) - matches
    
    return matches, numInCat1, numInCat2
       

catalog_file1 = "earthquake_catalog.txt"
catalog_file2 = "earthquake_catalog2.txt"
data1 = pd.read_csv('earthquake_catalog.txt',sep= "\t",usecols = ['time','longitude','latitude'])

data2 = pd.read_csv('earthquake_catalog2.txt',sep= "\t", usecols = ['time','longitude','latitude'])
[matches, numInCat1, numInCat2] = compare(data1, data2)
print(matches)
print(numInCat1)
print(numInCat2)