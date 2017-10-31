###### Tic Tac Toe Game #####
""" 2 payers, both be able to give imputs,
bord should print after every move made,
after the player gives an accepted imput the
symbol should print on the screan """

# player 1 and player 2 
player_one = []
player_two = []

# board
board = [['-','-','-'],['-','-','-'],['-','-','-']]
#A. print a board
def board_print():
    for i in range(3):
        print(board[0][i],board[1][i],board[2][i])

#B. Take a players input
turn = 0
def player_turn(turn):
    if turn % 2 == 0:
        i = int(input('What row: '))
        j = int(input('What colume: '))
        player_one.append([i-1])
        player_one.append([j-1])
        turn += 1
    elif turn % 2 == 1:
        i = int(input('What row: '))
        j = int(input('What colume: '))
        player_two.append([i-1])
        player_two.append([j-1])
        turn += 1
#C. Place their input on the board
def add_move_to_bord():
    pass

    
#D. Check if the game is won, tied, lost, or ongoing

#E. Repeat C aand D until the game has ben won or tied

#F. Ask if players want to play again
        
#################        
board_print()
player_turn(turn)
print(player_one)
print(player_two)
