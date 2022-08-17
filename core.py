from random import randint
from dice.checks import Check


class DiceBagMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._die = dict()

    def __repr__(cls):
        return str(cls.bag)

    @property
    def bag(cls):
        return cls._die


class _Dice:
    """A class that emulates a n-sided dice"""
    def __init__(self, sides: int = 6):
        Check.type_check(sides, int, 'sides')
        self._sds = sides

    def __repr__(self):
        return f'd{self._sds}'

    def __hash__(self):
        return hash(self._sds)

    def __eq__(self, other):
        tests = {
            type(self): lambda other: self.sides == other.sides,
            type(self._sds): lambda other: self.sides == other,
        }
        eq = tests[type(other)](other)
        return isinstance(other, tuple(key for key in tests.keys())) and eq

    @property
    def sides(self):
        return self._sds

    def roll(self, die: int = 1):
        Check.type_check(die, int, 'die')
        return tuple(randint(1, self.sides) for _ in range(die))


if __name__ == '__main__':
    d6 = _Dice()
    d8 = _Dice(8)
    print('Similar dice: ', d6 == _Dice())
    print(d6 == 6)
    # roll
    print(_Dice(6).roll(6))

    

