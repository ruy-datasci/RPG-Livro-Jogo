from dice.core import DiceBagMeta, _Dice
from dice.checks import Check


class DiceBag(metaclass=DiceBagMeta):
    """Stores a instance of each used dice"""
    @classmethod
    def dice(cls, sides=6):
        Check.type_check(sides, int, 'sides')
        return cls._die.setdefault(sides, _Dice(sides))

    @classmethod
    def add_dice(cls, dice):
        Check.type_check(dice, _Dice, 'sides')
        return cls._die.setdefault(dice.sides, dice)


class RpgRoller:
    @staticmethod
    def roll(die: int = 1, sides: int = 6, bonus: tuple = None):
        dice = DiceBag.dice(sides)
        rolls = dice.roll(die)
        if isinstance(bonus, int):
            bonus = [bonus for _ in range(len(rolls))]
        elif isinstance(bonus, (tuple, list)):
            bonus = list(bonus)
            bonus.extend(0 for _ in range(max(len(rolls)-len(bonus), 0)))
        elif bonus is None:
            bonus = [0 for _ in range(len(rolls))]
        else:
            raise TypeError('Bonus must be a Integer, List, Tuple or None')
        result = tuple(rolls[n]+bonus[n] for n in range(len(rolls)))
        #print(f'Rolls {dice}: ', rolls)
        #print(f'Bonus {dice}: ', bonus)
        #print(f'Result {dice}:', result)
        return result


if __name__ == '__main__':
    # bag
    print(DiceBag.dice(8))  # return a dice
    print(DiceBag.bag)  # show current bag
    print(DiceBag)  # another way to show current bag
    print(DiceBag.dice(10))  # return a new dice
    print(DiceBag)
    print(DiceBag.dice(10).roll(4))  # Try to roll 4 d10 die
    print(DiceBag)
    # roller
    RpgRoller.roll(4, 6, (0, 4, 1, 1, 1))
    RpgRoller.roll(4, 10, 3)
    RpgRoller.roll(4, 8)
