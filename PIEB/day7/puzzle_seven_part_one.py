class Player:
    def __init__(self, hand=None, bid=0, rank=None):
        self.hand = hand
        self.bid = bid
        self.strength = None
        self.rank = None

    def show_hand(self):
        return self.hand

    def show_bid(self):
        return self.bid

    def set_strength(self,value):
        self.strength = value
        return None

    def set_rank(self,value):
        self.rank = value
        return None

    def process_hand(self, hand):
        card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return [card_values.get(card, int(card)) for card in hand]

    def hands_strength(self.hand):
        pass
def order_players(players):
    winnings = 0

    print(len(players))
    return winnings


def Camel_Cards(file_path):
    players = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().rsplit(' ', 1)
            hand_part, bid_part = line.strip().rsplit(' ', 1)
            hand = list(hand_part)
            bid = int(bid_part)
            player = Player(hand, bid)
            players.append(player)
            print(player.show_hand(),"," ,player.show_bid())

        winnings = order_players(players)
    return winnings

file_path = 'test.txt'
total_winnings = Camel_Cards(file_path)

print(f"Le total_winnings est : {total_winnings}")
end = time.time()
elapsed = end - start
