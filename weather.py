import requests


from datetime import datetime

api_key = 'ca3c4e02310df90a1e1e03850154725a'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')

with open('weather.txt', 'w') as f:
    f.write(location+'\n')
    f.write(api_key+'\n')
    f.write(date_time+'\n')
    f.write(str(temp_city)+'\n')
    f.write(weather_desc+'\n')
    f.write(str(hmdt)+'\n')
    f.write(str(wind_spd)+'\n')