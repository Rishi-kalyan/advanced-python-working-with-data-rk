# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value


# TODO: The max() function finds the maximum value


# TODO: define a custom "key" function to extract a data field


# TODO: open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)
with open("../../30DayQuakes.json","r") as datafile:
    data = json.load(datafile)
maglist = [(data["features"][i]["properties"]["mag"]) for i in range(0,len(data["features"]))]
#print(maglist)
def magfun(mags):
    magnitude = mags["properties"]["mag"]
    if magnitude == None :
        magnitude = 0
    return float(magnitude)
print(min(data["features"],key=magfun))
print(max(data["features"],key=magfun))