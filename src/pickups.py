
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot", 20, "V"), Item("apple",20,"5"), Item("strawberry",20,"8"),
           Item("cherry",20,"9"), Item("watermelon",20,"O"), Item("radish",20,"Q"),
            Item("cucumber",20,"J"), Item("meatball",20,"W")]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen