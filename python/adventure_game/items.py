""" the class item has two methods. __init__.py and __str___
the init method is the constructor and is called whenever a new
object is created. the str method allows us to print on object and
see more useful information. without the str method, calling print() on
an object will display unhelpful information like <main.Item object at 0x101 etc. """

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}nValue: {}n".format(self.name, self.description, self.value)

"""The Gold class is now a subclass of the superclass Item. Another word for a subclass is child class
and superclasses may be called parent or base classes.

amt is a parameter defined as amt of gold, then we call the superclass constructor using super.__init__().
The superclass constructor must ALWAYS be called by a subclass constructor."""
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
            description="A round coin with {} stamped on the front.".format(str(self.amt)),
            value=self.amt)


 class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
            description="A fist-sized rock, suitable for bludgeoning.",
            value=0,
            damage=5)

class Dagger(Weapon):
    def __init__(self)
    super().__init__(name="Dagger",
        description="Small knife good for close encounters",
        value=10,
        damage=10)

