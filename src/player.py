from .functions import print_inventory


class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.got_shovel = 0

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def add_shovel(self):
        self.got_shovel = True
        print("got_shovel=true")


    def use_shovel(self, inv):
        self.got_shovel = False
        index = 0
        for item in inv:
            if item.name == "spade":
                print_inventory(inv)
                print(f"index={index}")
                inv.pop(index)
                return inv

            index +=1


    def can_move(self, x, y, grid, my_inv):
        if grid.get(self.pos_x + x, self.pos_y + y) == grid.wall:   #target square is a wall
            if self.got_shovel:                                     #but we got a shovel
                print(f"position: {self.pos_x + x}, {self.pos_y + y} "
                      f"symbol: {grid.get(self.pos_x + x, self.pos_y + y)}")
                self.use_shovel(my_inv)                             #we use the shovel
                return True                                         #we can move
            else:                                                   #no shovel
                print (grid.get(self.pos_x + x, self.pos_y + y))
            return False                                              #no movement
        else:
            print(f"position: {self.pos_x + x}, {self.pos_y + y} symbol: {grid.get(self.pos_x + x, self.pos_y + y)}")
            return True                                             #no wall
