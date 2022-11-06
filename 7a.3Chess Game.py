# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:51:23 2020

@author: nishi
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Nishi Rachel Presley 
# Section: 543
# Assignment: 7a-3
# Date: 30 September 2020

#my code handles invalid input so it should keep bothering you until you enter the correct input -- not case sensitive 

chess_board = [[". " for c in range(8)] for r in range(8)] #gets a beautiful 8 by 8 array of dots 

#this is an elegant way to create the board; it makes an array with spots 0 thru 7 filled with "."  #the cols 
#then it does the array previously created 0 thru 7 times, #the rows 
#an array of 8 arrays of "." gets what I want: an 8 by 8 array of dots 

#chess_board = [[2,1,3], [2,1,7,3], [2,3]] #this was to see how to print a board correct

#initialize where pieces are supposed to go 
#https://www.alt-codes.net/chess-symbols.php - gets the unicode 

def initializeBoard (chess_board):
    
    ######### all the pawns #########
    for c in range(len(chess_board[0])):
        chess_board[1][c] = chr(9823) #black pawns
        chess_board[-2][c] = chr(9817) #white pawns
    
    ######### rooks #########
    #black
    chess_board[0][-1] = chr(9820)
    chess_board[0][0] = chr(9820)
    
    #white
    chess_board[-1][0] = chr(9814)
    chess_board[-1][-1] = chr(9814)
    
    
    ######### knights #########
    #black
    chess_board[0][-2] = chr(9822)
    chess_board[0][1] = chr(9822)
    
    #white
    chess_board[-1][-2] = chr(9816)
    chess_board[-1][1] = chr(9816)
    
    
    ######### bishops #########
    #black
    chess_board[0][-3] = chr(9821)
    chess_board[0][2] = chr(9821)
    
    #white
    chess_board[-1][-3] = chr(9815)
    chess_board[-1][2] = chr(9815)
    
    
    ######### king and queen #########
    #black
    chess_board[0][-4] = chr(9818) #king
    chess_board[0][3] = chr(9819) #queen
    
    #white
    chess_board[-1][-4] = chr(9812) #king
    chess_board[-1][3] = chr(9813) #queen
    
    return chess_board


def showBoard (chess_board): 
    
    #to help visualize what is board consider: [[2,1,3], [2,1,7,3], [2,3]]
    row = 8
    print(" A  B  C  D  E  F  G  H") #prints the ABC header 
    
    for r in range(len(chess_board)): #goes thru rows
    
        print("%d" % (row), end= "") #prints 8 thru 1 down the rows
        
        for c in range(len(chess_board[r])): #goes thru cols
            print(chess_board[r][c], end = " ")
            
        print() #newline every row
        row -= 1


#need to handle moving pieces/ the duplicate piece dissappearing and empty squares being moved
#note empty spot moving is now handled in the playgame function  
def movePiece (chess_board, original_spot, new_spot): 
    #orignal spot = [0,2] etc.
    #print(type(original_spot[0])) #debug 
    
    chess_board[new_spot[0]][new_spot[1]] = chess_board[original_spot[0]][original_spot[1]] 
    chess_board[original_spot[0]][original_spot[1]] = ". "
    
     #chess_board[2,2] = chess_board[0,1] #piece at (0,1) goes to (2,2)
    #chess_board[0,1] = ". "              #and spot(0,1) = "." 
    
    showBoard(chess_board) #redraw the board after the move 
    

    
def findSpot (spot): 
    
    #change it so it returns error and you continue calling findspot until it is right 
    
    debug = 0
    current_col = -1 #initializers so the return statement has something to return 
    current_row = -1
    
    #so I can find which row or col I am actually on (index)
    rows = "87654321" #strings are treated as an array 
    cols = "ABCDEFGH"
    cols2 = cols.lower()
    
    spot = list(spot) #a2 --> ['a','2']
    
    if spot[0] in cols:
        current_col = cols.index(spot[0])
    elif spot[0] in cols2:
        current_col = cols2.index(spot[0])
     #else:
        #findSpot(getInput("c")) 
        #so recursion means that it will complete the iteration with correct data 
        #and come back a second time to complete it with wrong data so needs to be called in the playGame function 
        
    if spot[1] in rows:
        current_row = rows.index(spot[1])
     #else:
        #findSpot(getInput("r"))
        
    if debug :
        print("Current col:", current_col, "Current row:", current_row)
 
    row_col = [current_row, current_col] #chess_board[2][1] gets row 2 column 1 element 
    
    return row_col #returns the proper ordered coordinates 
    
#findSpot("b8") #tester code 
#input will look like e4 to c2 


def getInput (row_or_col): #this handles invalid input 
    
    if row_or_col == "r":
        spot = input("You entered an invalid row.\nPlease enter a valid column and row in the format 'e3' or 'A1'. Order matters: ")
    elif row_or_col == "c":
        spot = input("You entered an invalid column.\nPlease enter a valid column and row in the format 'e3' or 'A1'. Order matters: ")
    elif row_or_col == "empty":
        spot = input("You cannot move an empty space. \nPlease enter a valid column and row in the format 'e3' or 'A1'. ")
    #print("Spot from getInput:",spot) #for debugging 
    
    return spot

#initializeBoard(chess_board)
#showBoard(chess_board) 
#movePiece(chess_board, [0,1], [2,2])

def piece_coordinates_isValid (piece_coordinates): ###############*******HERE**************#################
    
    if piece_coordinates[0] == -1: #row    
        return False
    elif piece_coordinates[1] == -1: #col    
        return False
    
    if chess_board[piece_coordinates[0]][piece_coordinates[1]] == ". ": #handles moving empty spots via getInput function 
        return False

    return True 

def piece_coordinates_getNew (piece_coordinates): ###############*******HERE**************#################
    
    if piece_coordinates[0] == -1: #row    
        return findSpot(getInput("r"))
    elif piece_coordinates[1] == -1: #col    
        return findSpot(getInput("c"))
    #print("We are in the correction while loop for piece co") #after fixing the bad recursion call, this part works 

    if chess_board[piece_coordinates[0]][piece_coordinates[1]] == ". ": #handles moving empty spots via getInput function 
        return findSpot(getInput("empty"))
        #print("This is in the while loop trying to handle an empty spot moving") #debug 
    print("What is the problem? These piece coordinates are perfect")


################## MAIN CODE ###############

def playGame_simple (chess_board): #I really wanted to add more, but I had an essay due so it is what it is  
    #welcome
    
    initializeBoard(chess_board)
    showBoard(chess_board)
    
    keepPlaying = True
    
    while keepPlaying: 
        piece_loc = input("Enter a piece's location in the form 'B2' or 'f6': ")
        
        piece_coordinates = findSpot(piece_loc)
        
        while piece_coordinates_isValid(piece_coordinates) != True:
            piece_coordinates = piece_coordinates_getNew(piece_coordinates)
        
        moveTo_loc = input("Enter where you want to move " + chess_board[piece_coordinates[0]][piece_coordinates[1]] +" in the form 'B2' or 'f6': ")
        
        move_coordinates = findSpot(moveTo_loc)
        
        while move_coordinates[0] == -1 or move_coordinates[1] == -1:
            if move_coordinates[0] == -1: #row    
                move_coordinates = findSpot(getInput("r"))
            elif move_coordinates[1] == -1: #col    
                move_coordinates = findSpot(getInput("c"))
            #print("We are in the correction while loop for move co") #debug 
            
        movePiece (chess_board, piece_coordinates, move_coordinates)
        
        play_or_no = input("Type 'stop' to end game or press enter to continue. ")
        
        if play_or_no.lower() == "stop" or play_or_no.lower() == "s":
            keepPlaying = False
        
#playGame_simple(chess_board)


def playGame_complex(chess_board):
    #welcome
    print()
    print("Welcome to this game of chess! Not all rules are applicable. Here is what I have:")
    print("\n\t- checks if the spot is valid; if it isn't it continues asking user until correct input is given")
    print("\t- I encourage you to enter bad input to see what it does. I think I handled a majority of bad cases")
    print("\t- takes in player 1 and 2 names; player1 in the code regardless of what user picks is defined as white")
    print("\t- players do alternate properly, I have a special input statement for the first turns, then a default shorter one for the subsequent turns")
    print("\t- as always any player can move any piece to anywhere it wants. I didn't have time to add rules :(")
          
    keepPlaying = True
    play = input("Now you know what is included, do you want to play? (y/n) ")
    
    if play.lower() == 'y' or play.lower() == 'yes': 
        print("Alright let's begin!")
        
        player1_name = input("Player 1 what is your name (Note this will stay throughout the game): ")
        player1_color = input(player1_name + " which pieces would you like? Black or white? (B/W) ")
        
        colorFound = False 
        while not colorFound: #make it so player 1 is always white bc this confusing man -- delete when done 
        
            if player1_color.upper() == "B": #this makes sure player 1 is white because white plays first also bc storing color is confusing 
                colorFound = True
                player2_name = player1_name 
                player1_name = input("Player 2 what is your name (Note this will stay throughout the game, no space at end): ")
                print()
                print(player1_name, "you will be on the white side")
                print(player2_name, "you will be on the black side")
            elif player1_color.upper() == "W": 
                colorFound = True
                player2_name = input("Player 2 what is your name (Note this will stay throughout the game, no space at end): ")
                print()
                print(player1_name, "you will be on the white side")
                print(player2_name, "you will be on the black side")
            else:
                colorFound = False
                player1_color = input(player1_name + " enter a one character response. Please choose which side you want to be: Black or white? (B/W) ")
        
    else:
        print("Aww I am sorry to see you go. Have a great day!")
        keepPlaying = False 
    
    if keepPlaying:
        print()
        initializeBoard(chess_board)
        showBoard(chess_board)

    count = 0
    
    while keepPlaying: 
        
        if count == 0: #white turn
            piece_loc = input("White goes first so "+ player1_name + " which piece do you want to move? Enter in the form 'e3' or 'A8': ")
        elif count == 1:
            piece_loc = input(player2_name + " you are next which piece do you want to move? Enter in the form 'b4' or 'A8': ")
        elif count % 2 == 0: #white turn
            piece_loc = input(player1_name + " which piece do you want to move? ")
        elif count % 2 == 1:
            piece_loc = input(player2_name + " which piece do you want to move? ")
        else:
            print("Code went very wrong and count is likely not a number. I am in the while loop: keepPlaying; send help")
        
        piece_coordinates = findSpot(piece_loc)
        
        while piece_coordinates_isValid(piece_coordinates) != True:
            piece_coordinates = piece_coordinates_getNew(piece_coordinates)
                
        #this worked, but the wording seemed too formal 
        #moveTo_loc = input("Enter where you want to move " + chess_board[piece_coordinates[0]][piece_coordinates[1]] +" in the form 'B2' or 'f6': ")
        
        #showBoard(chess_boardy)
        
        if count % 2 == 0: #white turn
            moveTo_loc = input(player1_name + " where you want to move " + chess_board[piece_coordinates[0]][piece_coordinates[1]] +" of "+ piece_loc +" to? ")
        elif count % 2 == 1:
            moveTo_loc = input(player2_name + " where you want to move " + chess_board[piece_coordinates[0]][piece_coordinates[1]] +" of "+ piece_loc +" to? ")
        
        move_coordinates = findSpot(moveTo_loc)
        
        while move_coordinates[0] == -1 or move_coordinates[1] == -1:
            if move_coordinates[0] == -1: #row    
                move_coordinates = findSpot(getInput("r"))
            elif move_coordinates[1] == -1: #col    
                move_coordinates = findSpot(getInput("c"))
            #print("We are in the correction while loop for move co") #debug 
            
        movePiece (chess_board, piece_coordinates, move_coordinates)
        
        
        play_or_no = input("Type 'stop' to end game or press enter (or any key) to continue. ")
        
        if play_or_no.lower() == "stop" or play_or_no.lower() == "s":
            keepPlaying = False
        else:
            count += 1

gameType = input("Do you want to play the game which follows the lab assignment(1) or the one slightly more complex(2)? Choose 1 or 2: ")

if gameType == "1":
    playGame_simple(chess_board)
elif gameType == "2":
    playGame_complex(chess_board)
else:
    print("\nERROR: You will have to reload the game. You entered an invalid entry. We were looking for '1' or '2'. Sorry try again.")
    
#what we want in code:
    #see if the person wants to keep playing
    #ask which player is black and which is white enter a name + black 
    # add a count variable and do modulus to get player changes
    #print a welcome message 
    #ask which piece you want to move, then find the spot 
    #ask where you want to go and then get spot
    #then pass both spots and chess board to the move piece function 

#current to do:
    #must add another parameter to movePiece function 
    #figure out why I cannot add the check for empty space within the move function! find a way more efficient == now is not good 
    #find spot cannot call itself which why we have problems. 
    #add the parameter checking which team the pieces are on 