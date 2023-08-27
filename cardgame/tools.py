from cards.base import Deck


def deck_serve(deck, group):
    g = [Deck() for x in range(group)]
    try:
        while True:
            for d in g:
                d.append(deck.pick())
    except IndexError:
        return g

