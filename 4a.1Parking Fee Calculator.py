# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:31:07 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Mishra
# Rachel Spacek
# Presley Smith
# Section: 543
# Assignment: 4a-2 
# Date: 18 September 2020

#goal is to figure out the parking fee amount

#0-2 hrs - $4
#2-4 hrs - $3
#each additional hr is $1
#max per day is $24
#lost ticket  = $36
#and a lost ticket is denoted with a negative sign in the input 
#partial hours round up to a full hour

from math import *

hours = float(input("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.\nPlease enter the hours parked: "))

ticket_lost = False

if (hours < 0): #this sees if ticket is lost or not 
  ticket_lost = True


hrs_rounded = float(ceil(abs(hours))) #this forces 2.1 to become 3 #makes the hours positive if ticket lost

fee_amount = 0

if hrs_rounded == 0:
    fee_amount += 0
elif hrs_rounded <= 2:
  fee_amount = 4
elif hrs_rounded <= 4:
  fee_amount = 4 + 3
elif hrs_rounded < 24:
  fee_amount = 4 + 3 + (hrs_rounded - 4)
  if fee_amount > 24:
    fee_amount = 24 

elif hrs_rounded >= 24:
  days = hrs_rounded // 24
  fee_amount = days * 24
  leftover_hrs = hrs_rounded - days * 24 #gets the leftover hrs 
  
  if leftover_hrs == 0:
    fee_amount += 0
  elif leftover_hrs <= 2:
    fee_amount += 4
  elif leftover_hrs <= 4:
    fee_amount += 4 + 3
  elif leftover_hrs < 24:
    partial_fee = 4 + 3 + (leftover_hrs - 4)
    if partial_fee > 24:
      partial_fee = 24
    fee_amount += partial_fee 


if (ticket_lost == True):
  fee_amount += 36

print("Parking for", hours,"hours please pay $" + str(int(fee_amount)))





