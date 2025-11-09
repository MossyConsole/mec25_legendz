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

def list_of_nearby_areas_with_api(lat, longi, list):
    api = WeatherBit_Caller


    loc = Nominatim(user_agent="sunnyside_app")
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            print(i, j)
            location = loc.reverse(str(i/2+lat) + ", " + str(j/2+longi))
            data = api.request(api, i/2+lat, j/2+longi)
            print(location)
            print(data)
            if not(location in list) and data["alerts"] != []:
                list.append([location, data["alerts"][0]["severity"]])


if  __name__ == "__main__":
    l = []
    loc = Nominatim(user_agent="sunnyside_app")
    getLoc = loc.geocode("Toronto, Canada")
    list_of_nearby_areas_with_api(getLoc.latitude, getLoc.longitude, l)
    print(l)

def nearest_tab(ttk, tab):
    ttk.Label(tab, 
            text = "Nearby Areas", font=("Browallia new", 24)).pack(padx=100, pady=(0,100))
    ttk.Button(tab, text="Generate", command=lambda : nearest_city_create).pack(padx = "100", pady = 10)
    

    l = []
    list_of_nearby_areas_with_api(lat, longi, l)

    for i in l:
        ttk.Label(tab, 
            text = i[0] + " " + i[1], font=("Browallia new", 40)).pack(padx=100, pady=(0,100))

def nearest_city_create(ttk):
    file = open("sunny_data\location.txt", "r")
    latlongtext = file.readline();
    latlongarr = latlongtext.split(";")
    lat = float(latlongarr[0])
    longi = float(latlongarr[1])