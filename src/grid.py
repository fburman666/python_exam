import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    extra_wall_width = 12
    extra_wall_height = 5
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg
    extra_wall = "#" # Tecken för en ogenomtränglig extra-vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    def make_extra_wall_x(self):
        """Skapa extravägg på spelplanen i x-led"""
        x = self.get_random_x()
        y = self.get_random_y()
        if x + self.extra_wall_width > self.width -1:
            x = self.width -self.extra_wall_width -2
        if x == 0 or x == 1:
            x = 2
        if y == self.height or y == self.height -1:
            y = self.height -2
        if y == 0 or y==1:
            y = 2
        for j in range(self.extra_wall_width):
            self.set(x, y, self.extra_wall)
            #print(f"make wall at x={x}, y={y}")
            x += 1

    def make_extra_wall_y(self):
        """Skapa extravägg på spelplanen i y-led"""
        x = self.get_random_x()
        y = self.get_random_y()
        if y + self.extra_wall_height > self.height -1:
            y = self.height -self.extra_wall_height -2
        if y == 0 or y == 1:
            y = 2
        if x == self.width or x == self.width -1:
            x = self.width -2
        if x == 0 or x == 1:
            x = 2
        for j in range(self.extra_wall_height):
            self.set(x, y, self.extra_wall)
            #print(f"make wall at x={x}, y={y}")
            y += 1

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

