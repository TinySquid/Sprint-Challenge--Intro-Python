# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return f"{self.name} {self.lat} {self.lon}"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

# How is the CSV layed out? - First line describes fields
# What does the first line look like? - city,state_name,county_name,lat,lng,population,density,timezone,zips
# What information do we want from this file? - city, lat, lng
# Where do we want to store this information? - Each city into a City instance and appended to a cities list

# Read cities.csv, add each city with lat, lon to a City instance and append to cities list
# Import csv module
import csv


def cityreader(cities=[]):
    # For each city record, create a new City instance and add it to the
    # `cities` list

    # Open csv file
    with open("cities.csv") as csv_file:
        # Create csv reader
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Skip header
        next(csv_reader)

        # Read csv rows, create City instances and append to cities list
        for row in csv_reader:
            cities.append(City(row[0], row[3], row[4]))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = float(lat)
        self.lon = float(lon)

    def __str__(self):
        return f"Lat: {self.lat} | Lon: {self.lon}"


# Get lat / lon points from user
pointA = input("Enter first point (lat lon) -> ")
pointB = input("Enter second point (lat lon) -> ")

pointA = pointA.split(" ")
pointB = pointB.split(" ")


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

    # Normalize the input lat/lon
    if lat1 > lat2:
        # Top is lat1
        if lon1 > lon2:
            # Top right
            coordA = Coordinate(lat1, lon1)
            coordB = Coordinate(lat2, lon2)
        else:
            # Top left
            coordA = Coordinate(lat1, lon2)
            coordB = Coordinate(lat2, lon1)
    else:
        # lat/lon 2 will be top
        if lon2 > lon1:
            # Top right
            coordA = Coordinate(lat2, lon2)
            coordB = Coordinate(lat1, lon1)
        else:
            # Top left
            coordA = Coordinate(lat2, lon1)
            coordB = Coordinate(lat1, lon2)

    # within will hold the cities that fall within the specified region
    within = []

    # Go through each city and check to see if it falls within
    # the specified coordinates.
    for city in cities:
        if city.lat <= coordA.lat and city.lat >= coordB.lat:
            if city.lon <= coordA.lon and city.lon >= coordB.lon:
                within.append(city)

    return within


foundCities = cityreader_stretch(
    float(pointA[0]), float(pointA[1]), float(pointB[0]), float(pointB[1]), cities
)

for city in foundCities:
    print(city)
