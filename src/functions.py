from .grid import Grid
#from .player import Player
from . import pickups


def print_status(game_grid, pscore, pcount):
    """Show the grid and number of points."""
    print("--------------------------------------")
    print(f"You have {pscore} points.")
    print(f"This is game round: {pcount}")
    print(game_grid)


def print_inventory(inv_list):
    print("You have these elements in your inventory:")
    for item in inv_list:
        print(item.name)


def exit_game(inv, my_score, my_grid, my_player):
    """How to win the game and exit in style"""
    maybe_item = my_grid.get(my_player.pos_x, my_player.pos_y)
    if isinstance(maybe_item, pickups.Item):
        #print(f"maybe_item={maybe_item}")
        if len(inv) >= 9 and maybe_item.name == "exit": #exit is open once player has taken all items (including shovel) and is at "E"
            print(f"CONGRATULATIONS!! You have found the exit!")
            print(f"Total score: {my_score}")
            return True #Exit game
        else:
            return False #Item on this position, but not exit
    else:
        return False #no Item on this position