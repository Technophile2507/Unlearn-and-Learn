# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:05:15 2020

@author: AVI & ATHI
"""

import itertools

# define method to find winner
def win(current_game):
    
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else :
            return False
        
    # Find the horizontal winners
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (--) !")
            return True

    # Find the vertical winners
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
            
        if all_same(check):
            print(f"Player {row[0]} is the winner vertically ( | ) !")
            return True
            
    # Find the diagonal winners
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
        
    if all_same(diags):
            print(f"Player {diags[0]} is the winner diagonally ( / ) !")
            return True
            
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
            print(f"Player {diags[0]} is the winner diagonally ( \\ ) !")
            return True
    return False

# make game_board player moves
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another! ")
            return game_map,False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count,row in enumerate(game):
            print(count,row)
        return game_map, True
    except IndexError as e:
        print("Error: Make sure you input row/column as 0 1 or 2 ?",e)
        return game_map,False
    except Exception as e:
        print("Something went very wrong!",e)
        return game_map,False

play = True
players = [1,2]
while play:
# Prepare a gamemap
    game_size = int(input("What size game of tic tac toe you wanna play ? : "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game,just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player : {current_player}")
        played = False
        
        while not played:
            column_choice = int(input("What column do you want to play? (0,1,2) : "))
            row_choice = int(input("What row do you want to play? (0,1,2) : "))
            game,played = game_board(game, current_player, row_choice, column_choice)
            
        if win(game):
            game_wom = True
            again = input("The game is over would you like to play again? (y/n) :   ")
            if again.lower() == "y":
                print("Restarting....")
            elif again.lower() == "n":
                print("Byeeeeeee")
                play = False
            else:
                print("Not a valid answer so.. C u later aligator")
                play = False

