# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:           Nishi Mishra 
# Section:        543
# Assignment:     Lab 12b 
# Date:           21 November 2020

#Note: I did the challenge. When running, choose the type of Roman conversion you want: 
#Additive is for the regular lab and Traditional/Standard is for the challenge part
#PS I added a try-except block so feel free to type bad input and see if it catches it 


#need to draw the various symbols: I V X l C D M   
#every function ends with the turle pointing -> with the pen down for consistency 
#every function also returns the amount of pixels needed for that letter

from turtle import * 

def positionStart():
    ''' Positions the starting cursor near the top left corner of the screen '''
    penup() #position start 
    back(650) #left
    left(90)
    forward(300-90) #up 
    right(90)
    pendown()
    
def nextLinePos(pixelamountback): 
    '''
    This function is never called it was supposed to move to the next line 
    if there was not enough space for the letters. This takes in the amount of 
    pixels used up by letters so far and go back a that same amount to a new line.
    
    If the screen is maximized, there is no need for this. 
    '''
    penup()
    right(90)
    forward(150)
    left(90)
    back(pixelamountback)
    pendown()

def drawI():
    '''Draws the letter I and moves over with the cursor oriented --> at the end'''
    length = 85
    
    left(90) #I 
    forward(length) #up 
    back(length)
    right(90)
    penup()
    forward(30) #move for the next letter 
    pendown()
    
    return 30 
    
def drawV():
    '''Draws the letter V and moves over with the cursor oriented --> at the end'''
    length = 90 
    
    penup()
    forward(20) #give some space 
    pendown()
    left(110) # V #the left side
    forward(length) #length
    back(length)
    right(40) # 110 - 90 = 20 so the same angle on the onther side requires double 20
    forward(length) #length 
    back(length)
    right(70) # 110-40 = 70 to get back on the plane 
    penup()
    forward(60) #move for next letter 
    pendown()
    
    return 65

def drawX():
    '''Draws the letter X and moves over with the cursor oriented --> at the end'''
    length = 100
    penup() # X
    forward(50) #so there is more space to draw
    pendown()
    left(120) #draws \
    forward(length)
    back(length)
    left(60) #makes the arrow right side flat 180-120 = 60 
    penup()
    forward(50) #to start the other half 
    pendown()
    right(120) # daws / exact opposite of previous leg  
    forward(length)
    back(length)
    right(60) #returns to flatline __
    penup()
    forward(90) # move for the next letter 
    pendown()
    
    return 85 

def drawL():
    '''Draws the letter L and moves over with the cursor oriented --> at the end'''
    forward(40) #l
    back(40) #short part
    left(90)
    forward(85) #long part
    back(85) 
    right(90)
    penup()
    forward(60) #move over 
    pendown()
    
    return 70

def drawC():    
    '''Draws the letter C and moves over with the cursor oriented --> at the end'''
    penup() # C
    forward(40) #give some space 
    left(90) #makes pen |
    pendown()
    
    left(100) #make the pen start at an angle tostart on C 
    forward(20) #starts the first line 
    for i in range(8):
        right(25) #turns a bit each loop 
        forward(20)
    
    for i in range(8): # take it back now ya'll
        back(20)
        left(25)
    back(20)
    right(100) 
    
    penup()
    right(90)
    forward(25) #move for the next character 
    pendown()
    
    return 80

def drawD():
    '''Draws the letter D and moves over with the cursor oriented --> at the end'''
    left(90) # D 
    forward(90) #straight line 
    
    right(100)
    forward(20)
    for i in range(6):
        right(25) #turns a bit each loop 
        forward(20)
    right(10)
    forward(10)
    
    back(10) #take it back now y'all
    left(10)
    for i in range(6): 
        back(20)    
        left(25)
    back(20)
    left(100)
    
    back(90)
    left(90)
    
    penup()
    left(180)
    forward(80) #move for next character 
    pendown()
    
    return 80

def drawM():
    '''Draws the letter M and moves over with the cursor oriented --> at the end'''
    left(90) # M 
    forward(90) #first |
    left(35) # og angle 
    backward(50) # \
    right(70) #same angle og doubles 
    forward(50) # / 
    left(35) #same angle as og 
    backward(90)
    
    right(90) #flatline
    penup()
    forward(40) #move over a bit 
    pendown()
    
    return 85
    

#I V X l C D M   #this block helped determine how much space each letter needs 

# positionStart() 
# print("I", drawI()) #this is how much space each letter takes 
# print("V", drawV())
# #nextLinePos(100) #nextline code 
# print("X", drawX())
# print("L", drawL())
# print("C", drawC())
# print("D", drawD())
# print("M", drawM())

# penup()
# right(90)
# forward(20)
# left(90)
# back(550) #this mess forced the turtle to the start of the letters then I measured the width of each letter 
# pendown() #I never used this information 
# forward(30) # I
# penup()
# forward(5)
# pendown()
# forward(65) # V
# penup()
# forward(5)
# pendown()
# forward(85) # X
# penup()
# forward(5)
# pendown()
# forward(70) # L
# penup()
# forward(5)
# pendown()
# forward(80) # C
# penup()
# forward(5)
# pendown()
# forward(80) # D
# penup()
# forward(5)
# pendown()
# forward(85) # M


# =============================================================================
                                # MAIN CODE #
# =============================================================================


print("\nPlease maximize turtle window! \nBy the way this does catch bad user input if you want to try. \n")
num_good = False 
user_num = input("Enter a number to convert into Roman Numerals: ")
while num_good == False:
    try:
        if not (0 < int(user_num) <= 3999):
            user_num = input("Invalid number. Number must be between 1 - 3999. Enter a number to convert into Roman Numerals: ")
        else:
            num_good = True 
            #print("Got it!")
    except:
        user_num = input("This must be an integer (not letters nor decimals) from 1 to 3999. Enter a number to convert into Roman Numerals: ")
    
type_good = False   
type_conv = input("What type of conversion would you like? Additive(1) or Traditional/Standard(2): ")
while type_good == False:
    try:
        if not (1 <= int(type_conv) <= 2):
            type_conv = input("Invalid number. You must choose 1 or 2. Enter the type of conversion. Additive(1) or Traditional/Standard(2):  ")
            #print("here")
        else:
            type_good = True 
            #print("Why are you here?")# -- it works now 
    except:
        type_conv = input("This must be an integer (not letters nor decimals). Namely 1 or 2. Please enter the type of conversion. Additive(1) or Traditional/Standard(2):  ")

num = user_num
num_list_form = []
i = 0
while len(num_list_form) != 4:
    if i < len(num):
        num_list_form += [int(num[i])]
        i += 1
    else:
        num_list_form.insert(0, 0)


tracer(0,0) #this coupled with the update() statement make the drawing draw behind the scenes and update *instantly* for human purposes
hideturtle()

positionStart()

#call the various functions 

#additive notation 
if type_conv == "1":
    if 3 >= num_list_form[0] > 0: #first digit 
        for i in range(num_list_form[0]):
            drawM()
            
    if 4 >= num_list_form[1] > 0: #second digit 
        for i in range(num_list_form[1]):
            drawC()
    elif 9 >= num_list_form[1] > 4: 
        drawD()
        for i in range(num_list_form[1] - 5):
            drawC()
            
    if 4 >= num_list_form[2] > 0: #third digit 
        for i in range(num_list_form[2]):
              drawX()
    elif 9 >= num_list_form[2] > 4: 
        drawL()
        for i in range(num_list_form[2] - 5):
            drawX()
            
    if 4 >= num_list_form[3] > 0: #fourth digit 
        for i in range(num_list_form[3]):
            drawI()
    elif 9 >= num_list_form[3] > 4: 
        drawV()
        for i in range(num_list_form[3] - 5):
            drawI()

#do traditional roman numerals 
elif type_conv == "2":
    if 3 >= num_list_form[0] > 0: #first digit 
        for i in range(num_list_form[0]):
            drawM()
            
    if 3 >= num_list_form[1] > 0: #second digit 
        for i in range(num_list_form[1]):
            drawC()
    elif num_list_form[1] == 4:
        drawC()
        drawD()
    elif 9 > num_list_form[1] >= 5: 
        drawD()
        for i in range(num_list_form[1] - 5):
            drawC()
    elif num_list_form[1] == 9:
        drawC()
        drawM()
            
    if 3 >= num_list_form[2] > 0: #third digit 
        for i in range(num_list_form[2]):
            drawX()
    elif num_list_form[2] == 4:
        drawX()
        drawL()
    elif 9 > num_list_form[2] >= 5: 
        drawL()
        for i in range(num_list_form[2] - 5):
            drawX()
    elif num_list_form[2] == 9:
        drawX()
        drawC()
            
    if 4 > num_list_form[3] > 0: #fourth digit 
        for i in range(num_list_form[3]):
            drawI()
    elif num_list_form[3] == 4:
        drawI()
        drawV()
    elif 9 > num_list_form[3] > 4: 
        drawV()
        for i in range(num_list_form[3] - 5):
            drawI()
    elif num_list_form[3] == 9:
        drawI()
        drawX()

#create function which moves the cursor if exceed a certain amount of pixels -- not happening. I am done 

update() #makes the code run instantaneously for testing purposes 
done()
bye()
