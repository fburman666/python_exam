class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        if grid.get(self.pos_x + x, self.pos_y + y) == grid.wall:
            print (grid.get(self.pos_x + x, self.pos_y + y))

            return False
        else:
            print(f"position: {self.pos_x + x}, {self.pos_y + y} symbol: {grid.get(self.pos_x + x, self.pos_y + y)}")
            return True
