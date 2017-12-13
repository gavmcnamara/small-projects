import items, enemies

""" The MapTile class is going to provide a
template for all of the tiles in our world,
which means we need to define the methods that
all tiles will need. """

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

