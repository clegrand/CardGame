from random import shuffle, randint
from enum import Enum, auto


class CardColor(Enum):
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()
    SPADES = auto()

    def get_color(self):
        return self.name.lower()

    def __str__(self):
        return self.get_color()

    def __eq__(self, number):
        return self.name == number.name


class CardNumber(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def get_value(self):
        return self.name.lower()

    def __str__(self):
        return self.get_value()

    def __gt__(self, value):
        return self.value > value.value

    def __ge__(self, value):
        return self.value >= value.value


class Card:

    def __init__(self, number, color, face=True):
        self.value = number
        self.color = color
        self.face = face

    def __str__(self):
        return repr(self) if self.face else "[hidden]"

    def __repr__(self):
        c = "{c.value} of {c.color}".format(c=self)
        return c if self.face else " ".join((c, "[hidden]"))

    def __eq__(self, target):
        return self.value == target.value and self.color == target.color

    def __gt__(self, target):
        return self.value > target.value

    def __ge__(self, target):
        return self.value >= target.value


class Deck(list):

    def __init__(self, cards=None, to_shuffle=True):
        super().__init__(cards or [])
        if to_shuffle:
            self.shuffle()

    def shuffle(self):
        shuffle(self)

    def pick(self, number=1):
        if number == 1:
            return self.pop()
        return (self.pop() for _ in range(number))

    def random_pick(self):
        return self.pop(randint(0, len(self) - 1))

    def appends(self, deck):
        try:
            while True:
                self.append(deck.pick())
        except IndexError:
            pass

    def appends_random(self, deck):
        try:
            while True:
                self.push_random(deck.pick())
        except IndexError:
            pass

    def push_random(self, card):
        self.insert(randint(0, len(self)), card)

    def push(self, card):
        self.insert(0, card)

    def __str__(self):
        return "\n".join(map(str, self))

    def __repr__(self):
        h = "Cards: {}".format(len(self))
        return "\n".join((h, str(self)))

