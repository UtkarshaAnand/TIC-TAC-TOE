"""
TIC TAC TOE GAME
AUTHOR: UTKARSHA ANAND
"""

#fuction to display the board
def display_board(board):    
    print("   |     |   ")
    print(" " + board[7] + " |  " + board[8] + "  | " + board[9] + " ")
    print("   |     |   ")
    print("-------------")
    print("   |     |   ")
    print(" " + board[4] + " |  " + board[5] + "  | " + board[6] + " ")
    print("   |     |   ")
    print("-------------")
    print("   |     |   ")
    print(" " + board[1] + " |  " + board[2] + "  | " + board[3] + " ")
    print("   |     |   ")
    
#function to assign marker to each player
def player_input():
    marker=''
    while not (marker=='O' or marker=='X'):
        marker=input("Player1: Which marker do you want, 'X' or 'O'?  ").lower
        if marker=='O':
            return('O','X')
        else:
            return('X','O')
        
#function to assign marker to the desired position
def assign_marker(board,marker,position):
    board[position]=marker

#function to check win
def win(board,marker):
    return((board[1]==marker and board[2]==marker and board[3]==marker) or (board[4]==marker and board[5]==marker and board[6]==marker) or (board[7]==marker and board[8]==marker and board[9]==marker) or (board[1]==marker and board[4]==marker and board[7]==marker) or (board[2]==marker and board[5]==marker and board[8]==marker) or (board[3]==marker and board[6]==marker and board[9]==marker) or  (board[1]==marker and board[5]==marker and board[9]==marker) or (board[3]==marker and board[5]==marker and board[7]==marker)) 

#function to decide which player starts    
import random
def toss():
    if random.randint(1,2) == 1:
        return "Player 1"
    else:
        return "Player 2"

#function to check space
def check_space(board,position):
    return board[position]==' '

#function to check board full
def board_full(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

#function to ask and return the desired position of player's marker
def position_choice(board):
    position= ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not check_space(board,int(position)):
        position=input("Choose your next position: ")
    return int(position)

#function to ask for replay
def replay():
    return input("Do you want to play again? ").lower().startswith('y')


#main function
print("Welcome to 'Tic Tac Toe!'")
while True:
    the_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    player1_marker,player2_marker=player_input()
    turn=toss()
    print(turn + " will go first.")

    game_on = True

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            position=position_choice(the_board)
            assign_marker(the_board,player1_marker,position)

            if win(the_board,player1_marker):
                display_board(the_board)
                print("Congratulations, Player 1 has won the game!")
                game_on = False

            elif board_full(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break

            else:
                turn="Player 2"

        if turn == "Player 2":
            display_board(the_board)
            position=position_choice(the_board)
            assign_marker(the_board,player2_marker,position)

            if win(the_board,player2_marker):
                display_board(the_board)
                print("Congratulations, Player 2 has won the game!")
                game_on = False

            elif board_full(the_board):
                    display_board(the_board)
                    print("The game is a draw!")
                    break

            else:
                turn="Player 1"

    if not replay():
        break



    
    
     




          
