from itertools import product

from cards.base import Deck, Card, CardNumber, CardColor


class Deck32(Deck):

    def __init__(self, shuffle=True):
        super().__init__([Card(v, c) for v, c in product(list(CardNumber)[6:], list(CardColor))],
                         to_shuffle=shuffle)


class Deck52(Deck):

    def __init__(self, shuffle=True):
        super().__init__([Card(v, c) for v, c in product(list(CardNumber), list(CardColor))],
                         to_shuffle=shuffle)

