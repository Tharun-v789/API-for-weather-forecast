import requests
import tkinter as tk
import geocoder
from geopy.geocoders import Nominatim


OPEN_WEATHER_MAP_API_KEY = 'cd3d2e0c8dad39f8240341670da00c9f'
OPEN_WEATHER_MAP_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'



def get_weather():
    input_value= input_field.get()
     # Try to get weather data directly using city name
    weather_query_params = {
        'q': input_value,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(
         OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    # Display weather data
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']}°C")


def get_location_weather():
    g = geocoder.ip('me')
    data=g.latlng
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Latitude & Longitude input
    Latitude = str(data[0])
    Longitude = str(data[1])
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']

    # traverse the data
    city = address.get('city', '')
    weather_query_params = {
        'q': city,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(
         OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    # Display weather data
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']}°C")
 
        
   

root = tk.Tk()
root.title("Weather Forecasting App")
root.geometry("400x200")


input_label = tk.Label(root, text="Enter city sz:")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack()

submit_button = tk.Button(root, text="Get Weather", command=get_weather)
submit_button.pack()

location_button = tk.Button(
    root, text="Use Current Location", command=get_location_weather)
location_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()


root.mainloop()
