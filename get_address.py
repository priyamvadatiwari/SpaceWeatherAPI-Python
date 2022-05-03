import urllib.request
import json

def address(lat, lon):
    key = 'BINXbEGosKImGATS8RKAsLCIw0BZKGz7'
    url = f'http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())

    # print(result)
    return result
