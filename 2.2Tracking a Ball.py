# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:05:44 2020

@author: nishi
"""

#By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 2b-2b
# Date: 26 August 2020

'''So we have a ball being thrown and the goal is to figure out 
where in space it is at a given time. Alright lets go'''

'''
pos1 = input("Where did the ball start? Please insert commas: ")
arrpos1 = pos1.split(",")

x1 = int(arrpos1[0])
y1 = int(arrpos1[1])
z1 = int(arrpos1[2])

t1 = int(input("When was that? (in seconds): "))

pos2 = input("Where did the ball end up? Please insert commas: ")
arrpos2 = pos2.split(",")

x2 = int(arrpos2[0])
y2 = int(arrpos2[1])
z2 = int(arrpos2[2])

t2 = int(input("When was that? (in seconds): "))

t1_5 = int(input("When do you want to know the ball's position? (in seconds): ")) 
#1_5 bc the time is somewhere between 1 & 2

'''
#initializers because a computer cannot input things. I just added input statements 
#because they are fun also I say ball is thrown but there is no gravity bc constant speed

x1 = 1
y1 = 3
z1 = 7
t1 = 13

x2 = 23
y2 = -5
z2 = 10
t2 = 84

t1_5 = 50

'''
To find the mystery point I need to get the speed v then use v = x/t to calculate 
'''


timediff = t2 - t1

speedx = (x2-x1)/timediff 
speedy = (y2-y1)/timediff
speedz = (z2-z1)/timediff

#speed is slope m = delta y over delta x therefore delta pos over delta time 
#speedx = xmid - x1 / t1_5 - t1 and then rearrange 

#I just added a loop
while t1_5 < 54: 
    xmid = speedx * (t1_5-t1) + x1
    ymid = speedy * (t1_5-t1) + y1
    zmid = speedz * (t1_5-t1) + z1
    
    #print ("At t = " ,t1_5, " the ball is at (", xmid, ",", ymid,",",zmid, ")")
    print ("At time", t1_5, "seconds:")
    print ("x0 =",xmid,"m")
    print ("y0 =",ymid,"m")
    print ("z0 =",zmid,"m")
    print("---------------------")
    
    t1_5+=1

#I don't have this in the loop bc the 
#computer counted the extra line of hyphens wrong
xmid = speedx * (54-t1) + x1
ymid = speedy * (54-t1) + y1
zmid = speedz * (54-t1) + z1

print ("At time", 54, "seconds:")
print ("x0 =",xmid,"m")
print ("y0 =",ymid,"m")
print ("z0 =",zmid,"m")