import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def get_coords(location):
    geolocator = Nominatim()
    place = geolocator.geocode(location)
    return place.latitude, place.longitude
