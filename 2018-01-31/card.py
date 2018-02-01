import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def print_value(self):
        map = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }
        if self.value in map:
            return map[self.value]
        return str(self.value)

    def blackjack_value(self):
        if self.value > 10:
            return 10
        if self.value == 1:
            return 11
        return self.value

    def __str__(self):
        #KD
        return self.print_value() + self.suit

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    deck = []
    suits = ['D', 'C', 'H', 'S']
    for suit in suits:
        for value in range(1, 14):
            c = Card(value, suit)
            deck.append(c)

    # random.seed('hello')
    # random.shuffle(deck)


    for i in range(7):
        middle = len(deck)//2
        l = deck[:middle]
        r = deck[middle:]
        deck = []
        for i in range(len(l)):
            if random.randint(0,1) == 1:
                first = l
                last = r
            else:
                first = r
                last = l
            deck.append(first[i])
            deck.append(last[i])

    for card in deck:
        print(card, card.blackjack_value())
