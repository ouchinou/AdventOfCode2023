import time


class Player:
    def __init__(self, hand=None, bid=0):
        self.hand = hand
        self.bid = bid
        self.strength = None
        self.rank = None

    def show_hand(self):
        return self.hand

    def show_bid(self):
        return self.bid

    def set_strength(self, value):
        self.strength = value

    def set_rank(self, value):
        self.rank = value

    def process_hand(self):
        card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.hand = [card_values.get(card, int(card)) for card in self.hand]

    def calculate_hand_strength(self):
        pass


def order_players(players):
    # Implement the logic to order players based on their hand strength or bids
    pass


def camel_cards(file_path):
    players = []
    with open(file_path, 'r') as file:
        for line in file:
            hand_part, bid_part = line.strip().rsplit(' ', 1)
            hand = list(hand_part)
            bid = int(bid_part)
            player = Player(hand, bid)
            player.process_hand()
            player.calculate_hand_strength()
            players.append(player)

    order_players(players)
    return 0


start = time.time()
file_path = '../test.txt'
total_winnings = camel_cards(file_path)
print(f"Le total_winnings est : {total_winnings}")

end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
