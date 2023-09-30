import numpy as np
import random

# rotate specific quadrants of the game board
def rotate_clockwise(board):
    temp= board.copy()
    n=len(board[0])
    for i in range(n):
        for j in range(n):
            temp[j][n-i-1]= board[i][j]
    return temp

def rotate_anticlockwise(board):
    temp= board.copy()
    n=len(board[0])
    for i in range(n):
        for j in range(n):
            temp[n-j-1][i]=board[i][j]
    return temp
    
# prints current game board
def display_board(board):
    print(board)

# updates the game board with a player's move, including rotation of a specified quadrant
def apply_move(board,turn,row,col,rot):
    board[row,col]= turn
    #quadrant1 is the top left portion of the board
    quadrant1= board[:3,:3]
    #quadrant2 is the top right portion of the board
    quadrant2= board[:3,3:]
    #quadrant3 is the bottom left portion of the board
    quadrant3= board[3:,:3]
    #quadrant4 is the bottom right of the board
    quadrant4= board[3:,3:] 
    
        
    if rot==1:
        temp= rotate_clockwise(quadrant2)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i][j+3]=temp[i][j]
    elif rot==3: 
        temp= rotate_clockwise(quadrant4)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i+3][j+3]=temp[i][j]
    elif rot==5:
        temp= rotate_clockwise(quadrant3)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i+3][j]=temp[i][j]
    elif rot==7:
        temp= rotate_clockwise(quadrant1)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i][j]=temp[i][j]
    elif rot==2:
        temp= rotate_anticlockwise(quadrant2)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i][j+3]=temp[i][j]
    elif rot==4:
        temp= rotate_anticlockwise(quadrant4)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i+3][j+3]=temp[i][j]
    elif rot==6:
        temp= rotate_anticlockwise(quadrant3)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i+3][j]=temp[i][j]
    elif rot==8:
        temp= rotate_anticlockwise(quadrant1)
        for i in range(len(temp[0])):
                for j in range(len(temp[0])):
                    board[i][j]=temp[i][j]
    
    return board
   
#function checks if a player has won the game by connecting 5 marbles in a row horizontally, vertically, or diagonally. It also identifies a draw if the board is filled.                 
def check_victory(board,turn,rot):
    #checking for 5 consecutive marbles (player 1)
    victory=0
    win = 0
    for i in range(6):
        for j in range(2):
            #checking for 5 consecutive horizontal marbles
            if board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1\
            and board[i][j+3]==1 and board[i][j+4]==1:
                runsum=1
                victory+=runsum
            #checking for 5 consecutive vertical marbles  
            elif board[j][i]==1 and board[j+1][i]==1 and board[j+2][i]==1\
            and board[j+3][i]==1 and board[j+4][i]==1:
                runsum=1
                victory+=runsum  
        
    for i in range(2):
        for j in range(2):
            #checking for 5 consecutive diagonal marbles (negatively sloped) 
            if board [i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1\
            and board[i+3][j+3]==1 and board[i+4][j+4]==1:
                sum=1
                victory+=sum   
    
    for i in range(4,6):
        for j in range(2):
            #checking for 5 consecutive diagonal marbles (positively sloped)
            if board [i][j]==1 and board[i-1][j+1]==1 and board[i-2][j+2]==1\
            and board[i-3][j+3]==1 and board[i-4][j+4]==1:
                sum=1 
                victory+=sum 
            else:
                sum=0
                victory+=sum
    if victory>0: #player 1 has won
        win += 1
    
    #checking for 5 consecutive marbles (player 2)
    victory = 0
    for i in range (len(board[0])):
        for j in range (2):
            #checking for 5 consecutive horizontal marbles
            if board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2\
            and board[i][j+3]==2 and board[i][j+4]==2:
                sum=2
                victory=victory+sum
            #checking for 5 consecutive vertical marbles  
            elif board[j][i]==2 and board[j+1][i]==2 and board[j+2][i]==2\
            and board[j+3][i]==2 and board[j+4][i]==2:
                sum=2
                victory+=sum  
            
    for i in range(2):
        for j in range(2):
            #checking for 5 consecutive diagonal marbles (negatively sloped)   
            if board [i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2\
            and board[i+3][j+3]==2 and board[i+4][j+4]==2:
                sum=2
                victory+=sum   
                
    for i in range(4,6):
        for j in range(2):
            #checking for 5 consecutive diagonal marbles (positively sloped)
            if board [i][j]==2 and board[i-1][j+1]==2 and board[i-2][j+2]==2\
            and board[i-3][j+3]==2 and board[i-4][j+4]==2:
                sum=2
                victory+=sum 
            else:
                sum=0
                victory+=sum
                
    if victory>0: #player 2 has won
        win += 2
    
    if not(0 in board): #draw
        return 3
    else:
        return win

# verifies if a move is valid
def check_move(board,row,col): 
    if board[row][col]==0:
        return True
    else:
        return False

# function takes user input for row, column, and rotation index, ensuring the input is valid and within the allowed ranges
def user_input(board):
    print("Enter 'q' to quit the game")
    row = input("please enter row (0-5): ")
    if row == 'q':
        return -1
    while not(row == '0' or row == '1' or row == '2' or row == '3' or row == '4' or row == '5' or row == 'q'):
        print("Row is out of range!")
        row = input("please enter row (0-5): ")
        if row == 'q':
            return -1
    row = int(row)
        
    col = input("please enter column (0-5): ")
    if col == 'q':
        return -1
    while not(col=='0' or col=='1' or col=='2' or col=='3' or col=='4' or col=='5' or col=='q'):
        print("Col is out of range!")
        col = input("please enter column (0-5): ")
        if col=='q':
            return -1
    col= int(col)
    
    rot = input("please enter rotation index (1-8): ")
    if rot == 'q':
        return -1
    while not(rot=='1' or rot=='2' or rot=='3' or rot=='4' or rot=='5' or rot=='6'\
    or rot=='7' or rot=='8' or rot=='q'):
        print("Rot is out of range!")
        rot = input("please enter rotation index (1-8): ")
        if rot=='q':
            return -1
    rot= int(rot)
    
    if check_move(board, row, col) == False:
        print("move is invalid")
        return user_input(board)
        
    return row, col, rot

# function allows two players to take turns making moves and displays the current game status. It also determines the game's outcome (win, draw, or quit).         
def player_vs_player(board):
    print("Player vs player mode:")
    turn=1
    while True:
        print("This is player " + str(turn) + "'s turn")
        print(" ")
        player_choice = user_input(board)
        if player_choice == -1:
            victory = -1
            break
        board = apply_move(board, turn, player_choice[0], player_choice[1], player_choice[2])
        print("Player "+ str(turn)+" played row "+str(player_choice[0])+", col " +str(player_choice[1])+" and rot "+str(player_choice[2]))
        display_board(board)
        
        victory = check_victory(board, turn, player_choice[2])
            
        if victory == 0:   
            if turn == 1:
                turn = 2
            else:
                turn = 1
        else:
            break
    
    
    if victory == 1:
        print("Player 1 wins")
    elif victory == 2:
        print("Player 2 wins")
    elif victory==3:
        print("It's a draw")
    else:
        print("Thanks for playing!")
        
# function generates a computer move based on the selected difficulty level
def computer_move(board,turn,level):
    if level==1:
        row= random.randint(0,5)
        col=random.randint(0,5)
        rot=random.randint(1,8)
        
        if check_move(board, row, col) == False:
            return computer_move(board,turn,level)
    
        print("Computer played row "+str(row)+", col " +str(col)+" and rot "+str(rot))
        return row, col, rot
    
#generating computer move to a direct win        
    if level==2:
        
            for i in range(6):
                #checking for 4 consecutive horizontal marbles   
                if board[i][0]==2 and board[i][1]==2 and board[i][2]==2\
                and board[i][3]==2 and board[i][4]==0:
                    row=i
                    col=4
                    
                elif board[i][1]==2 and board[i][2]==2 and board[i][3]==2\
                and board[i][4]==2 and board[i][5]==0:
                    row=i
                    col=5
                    
                elif board[i][0]==0 and board[i][1]==2 and board[i][2]==2\
                and board[i][3]==2 and board[i][4]==2:
                    row=i
                    col=0
                    
                elif board[i][1]==0 and board[i][2]==2 and board[i][3]==2\
                and board[i][4]==2 and board[i][5]==2:
                    row=i
                    col=1  
                
                #checking for 3 consecutive horizontal marbles, 1 empty space and 1 marble 
                elif board[i][0]==2 and board[i][1]==2 and board[i][2]==2\
                and board[i][3]==0 and board[i][4]==2:
                    row=i
                    col=3
                    
                elif board[i][1]==2 and board[i][2]==2 and board[i][3]==2\
                and board[i][4]==0 and board[i][5]==2:
                    row=i
                    col=4    
                    
                elif board[i][0]==2 and board[i][1]==0 and board[i][2]==2\
                and board[i][3]==2 and board[i][4]==2:
                    row=i
                    col=1
                    
                elif board[i][1]==2 and board[i][2]==0 and board[i][3]==2\
                and board[i][4]==2 and board[i][5]==2:
                    row=i
                    col=2  
                
                #checking for 2 consecutive horizontal marbles, 1 empty space and 2 more marbles
                elif board[i][0]==2 and board[i][1]==2 and board[i][2]==0\
                and board[i][3]==2 and board[i][4]==2:
                    row=i
                    col=2
                    
                elif board[i][1]==2 and board[i][2]==2 and board[i][3]==0\
                and board[i][4]==2 and board[i][5]==2:    
                    row=i
                    col=3
                    
                #checking for 4 consecutive vertical marbles  
                elif board[0][i]==2 and board[1][i]==2 and board[2][i]==2\
                and board[3][i]==2 and board[4][i]==0:
                    row=4
                    col=i
                    
                elif board[1][i]==2 and board[2][i]==2 and board[3][i]==2\
                and board[4][i]==2 and board[5][i]==0:
                    row=5
                    col=i
                    
                elif board[1][i]==0 and board[2][i]==2 and board[3][i]==2\
                and board[4][i]==2 and board[5][i]==2:
                    row=1
                    col=i
                    
                elif board[0][i]==0 and board[1][i]==2 and board[2][i]==2\
                and board[3][i]==2 and board[4][i]==2:
                    row=0
                    col=i
                    
                #checking for 3 consecutive vertical marbles, 1 empty space and 1 marble 
                elif board[0][i]==2 and board[1][i]==2 and board[2][i]==2\
                and board[3][i]==0 and board[4][i]==2:
                    row=3
                    col=i
        
                elif board[1][i]==2 and board[2][i]==2 and board[3][i]==2\
                and board[4][i]==0 and board[5][i]==2:
                    row=4
                    col=i
        
                elif board[1][i]==2 and board[2][i]==0 and board[3][i]==2\
                and board[4][i]==2 and board[5][i]==2:
                    row=2
                    col=i
                
                elif board[0][i]==2 and board[1][i]==0 and board[2][i]==2\
                and board[3][i]==2 and board[4][i]==2:
                    row=1
                    col=i
                    
                #checking for 2 consecutive vertical marbles, 1 empty space and 2 more marbles
                elif board[0][i]==2 and board[1][i]==2 and board[2][i]==0\
                and board[3][i]==2 and board[4][i]==2:
                    row=2
                    col=i
        
                elif board[1][i]==2 and board[2][i]==2 and board[3][i]==0\
                and board[4][i]==2 and board[5][i]==2:
                    row=3
                    col=i
        
        
            for i in range(2):
                #checking for 4 consecutive diagonal marbles (negatively sloped) 
                if board [i][0]==2 and board[i+1][1]==2 and board[i+2][2]==2\
                and board[i+3][3]==2 and board[i+4][4]==0:
                    row= i+4
                    col= 4
                    
                elif board [i][1]==2 and board[i+1][2]==2 and board[i+2][3]==2\
                and board[i+3][4]==2 and board[i+4][5]==0:
                    row= i+4
                    col= 5
                
                elif board [i][0]==0 and board[i+1][1]==2 and board[i+2][2]==2\
                and board[i+3][3]==2 and board[i+4][4]==2:
                    row= i
                    col= 0   
                
                elif board [i][1]==0 and board[i+1][2]==2 and board[i+2][3]==2\
                and board[i+3][4]==2 and board[i+4][5]==2:
                    row= i
                    col= 1
                    
                #checking for 3 consecutive diagonal marbles, 1 empty space and 1 marble (negatively sloped)
                elif board[i][0]==2 and board[i+1][1]==2 and board[i+2][2]==2\
                and board[i+3][3]==0 and board[i+4][4]==2:
                    row= i+3
                    col= 3
                    
                elif board[i][1]==2 and board[i+1][2]==2 and board[i+2][3]==2\
                and board[i+3][4]==0 and board[i+4][5]==2:
                    row= i+3
                    col= 4
                
                elif board[i][0]==2 and board[i+1][1]==0 and board[i+2][2]==2\
                and board[i+3][3]==2 and board[i+4][4]==2:
                    row= i+1
                    col= 1
                
                elif board[i][1]==2 and board[i+1][2]==0 and board[i+2][3]==2\
                and board[i+3][4]==2 and board[i+4][5]==2:
                    row= i+1
                    col= 2
                
                #checking for 2 consecutive diagonal marbles, 1 empty space and 2 more marbles (negatively sloped)
                elif board[i][0]==2 and board[i+1][1]==2 and board[i+2][2]==0\
                and board[i+3][3]==2 and board[i+4][4]==2:
                    row= i+2
                    col= 2
                    
                elif board[i][1]==2 and board[i+1][2]==2 and board[i+2][3]==0\
                and board[i+3][4]==2 and board[i+4][5]==2:
                    row= i+2
                    col= 3
                
                
            for i in range(4,6):
                #checking for 4 consecutive diagonal marbles (positively sloped)
                if board[i][0]==2 and board[i-1][1]==2 and board[i-2][2]==2\
                and board[i-3][3]==2 and board[i-4][4]==0:
                    row=i-4
                    col= 4
                    
                elif board[i][1]==2 and board[i-1][2]==2 and board[i-2][3]==2\
                and board[i-3][4]==2 and board[i-4][5]==0:
                    row=i-4
                    col= 5
        
                elif board[i][0]==0 and board[i-1][1]==2 and board[i-2][2]==2\
                and board[i-3][3]==2 and board[i-4][4]==2:
                    row= i
                    col= 0
                    
                elif board[i][1]==0 and board[i-1][2]==2 and board[i-2][3]==2\
                and board[i-3][4]==2 and board[i-4][5]==2:
                    row= i
                    col= 1
                    
                
                #checking for 3 consecutive diagonal marbles, 1 empty space and 1 marble (positively sloped)
                elif board[i][0]==2 and board[i-1][1]==2 and board[i-2][2]==2\
                and board[i-3][3]==0 and board[i-4][4]==2:
                    row= i-3
                    col= 3
                        
                elif board[i][1]==2 and board[i-1][2]==2 and board[i-2][3]==2\
                and board[i-3][4]==0 and board[i-4][5]==2:
                    row= i-3
                    col= 4
                    
                elif board[i][0]==2 and board[i-1][1]==0 and board[i-2][2]==2\
                and board[i-3][3]==2 and board[i-4][4]==2:
                    row= i-1
                    col= 1
                    
                elif board[i][1]==2 and board[i-1][2]==0 and board[i-2][3]==2\
                and board[i-3][4]==2 and board[i-4][5]==2:
                    row= i-1
                    col= 2
                    
                #checking for 2 consecutive diagonal marbles, 1 empty space and 2 more marbles (positively sloped)
                elif board[i][0]==2 and board[i-1][1]==2 and board[i-2][2]==0\
                and board[i-3][3]==2 and board[i-4][4]==2:
                    row= i-2
                    col= 2
                    
                elif board[i][1]==2 and board[i-1][2]==2 and board[i-2][3]==0\
                and board[i-3][4]==2 and board[i-4][5]==2:
                    row= i-2
                    col= 3
                
    print("Computer played row "+str(row)+", col " +str(col)+" and rot "+str(rot))
    return row, col, rot
            

    
        
# function lets a player compete against the computer with a chosen difficulty level 
def player_vs_computer(board,level):
    
    print("Level "+ str(level)+ "of Player vs computer mode. Player is player 1, computer is player 2")
    turn=1
    while True:
        print("This is player 1's turn")
        print(" ")
        player_choice = user_input(board)
        if player_choice == -1:
            victory = -1
            break
        board = apply_move(board, turn, player_choice[0], player_choice[1], player_choice[2])
        display_board(board)
        print(" ")
        victory = check_victory(board, turn, player_choice[2])
        if victory == 0:   
            if turn == 1:
                turn = 2
                while turn==2:
                    computer_choice= computer_move(board,turn,level)
                    board=apply_move(board, turn, computer_choice[0], computer_choice[1], computer_choice[2])
                    display_board(board)
                    print(" ")
                    victory= check_victory(board, turn, computer_choice[2])
                    if victory == 0:
                         if turn==2:
                             turn=1  
                    else:
                        break
        else:
            break
        
    if victory == 1:
        print("Player 1 wins")
    elif victory == 2:
        print("Player 2 wins")
    elif victory==3:
        print("It's a draw")
    else:
        print("Thanks for playing!")

# function allows the user to choose between player vs. player or player vs. computer modes and sets the difficulty level
def menu():  
   board= np.zeros((6,6))
   display_board(board)
   print("Welcome to Pentago!")
   mode= input("Choose the game mode. Enter A for player vs player, enter B for player vs computer: " )
   while not(mode=='A' or mode=='B'):
       print("Invalid mode")
       mode= input("Choose the game mode. Enter A for player vs player, enter B for player vs computer: ")
   if mode=='A':
       player_vs_player(board)
   elif mode=='B':
       level=input("Choose between the difficulty levels 1 or 2: ")
       while not(level=='1' or level=='2'):
           print("Invalid level")
           level=input("Choose between the difficulty levels 1 or 2: ") 
       level=int(level)
       player_vs_computer(board)


menu()
    