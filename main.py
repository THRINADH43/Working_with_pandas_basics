import csv

#with open("weather_data.csv","r") as weatherdata:
#    complete_data=weathered.readlines()
#    print(complete_data)
#with open(file="weather_data.csv",mode='r') as weather_data:
#    new_data=csv.reader(weather_data) #csv.reader is an in built function of csv files.
#    #print(new_data)
#    for data in new_data:
#        print(data)  # same as above

# Challenge -2
# Create a new list and it should contain the temperate as integer and should avoid the string.

#with open(file="weather_data.csv",mode='r') as weather_data:
#    complete_data=csv.reader(weather_data)
#    temperature=[]
#    for data in complete_data:
#        if (data[1]=="temp"):
#            continue
#        new_data=int(data[1])
#        temperature.append(new_data)
#    print(temperature)                   # challenge completed

import pandas as pd
data=pd.read_csv("weather_data.csv")
#print(data)
print(data["condition"])  # easier than previous challenge




