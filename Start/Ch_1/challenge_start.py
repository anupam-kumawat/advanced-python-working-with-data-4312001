# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1:
print("Total quakes: ", len(data["features"]))

# 2:
print("Total quakes felt by at least 100 people: ", sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 100
                                                        for quake in data["features"]))

# 3:


def getReports(dataitem):
    reports = dataitem["properties"]["felt"]
    if (reports is None):
        reports = 0
    return reports


result = max(data["features"], key=getReports)
print("Most felt reports: ", "M", result["properties"]["mag"], "-",
      result["properties"]["place"], " reports: ", result["properties"]["felt"])

# 4:


def getSignificance(dataitem):
    sig = dataitem["properties"]["sig"]
    if sig is None:
        sig = 0
    return sig


data["features"].sort(key=getSignificance, reverse=True)

for i in range(0, 10):
    print("Event: ", "M", data["features"][i]["properties"]
          ["mag"], "-", data["features"][i]["properties"]["place"], "Significance: ", data["features"][i]["properties"]["sig"])
