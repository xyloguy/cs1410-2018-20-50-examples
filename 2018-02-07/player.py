class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_cards(self):
        return str(self.cards)

    def empty_hand(self):
        self.cards = []

    def get_name(self):
        return self.name

    def get_value(self):
        total = 0
        for card in self.cards:
            total += card.blackjack_value()
        return total

    def bust(self):
        return self.get_value() > 21

    def has_twenty_one(self):
        has_21 = self.get_value() == 21
        has_two_cards = len(self.cards) == 2
        return has_21 and has_two_cards

    # TODO: turn hard in soft hand
