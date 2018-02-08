import deck
import player


def createPlayers():
    players = []
    a = int(input('how many players? '))
    for i in range(a):
        name = input('Name: ')
        p = player.Player(name)
        players.append(p)
    return players


def resetPlayersHands(players, d):
    # empty each player's hand
    for p in players:
        p.empty_hand()

    # give each player two cards
    for i in range(2):
        for p in players:
            card = d.deal()
            p.add_card(card)


def takeTurn(p, d):
    print(p.get_name(), 'its your turn!')
    while True:
        print('Your current cards are', p.show_cards())
        if p.has_twenty_one():
            print('BLACKJACK!')
            break

        ask = input('[h]it or [s]tay? ')
        if ask == 'h':
            card = d.deal()
            print('You get a', card)
            p.add_card(card)

            if p.bust():
                break
        else:
            break
    print('Your turn is over, your total is:', p.get_value())
    print()

def main():
    d = deck.Deck()
    d.shuffle()
    players = createPlayers()
    while True:
        resetPlayersHands(players, d)
        for p in players:
            takeTurn(p, d)
        keepplaying = input('Keep playing? [y/n]: ')
        if keepplaying == 'n':
            break
if __name__ == '__main__':
    main()






