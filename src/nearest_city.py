from geopy.geocoders import Nominatim
from api_caller import WeatherBit_Caller
import json


def list_of_nearby_areas(lat, longi, list):
    loc = Nominatim(user_agent="sunnyside_app")
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            print(i, j)
            location = loc.reverse(str(i/2+lat) + ", " + str(j/2+longi))
            print(location)
            if not(location in list):
                list.append(location)

def list_of_nearby_areas_with_api(lat, longi, list, ttk, tab):
    api = WeatherBit_Caller()


    loc = Nominatim(user_agent="sunnyside_app")
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            print(i, j)
            location = loc.reverse(str(i/2+lat) + ", " + str(j/2+longi))
            data = api.request(i/2+lat, j/2+longi)
            print(location)
            print(data)
            if not(location in list):
                if data["alerts"] != []:
                    m = ttk.Label(tab, text = str(location) + " " + data["alerts"][0]["severity"], font=("Browallia new", 8), foreground = "red")
                    m.pack(padx=100, pady=4)
                    m.update_idletasks()
                else:
                    m = ttk.Label(tab, text = str(location) + " " + "Safe", font=("Browallia new", 8), foreground = "green")
                    m.pack(padx=100, pady=4)
                    m.update_idletasks()
                list.append(location)
                


def nearest_tab(ttk, tab):
    ttk.Label(tab, 
            text = "Nearby Areas", font=("Browallia new", 24)).pack(padx=100, pady=(0,20))
    ttk.Button(tab, text="Generate", command=lambda : nearest_city_create(ttk, tab)).pack(padx = "100", pady = 10)
    

    

    

def nearest_city_create(ttk, tab):
    
    file = open("sunny_data\location.txt", "r")
    latlongtext = file.readline();
    latlongarr = latlongtext.split(";")
    lat = float(latlongarr[0])
    longi = float(latlongarr[1])
    list_of_nearby_areas_with_api(lat, longi, [], ttk, tab)

        