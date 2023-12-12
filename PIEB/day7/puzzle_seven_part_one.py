import time


class Player:
    def __init__(self, hand=None, bid=0):
        self.hand = hand if hand is not None else []
        self.bid = bid
        self.strength = None
        self.process_hand()
        self.calculate_hand_strength()

    def process_hand(self):
        card_values = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        self.hand = [card_values.get(card, card) for card in self.hand]

        # Convert all elements to integers if they are not already
        self.hand = [int(card) if isinstance(card, str) and card.isdigit() else card for card in self.hand]

    def calculate_hand_strength(self):
        card_count = {card: self.hand.count(card) for card in set(self.hand)}
        count_values = sorted(card_count.values(), reverse=True)

        if 5 in count_values:
            self.strength = 7  # Five of a kind
        elif 4 in count_values:
            self.strength = 6  # Four of a kind
        elif sorted(count_values) == [2, 3]:
            self.strength = 5  # Full house
        elif 3 in count_values:
            self.strength = 4  # Three of a kind
        elif count_values.count(2) == 2:
            self.strength = 3  # Two pair
        elif 2 in count_values:
            self.strength = 2  # One pair
        else:
            self.strength = 1  # High card


def order_players(players):
    players.sort(key=lambda player: (player.strength, player.hand), reverse=True)


    total_sum = 0
    rank = len(players)
    for player in players:
        player.rank = rank
        total_sum += player.bid * rank
        print(f"Hand: {player.hand}, Bid: {player.bid}, Strength: {player.strength}, Rank: {player.rank}")
        rank -= 1

    return total_sum



def camel_cards(file_path):
    players = []
    with open(file_path, 'r') as file:
        for line in file:
            hand_part, bid_part = line.strip().rsplit(' ', 1)
            hand = list(hand_part)
            bid = int(bid_part)
            player = Player(hand, bid)
            #print(f'{hand=} + {bid=} + {player.strength=}')
            players.append(player)

    result = order_players(players)

    return result


start = time.time()
#file_path = '../test.txt'
file_path = 'puzzle_7.txt'
total_winnings = camel_cards(file_path)
print(f"Le total_winnings est : {total_winnings}")

end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
