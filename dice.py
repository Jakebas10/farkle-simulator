from die import Die

class Dice:

    @staticmethod
    def roll_set():
        dice = []
        for x in range(1, 7):
            new_die = Die(x)
            dice.append(new_die)
        return dice

    @staticmethod
    def roll_subset():
        return []
