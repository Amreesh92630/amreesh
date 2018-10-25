#creating a display board
from IPython.display import clear_output

#function for displaying board
def display_board(board):
    clear_output # this work only in Jupter book
    #board type
    print(' | | ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' | | ')
    print('--------')
    print(' | | ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' | | ')
    print('--------')
    print(' | | ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' | | ')
    print('--------')
    #board Completed


    #player input function
def player_input():
    marker = ''
    while not(marker == 'X'  or marker == 'O'):
        marker = input('player_1 take X or O :').upper()
        if marker == 'X':
            return ('X','O')
        else:
            return('O','X')

def place_marker(board,position,marker):
    board[position] = marker
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9]== mark) or# upper row
    (board[4] == mark and board[5] == mark and board[6]== mark) or# middle row
    (board[1] == mark and board[2] == mark and board[3]== mark) or# Lower row
    (board[1] == mark and board[5] == mark and board[9]== mark) or # first diagonal
    (board[7] == mark and board[5] == mark and board[3]== mark) or# second diagonal
    (board[7] == mark and board[4] == mark and board[1]== mark) or# first column
    (board[8] == mark and board[5] == mark and board[2]== mark) or# second column
    (board[9] == mark and board[6] == mark and board[3]== mark)) # Third Column
import random
def check_first():
    if random.randint(0,1) == 0 :
        return 'player_1'
    else:
        return 'player_2'

# A function which will tell whether a position is available on the board
# space check function first depens on board then which position in board

def space_check(board,position):
    
    return board[position] == ''
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def replay():
    return input('Players \nDo you want to play again enter Yes or No:').lower().startswith('y')




def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Enter your next position (1-9)'))
        
    return position
    print('welcome to Tic Tac Toe')

while True:
      # reset board
    
    theboard = [''] * 10
    player1_marker , player2_marker = player_input()
    turn = check_first()
    print(turn + 'will go first:')
    play_game = input("Are you ready to play game Yes or No")
    
    
    if play_game.lower()[0] =='y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'player1':
        
        #player1's turn
            display_board(theboard)# for complete view of board
            position = player_choice(theboard)     #which position available for later use
            place_marker(theboard,position,player1_marker)
            
            if win_check(theboard,player1_marker):
               display_board(theboard)
               print('player1 wins the game')
               game_on = False
                
            else:
                if full_board_check(theboard):
                   display_board(theboard)
                   print('Game  Drawn')
                   break
                else:
                    turn = 'player_2'
                
                
            
        else:
            # player 2's turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,position,player2_marker)
            
            if win_check(theboard,player2_marker):
               display_board(theboard)
               print('player2 wins the game')
               game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('Game Drawn')
                    break
                else:
                    turn = 'player1'
                
                
    if not replay():
        break

