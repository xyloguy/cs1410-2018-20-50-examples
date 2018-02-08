import random

from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['D', 'C', 'H', 'S']
        for suit in suits:
            for value in range(1, 14):
                c = Card(value, suit)
                self.cards.append(c)

    def shuffle(self):
        for i in range(5000):
            r = random.randrange(1, len(self.cards))
            self.cards[r], self.cards[0] = self.cards[0], self.cards[r]

    def deal(self):
        if len(self.cards) == 0:
            return None

        c = self.cards[0]
        self.cards = self.cards[1:]
        return c

    def cut(self, n):
        if n >= len(self.cards):
            n = len(self.cards) - 1
        if n < 0:
            n = 0

        top = self.cards[:n]
        bottom = self.cards[n:]
        self.cards = bottom + top

if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(len(deck.cards), deck.cards)
    for i in range(40):
        print(deck.deal())
    print(len(deck.cards), deck.cards)
    deck.cut(10)
    print(len(deck.cards), deck.cards)