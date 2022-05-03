import urllib.request
import json
filename = "countryinfo.json"
def country(name):
    url = f'https://restcountries.com/v3.1/alpha/{name}'
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    # print(f"This is new info {result}")

    with open(filename, 'w') as jsonFile:
      jsonFile.write(json.dumps(result, indent=3))
  
    return result

