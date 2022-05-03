import urllib.request
import json

def get_weather(lat, lon):
    """
    Get the weather at a given location
    """
    key = 'c17856fae46dcfdee7fb3ae1a4301558'
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    return result
