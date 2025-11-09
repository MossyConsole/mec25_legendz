from geopy.geocoders import Nominatim


def list_of_nearby_areas(lat, longi, list):
    loc = Nominatim(user_agent="sunnyside_app")
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            print(i, j)
            location = loc.reverse(str(i/2+lat) + ", " + str(j/2+longi))
            print(location)
            if not(location in list):
                list.append(location)

if  __name__ == "__main__":
    l = []
    loc = Nominatim(user_agent="sunnyside_app")
    getLoc = loc.geocode("Toronto, Canada")
    list_of_nearby_areas(getLoc.latitude, getLoc.longitude, l)
    print(l)