from math import radians, sin, cos, sqrt, atan2

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


def compare(cat1, cat2):
    matches = 0
    numInCat1 = 0
    numInCat2 = 0
    
    for event1 in cat1:
        matchFound = false
        for event2 in cat2:
            timeDiff = abs(event1['time'] - event2['time'])
            distance = distanceCalc(event1['latitude'], event1['longitude'], event2['latitude'], event2['longitude'])
            
            if timeDiff <= 5 and distance <= 25:
                matches+=1 #++ does not work in python 
                matchFound = true
                break
        
        if not matchFound:
            numInCat1+=1
            
    numInCat2 = len(cat2) - matches
    
    return matches, numInCat1, numInCat2
        
