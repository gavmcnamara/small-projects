import items, enemies

""" The MapTile class is going to provide a
template for all of the tiles in our world,
which means we need to define the methods that
all tiles will need. """

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

""" We call it an abstract base class because we don’t
want to create any instances of it. In our game, we will
only create specific types of tiles. We will never create
a MapTile directly, instead we will create subclasses. The
code raise NotImplementedError() will warn us if we accidentally
create a MapTile directly.
"""
def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

"""Because it’s the starting room, I didn’t want anything
to happen to the player. The pass keyword simply tells
Python to not do anything. You might wonder why the method
is even in this class if it doesn’t do anything. The reason
is because if we don’t override modify_player, the superclass’s
modify_player will execute and if that happens the program will
crash because of raise NotImplementedError()."""
class StartingRoom(MapTile):
    def intro_rext(self):
        return """You find yourself if a cave with a
         flickering torch on the wall.You can make out four
          paths, each equally as dark and foreboding
          """
    def modify_player(self, player):
        #Room has no action player
        pass

#  add a class for the tile where a player will find a new item.
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = itemsuper().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(player)

    def modify_player(self, player):
        self.add_loot(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp =  the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps in front of you!
            """
        else:
            return """
            The dead spider rots on the ground
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shinyin the corner.
        Its a dagger! You pick it up.
        """