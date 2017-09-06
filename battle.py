#! /usr/bin/env python3

from cards.tools import deck_serve

from cards import Deck
from cards.decks import Deck52


def battle(p):
    pass


def battles(players):
    cs = [p.deck.pick() for p in players]
    print("Battle :", " VS ".join(map(str, cs)))
    c = max(cs)
    if cs.count(c) > 1:
        pass
    print("Card win: %s" % c)


class Player:

    def __init__(self, name, deck=None):
        self.name = name
        self.deck = deck or Deck()

    def __str__(self):
        return "{p.name:%^80}\n{p.deck}".format(p=self)


if __name__ == '__main__':
    while True:
        try:
            gn = int(input("Number of player: "))
        except ValueError:
            pass
        else:
            break
    g = deck_serve(Deck52(), gn)
    players = [Player(input("Enter a pseudo: "), d) for d in g]
    for p in players:
        print(p)
    print("%" * 80)
    input("Next ")
    while True:
        battles(players)
        input("Next battle ")
