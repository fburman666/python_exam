from .grid import Grid
from .player import Player
from . import pickups


def print_status(game_grid, pscore):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {pscore} points.")
    print(game_grid)


def print_inventory(inv_list):
    print("You have these elements in your inventory:")
    for item in inv_list:
        print(item.name)


