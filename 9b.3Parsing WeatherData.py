# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 9b-3
# Date: 27 October 2020

#the maximum temperature seen over the 3-year period
#the minimum temperature seen over the 3-year period
#the avg daily precipitation seen over the 3-year period (2 decimals)


#Get input for month and year; then for that month:
# Calculate the average of the low temperatures (use 1 decimal place)
# Calculate the percentage of days when the average humidity was below 75% (use 1 decimal place)
# Calculate the mean and standard deviation of the daily precipitation levels (use 4 decimal places)

#find the month and make a low temp array 
#count the num of days in month & count the num of days with avg humidity less than 75% 
#we already have a precip array just do that calcs needed 

month = 1
year = 2015

tempdat = open("WeatherData.csv", "r")
#tempdat = open("one.csv", "r")

tempdat.readline()

min_temps = [] 
max_temps = []
precipitations = []
'''
month_min_temps = [] #this was moved below bc we need to ask user input in the middle of the code unfortunately
month_avg_humidity = []
month_precipitations = []
'''
for next_ln in tempdat:
    arr = next_ln.split(",")
    arr[-1] = arr[-1].strip() 
    
    min_temps += [float(arr[3])]
    max_temps += [float(arr[1])]
    precipitations += [float(arr[-1])]
    
    '''
    ##### Below starts monthly data arrays ######
    date = arr[0].split("/")
    
    if int(date[0]) == month and int(date[-1]) == year:
        month_min_temps += [float(arr[3])]
        month_avg_humidity += [float(arr[8])]
        month_precipitations += [float(arr[-1])]
     '''   
tempdat.close()

#find max temp
max_temp = max_temps[0]

for maxT in max_temps:
    
    if maxT > max_temp:
        max_temp = maxT

#find min temp 
min_temp = min_temps[0]

for minT in min_temps:
    
    if minT < min_temp:
        min_temp = minT


avg_precip = 0
#find avg preciptiations         
for precip in precipitations:
    avg_precip += precip 
avg_precip /= len(precipitations)

#print it all nicely!

print("3-year maximum temperature: %d F" % max_temp)
print("3-year minimum temperature: %d F" % min_temp)
print("3-year average precipitation: %.2f inches" % avg_precip)


#################### Next Part ####################

#getting monthly data from file!
monthname = input("\nEnter a month: ")
year = int(input("Enter a year: "))

#dictionary of months 
dict_months = {
    "January": 1,
    "February": 2,
    "March": 3, 
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12  
    }

month = dict_months[monthname]


tempdat = open("WeatherData.csv", "r")
#tempdat = open("one.csv", "r")

tempdat.readline()

month_min_temps = []
month_avg_humidity = []
month_precipitations = []

for next_ln in tempdat:
    arr = next_ln.split(",")
    arr[-1] = arr[-1].strip() 
    
    ##### Below starts monthly data arrays ######
    date = arr[0].split("/")
    
    if int(date[0]) == month and int(date[-1]) == year:
        month_min_temps += [float(arr[3])]
        month_avg_humidity += [float(arr[8])]
        month_precipitations += [float(arr[-1])]
        
tempdat.close()


### Monthly Calcs ###

#avg low temp within the month 
avg_lowT = 0
for minT in month_min_temps:
    avg_lowT += minT
avg_lowT /= len(month_min_temps)

#find percent of days with avg humidity below 75%
day_count = 0
days_not_humid = 0 
for avg_humidity in month_avg_humidity:
    day_count += 1
    
    if avg_humidity < 75 : #humidity is a whole number not 0.25 etc. 
        days_not_humid += 1
        
percent_days_not_humid = days_not_humid / day_count * 100 

#get the mean precip 
mean_precip = 0
for precip in month_precipitations:
    mean_precip += precip
mean_precip /= len(month_precipitations) 

#get std deviation of precips 
sum_squares = 0
for precip in month_precipitations:
    sum_squares += (precip - mean_precip) ** 2
std_deviation = (sum_squares / len(month_precipitations)) ** (1/2)


#print answers
print("\nFor", monthname, str(year) + ":")
print("Average low temperature: %0.1f F" % avg_lowT)
print("Percentage of days with average humidity below 75%%: %.1f%%" % percent_days_not_humid)
print("Mean daily precipitation: %.4f inches" % mean_precip)
print("Standard deviation of daily precipitation: %.4f inches" % std_deviation)


#for reference: Date(0),Temp High(1),Temp Avg(2),Temp Low(3),
#Dew Point High(4),Dew Point Avg(5),Dew Point Low(6),
#Humidity High(7),Humidity Avg(8),Humidity Low(9),
#Pressure High(10),Pressure Avg(11),Pressure Low(12),
#Precipitation (in.)(13)