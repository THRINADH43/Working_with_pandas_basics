# Continuing to work with given data set and with rows and columns in the data.
import pandas
import pandas as pd
data=pd.read_csv("weather_data.csv")
#print(data)
#print(type(data["temp"]))
#print(type(data))
#print(type(data["day"]))
#print(type(data["condition"]))

# single sheet is called Series like a single column.
# multiple sheets are called as Data Frames like multiple column.

# csv to dictionary
#data_dict=data.to_dict()
#print(data_dict)

# series to list
#data_list=data["temp"].to_list()  # converting a series to list
#print(data_list)


# challenge = calculate the average temparutes.
data_list=data["temp"].to_list()
#sum=sum(data_list)  # use the function sum() to calculate the sum of numbers in list.
#average=sum/len(data_list)
#print(f"{average:.2f}")

#print(data["temp"].mean())  # using the mean function from the series of pandas.

# challenge to find the maximum temperature using the series documentation
#max=data["temp"].sort_values(ascending=False)
#print(f"maximum value= {max.to_list()[0]}")
#print(data["temp"].max())
# another way

# getting data in rows.
#print(data[data.temp== 24])

# challenge is to print out the row with maximum temperature.
#maximum_temp=data["temp"]
#max_temp=maximum_temp.max()
#print(data[data.temp== max_temp])
# challenge completed.

# challenge is to get monday's temperature in farenheit scale
#monday=data[data.day== "Monday"]
#monday_celsius=monday.temp
#monday_farenheit=((9*monday_celsius)/5)+32
#print(monday_farenheit)
# challenge completed.

# create a Data Frame from scratch.
data_dict={
    "students" : ["Any","James","Angela"],
    "scores": [76,56,65]
}
data=pandas.DataFrame(data_dict)
print(data)
print(data.to_csv("new_data.csv"))



