#Created on Wed Aug 26 19:10:32 2020


#By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name: Nishi Mishra
# Section: 543
# Assignment: Lab 2b-3
# Date: 26 August 2020

#Code must consist of only the following lines of code to produce the
#output shown below. 

#Your program should print out the following, when run:
#1
#24
#321
#10000000000000000 [Note: that’s 10^16]
#1234


#x = 1
#y = 10
#z = 0
#x = y
#x += 1
#y += x
#y *= x
#z += x
#z += y
#print(z)
#You may also use blank lines and single line # comments in your code

z = 0
x = 1
z += x
print(z) #AAAA I got 1

z = 0
x += 1 # x=2 now 
y = 10
y *= x #y=20
y += x 
y += x #y=24
z += y #z has the hot potato
print(z) #Annddd score!! We got 24 down


z = 0 
x = 1
z += x #z has the ones digit
x += 1 # x=2
y = 10
y *= x 
z += y #we have the tens digit
x += 1 # x=3
y = 10 
y *= x #y=30
x = y # x=30 now
y = 10 
y *= x #x times y is 30 times 10 
z += y #aand we have all the places (I am going cross-eyed)
print(z)


y = 10
x = y # x=10^1
y *= x # y=10^2
x = y 
y *= x #10^4
x = y 
y *= x #10^8
x = y 
y *= x #10^16 
z = 0
z += y #z = 10^16 
print(z) # finallyyy jeez scientific notation was hard

x = 1 
y = 10
x = y 
y *= x # y=100
y *= x # y=1000
z = 0
z += y #we have 1000 in the box
y = 10 #x=10
y *= x # y=100
x = 1
x += 1
y *= x #finally have 200 this is so hard
z += y
x += 1 # x=3
y = 10
y *= x #30
z += y #tens digit
x += 1 # x=4
z += x 
print(z)


