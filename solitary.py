#! /usr/bin/env python3
from cards.base import Deck, CardColor
from cards.decks import Deck52

PICK_NUMBER = 2


class FamilyDeck(Deck):
    def next_card(self, card):
        last_card = self[-1] if len(self) else None
        if (not len(self) and card.value == card.value.ACE) or\
                (last_card and card.value.value == last_card.value.value - 1 and card.color == last_card.color):
            self.append(card)
            return True
        return False


def get_value(deck):
    d = Deck()
    try:
        d.extend((deck.pick() for x in range(PICK_NUMBER)))
    except IndexError:
        pass
    return d


def update_family(family, deck):
    entered = 0
    try:
        while family.next_card(deck[-1]):
            print("VALIDATED:", deck.pop())
            entered += 1
    except IndexError:
        pass
    return entered


if __name__ == '__main__':
    deck = Deck52()
    recover = Deck()
    families = [FamilyDeck() for x in CardColor]
    passed = False
    while True:
        tmp = get_value(deck)
        recover.extend(tmp)
        print(">", end=' ')
        while True:
            tmp_pass = False
            for family in families:
                if update_family(family, recover):
                    passed = tmp_pass = True
            if not tmp_pass:
                break
        print("STOP:", deck[-1] if len(deck) else "[end]")
        if len(tmp) < PICK_NUMBER:
            if not len(recover):
                break
            deck.appends(recover)
            if not passed:
                print("NEED SHUFFLE")
                deck.shuffle()
            passed = False
            for family in filter(lambda f: len(f), families):
                print(family[-1])
            input("PAUSE")
    print("FAMILIES:")
    print(sorted(families, key=lambda f: len(f), reverse=True))
    print("END")
