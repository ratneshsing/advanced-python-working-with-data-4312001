# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
# 1: How many quakes are there in total?
print("1.How many quakes are there in total ? ",len(data["features"]))

def df_felt(df):
    return df["properties"]["felt"] if df["properties"]["felt"] is not None else 0

print("2.How many quakes were felt by at least 100 people? ")
print(sum(data["properties"]["felt"] is not None and data["properties"]["felt"] >=100
      for data in data["features"]))

print("3.Print the name of the place whose quake was felt by the most people,\
with the # of reports")
def felt(d):
    if d["properties"]["felt"] is not None:
        return (d["properties"]["felt"])
    else:
        return 0

data["features"].sort(key=felt,reverse=True)
for i in range(0,5): # data["features"]:
    print(data["features"][i]["properties"]["place"],
          data["features"][i]["properties"]["felt"])
#print(sorted(data["properties"]["felt"], key=felt, reverse=True))

def signeficant(d):
    sign = d["properties"]["sig"]
    if sign is None:
        return 0 
    else:
        return sign


print("4. Print the top 10 most significant events, with the significance value of each")
data["features"].sort(key=signeficant, reverse=True)
for i in range(0,10):
    print(data["features"][i]["properties"]["title"],
          data["features"][i]["properties"]["sig"])
