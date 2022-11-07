# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:40:23 2020

@author: nishi
"""

#message "xemtovhechyjsxuo"

#read the file
#key is a right shift of the 
#sum last five numbers  
#plus the  average of all of the numbers rounded down (to the whole number)
#plus the mode (the most common number in the file #use count 

with open("NumberDoc.txt", "r") as NumDoc:
    
    arr = NumDoc.readlines()
    
#sum last five numbers
sum_last_five = 0
ind = len(arr) - 1
i=0

while i < 5:
    sum_last_five += int(arr[ind]) 
    ind -= 1
    i += 1
#print(sum_last_five)

#avg + rounding 
avg = 0
count = 0
for i in range(len(arr)):
    avg += int(arr[i])
    count += 1
    
avg = (avg / count) // 1
print(avg)
#find the mode -- probably inefficient but who cares 
current_mode = -1 
num_occur_highest = 0
num_occur = 0 

for i in range(len(arr)):
    
    num_occur = arr.count(arr[i]) #find the num of instances of current element
    
    if num_occur > num_occur_highest:
        num_occur_highest = num_occur
        current_mode = int(arr[i])
        #print(current_mode, num_occur)
print("Mode",current_mode)

#add them up and get key?

key = sum_last_five + avg + current_mode
print("Key", key)
#decipher with a "key" number of right shifts 
#this number is way more than the alphabet and 26 right is the same letter 

key = key % 26 #to get the leftover actual shift
print("Key",key)
code = "xemtovhechyjsxuo"
ans = ""

for letter in code:
    char_num = ord(letter) + int(key)
    
    if char_num > ord("z"): 
        char_num = ord("a") + (char_num % ord("z") - 1) 
    
    ans += chr(char_num)

'''
char_num = 124 
if char_num > ord("z"): 
    char_num = ord("a") + (char_num % ord("z") - 1) 
'''

print(code)
print(key)
print(ans)

#print(chr(ord("a") + 1))
