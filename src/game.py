from operator import truediv
from .grid import Grid
from .player import *
from . import pickups
from .functions import *

player = Player(18, 5)
score = 0
inventory = []


g = Grid()
g.set_player(player)
g.make_walls()
g.make_extra_wall_x()
g.make_extra_wall_y()
g.make_extra_wall_x()
pickups.randomize(g)

def move_player(direction, grid, pscore=0):
    """How to move the player in direction direction[x,y]"""
    maybe_item = grid.get(player.pos_x + direction[0], player.pos_y - direction[1])
    player.move(direction[0], -direction[1])
    pscore -= 1
    if isinstance(maybe_item, pickups.Item):
        # we found something
        pscore += maybe_item.value
        print(f"Du hittade en {maybe_item.name}, och tjänar {maybe_item.value} poäng.")
        # g.set(player.pos_x, player.pos_y, g.empty)
        if maybe_item.name == "exit":
            return pscore
        if maybe_item.name != "trap":
            grid.clear(player.pos_x, player.pos_y)
            print(f"Now we clear position {player.pos_x,player.pos_y}")
            inventory.append(maybe_item)
            if maybe_item.name == "spade":
                player.add_shovel()


    return pscore


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g, score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    my_direction = [0, 0]
    if command == "d" and player.can_move(1, 0, g, inventory):  # move right
        my_direction = [1,0]
    elif command == "w" and player.can_move(0, -1, g, inventory):  # move up
        my_direction = [0,1]
    elif command == "a" and player.can_move(-1, 0, g, inventory):  # move left
        my_direction = [-1,0]
    elif command == "s" and player.can_move(0, 1, g, inventory):  # move down
        my_direction = [0,-1]
    elif command == "i":
        print_inventory(inventory)

    if exit_game(inventory, score, g, player):
        break

    score = move_player(my_direction, g, score) #spelaren flyttas i riktningen my_direction


# End of while-loop
print(f"Thank you for playing! You got the score: {score} points")