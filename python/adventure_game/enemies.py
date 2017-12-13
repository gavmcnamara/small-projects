class Enemy:
    def __init_(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def isAlive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Spider", hp=30, damage=15)

class Oger(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=10, damage=2)