import random

class Die:

    def __init__(self, id):
        self.id = id
        self.roll = random.randrange(1, 7)

    def __str__(self):
        return 'die: {}, roll: {}'.format(self.id, self.roll)