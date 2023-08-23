# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json


def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True


# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"


def filterevn(x):
    if x % 2 == 0:
        return True
    else:
        return False


# TODO: use filter to remove items from a list
evn_nums = list(filter(filterevn, nums))
print(evn_nums)


def filter_upper(x):
    return True if x.isupper() else False


# TODO: use filter on non-numeric sequence
result_char = list(filter(filter_upper, chars))
print(result_char)

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


def not_quak(data):
    if data["properties"]["type"] == 'earthquake':
        return False
    else:
        return True


def quak(data):
    if data["properties"]["type"] != 'earthquake':
        return False
    else:
        return True

with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

events = list(filter(not_quak, data["features"]))
events_quak = list(filter(quak, data["features"]))

print("Number of non quacks =", len(events))
print("Number of quacks =", len(events_quak))

for i in range(0,10):
    print(events[i]["properties"]["type"])
    
