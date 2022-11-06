# -*- coding: utf-8 -*-
# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra  
# Section: 543
# Assignment: 9b-1
# Date: 27 October 2020

celcius_data = open("Celsius.txt", "r")

fahr = []

for next_ln in celcius_data:
    celcius = float(next_ln.strip())
    
    fahr += [(celcius * 9/5) + 32]

celcius_data.close()

#take in the values and output results with two (2) decimal places, right justified, with a 10 character width

fahr_data = open("Fahrenheit.txt", "w")

for f in fahr:
    fahr_data.write("{:.2f}\n".format(f).rjust(11))

fahr_data.close()

