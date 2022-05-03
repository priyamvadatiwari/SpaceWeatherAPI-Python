from flask import Flask, render_template
from get_distance import dist
from get_address import address
from get_country import country
from get_iss import iss_loc
from get_weather import get_weather


#import everything

app = Flask('app')

@app.route('/')
def iss_data():
  data = []
  #connect to each module, download and return data
  #send data to flask page (connect to jinja)

  issLocation = iss_loc()
  lat, lon = issLocation[0], issLocation[1]

  #43.590086,-79.6509581  --360 Square One Drive, Mississauga, ON
  #distance from the iss
  distance = dist(43.590086,-79.6509581,lat,lon) #your location and the location of the ISS in lat/lon
  dist_ = f"You are {distance}km from the ISS"
  data.append(dist_)
  
  #weather
  weather = get_weather(lat, lon)
  #print(weather)
  temp_c = round(weather["main"]["temp"] - 273.15,2)
  temperature = f"Current temperature is {temp_c} degree Celcius"
  desc = weather["weather"][0]['description']
  description = f"Current weather at the space station shows : {desc}"
  # print(str(temp_c)+"C", desc)

  #get ISS location
  issloc = iss_loc()
  #get country Name
  getaddress = address(lat,lon)
  # print("Country code",getaddress["results"][0]['locations'][0]["adminArea1"])
  countryInfo = ""

  desc_country = []
  if getaddress["results"][0]['locations'][0]["adminArea1"] == "XZ":
    countrycode = f"The ISS is over water"
    # print('the ISS is over water')
    flag = 'https://media.istockphoto.com/photos/blue-sea-or-ocean-water-surface-and-underwater-with-sunny-and-cloudy-picture-id1197623205?k=20&m=1197623205&s=612x612&w=0&h=lraPEr-aoqmFO5LsuEulv77jZZVCL5ojHaU1RYPzxeg='
    # print(flag)
    desc_country.append("Nothing to say here!")
  else:
    location = getaddress["results"][0]['locations'][0]["adminArea1"]
    countrycode = f"Current Location is over {location}"
    flag = country(location)[0]["flags"]["png"]
    countryName = country(location)[0]["name"]["common"]
    officialName = f"Official Name is {country(location)[0]['name']['official']}"
    capital = f"Capital is {country(location)[0]['capital']}"
    desc_country.append(countryName)
    desc_country.append(officialName)
    desc_country.append(capital)

    
  # Latitude and Longitude of ISS
  countryInfo = f"Iss is currently located in {issloc}"

  
  data.append(temperature)
  data.append(description)
  data.append(countryInfo)
  data.append(countrycode)
  data.append(flag)
  
  return render_template("index.html",data=data, desc_country=desc_country)

app.run(host='0.0.0.0', port=8080)
