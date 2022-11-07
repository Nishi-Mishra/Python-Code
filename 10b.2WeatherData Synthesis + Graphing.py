# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 10b-1
# Date: 31 October 2020


import numpy as np 
import matplotlib.pyplot as plt 

#make a line graph with avg temps and pressure against date
#make a histogram showing precipitation levels on x axis and y axis with num days 
#create a scatterplot of avg temp vs avg dew point 
#make a bar chart with a bar per month (all 3 yrs of data per month), showing the
#average temperature, along with lines indicating the highest high and lowest low temperatures

#for reference: Date(0),Temp High(1),Temp Avg(2),Temp Low(3),
#Dew Point High(4),Dew Point Avg(5),Dew Point Low(6),
#Humidity High(7),Humidity Avg(8),Humidity Low(9),
#Pressure High(10),Pressure Avg(11),Pressure Low(12),
#Precipitation (in.)(13)

tempdat = open("WeatherData.csv", "r")
#tempdat = open("one.csv", "r")

tempdat.readline()

avg_temps = [] 
avg_pressures = []
avg_dewPoints = []
precipitations = []
dates = []

monthTemp_data = { #avgs, highs, lows 
    1 : [[],[],[]],
    2 : [[],[],[]],
    3 : [[],[],[]],
    4 : [[],[],[]],
    5 : [[],[],[]],
    6 : [[],[],[]],
    7 : [[],[],[]],
    8 : [[],[],[]],
    9 : [[],[],[]],
    10 : [[],[],[]],
    11 : [[],[],[]],
    12 : [[],[],[]] #this is an initializer
    }


for next_ln in tempdat:
    arr = next_ln.split(",")
    arr[-1] = arr[-1].strip() 
    
    avg_temps += [float(arr[2])]
    avg_pressures += [float(arr[11])]
    precipitations += [float(arr[-1])]
    dates += [arr[0]]
    avg_dewPoints += [float(arr[5])]

    date = arr[0].split("/") #element 0 is the month 
    monthTemp_data[int(date[0])][0].append(float(arr[2])) #avg temps
    monthTemp_data[int(date[0])][1].append(float(arr[1])) #high temps 
    monthTemp_data[int(date[0])][2].append(float(arr[3])) #low temps


# monthTemp_data[1][0].append("Hi") #add actual data 
# print(monthTemp_data[1])
  
tempdat.close()


###################### Line Plot #############################
fig, ax1 = plt.subplots()
ax2 = ax1.twinx() #creates a plot which shares an x-axis 

ax1.plot(avg_temps, "r-", label = "Average Temps")
ax2.plot(avg_pressures, "b-", label = "Average Pressures")
fig.legend(loc = "lower left")
plt.suptitle("Avg Temperature and Pressure for Date Range")
ax1.set_xlabel("date")
ax1.set_ylabel("Average Temperature, F")
ax2.set_ylabel("Average Pressure, mmHg")
plt.show()

######################## Histogram #############################3

# the histogram of the data
n, bins, patches = plt.hist(precipitations, 100, facecolor='b')

plt.xlabel('Precipitation (in.)')
plt.ylabel('Number of Days')
plt.title('Histogram of Precipitation')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([-0.25, 8, 0, 35.5])
plt.show()

######################## Scatterplot #############################3
plt.scatter(avg_temps, avg_dewPoints, s=10, color = "black")
plt.suptitle("Dew Point vs. Temperature")
plt.xlabel("Average Temperature, F")
plt.ylabel("Average Dew Point, F")
plt.show()


######################## Bar/Line Graph #############################3

#data is in the dictionary called monthTemp_data by month; 
#first element is avg temps, second high temps and third low temps 
#graph needs one value for avg, high, low per month 

avgs_month = []
highs_month = []
lows_month = []
month_nums = [i for i in range(1, 13)] #fancy way of making an array with elements 1-12 
#print(month_nums)

#find monthly avgs 
for month in monthTemp_data:
    #print(monthTemp_data[month][0]) 
    avg_sum = 0
    for data in monthTemp_data[month][0]: 
        avg_sum += data
    avgs_month.append(avg_sum / len(monthTemp_data[month][0]))

#find monthly highs 
for month in monthTemp_data:
    high = max(monthTemp_data[month][1]) 
    highs_month.append(high)
    
#find monthly lows 
for month in monthTemp_data:
    low = min(monthTemp_data[month][2]) 
    lows_month.append(low)
    
plt.plot(month_nums, highs_month, color = "red", label = "High T")
plt.plot(month_nums, lows_month, color = "black", label = "Low T")
plt.bar(month_nums, avgs_month, color = "orange")
plt.suptitle("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Average Temperature, F")
plt.xticks(month_nums) #takes in the list of labels for x-axis
plt.legend()
plt.show()
