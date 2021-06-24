def display_board(board):
    print (board[:3])
    print (board[3:6])
    print (board[6:])

test_board = ['1','2','3','4','5','6','7','8','9']
tokens = {'player_1': '1', 'player_2': '2'}
flag = 0
display_board(test_board)
# clear_output()

def player_input():
    
    choose_token = raw_input(" Player One, Choose your token ( X / O ): ")
    if choose_token == 'X' or choose_token == 'O':
        tokens['player_1'] = choose_token
        if choose_token == 'X':
            tokens['player_2'] = 'O'
        else:
            tokens['player_2'] = 'X'   
        print ("Player One, your token is " + tokens['player_1'])
        print ("Player Two, your token is " + tokens['player_2'])
    else:
        print ("invalid! please choose X or O\n") 
        player_input()

        
def place_marker(board, marker, position):
    board[int(position) - 1] = marker      

def win_check(board, mark):
    
    if board[0] == board[1] == board[2] == mark or board[3] == board[4] == board[5] == mark or board[6] == board[7] == board[8] == mark or board[0] == board[3] == board[6] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or board[0] == board[4] == board[8] == mark or board[2] == board[4] == board[6] == mark:
        flag = 1
    else:
        flag = 0

#import random

#def choose_first():
#    pass   
# 

#def space_check(board, position):
#    
#   print board[position] == null

#def full_board_check(board):
#    
#    print board !

#def replay():
    
    #pass

print('Welcome to Tic Tac Toe!')

player_input()

while True:
    #Player 1 Turn
    print ("Player one's turn")
    pos = raw_input("where do you want to place your marker? :")
    place_marker(test_board,tokens['player_1'],pos)
    display_board(test_board)
    win_check(test_board,tokens['player_1'])
    if flag == 0:
        #Player 2 Turn
        print ("Player two's turn")
        pos = raw_input("where do you want to place your marker? :")
        place_marker(test_board,tokens['player_2'],pos)
        display_board(test_board)
        win_check(test_board,tokens['player_2'])

        if flag == 0:
            pass
        elif flag == 1:
            print("player 2 wins")
            game_on = False
            break
                
    elif flag == 1:
        print("player 1 wins")
        game_on = False
        break



