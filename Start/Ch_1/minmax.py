# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# # TODO: The min() function finds the minimum value
# print(f"This is min: {min(values)}")
# print(f"This is min: {min(strings)}")

# # TODO: The max() function finds the maximum value
# print(f"max={max(values)}")
# print(f"This is max: {max(strings)}")

# # TODO: define a custom "key" function to extract a data field
# print(f"min len={min(strings,key=len)}")
# print(f"This is max len: {max(strings,key=len)}")

# print(f"This is string len2 ******: {(len(strings))}")


# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
     data = json.load(datafile)

print(data["metadata"]["title"])
print("Features:", len(data["features"]))

def getmag(dataitems):
    meganitude = dataitems["properties"]["mag"]
    return 0 if meganitude is None else float(meganitude)


# print(getmag(data))
print(min(data["features"], key=getmag))
print(max(data["features"], key=getmag))
