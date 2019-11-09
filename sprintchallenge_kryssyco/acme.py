'''Sprint Challenge Unit 3 Sprint 1 - Part 1 Keep it Classy'''

from random import randint

class Product:
    ''' Designed a class for Acme Product Inventory'''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    '''Sprint Challenge Unit 3 Sprint 1 - Part 2 Objects that go'''

    def stealability(self):
        """Figure out how 'stealable' a product is."""
        value_weight_ratio = self.price / self.weight
        if value_weight_ratio < 0.5:
            return 'Not so stealable...'
        elif value_weight_ratio < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """Destroy products if they have a potency 10 or over"""
        potency = self.flammability * self.weight
        if potency < 10:
            return '...fizzle.'
        elif potency < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

    '''Sprint Challenge Unit 3 Sprint 1 - Part 3 A proper Inheritance'''

class BoxingGlove(Product):
    """ Made a subclass of Product that return how hard the BoxingGlove hits"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """The main purpose of a boxing glove."""
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
