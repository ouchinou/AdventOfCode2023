import time


class ScratchCard:
    def __init__(self, winning_numbers, own_numbers):
        self.winning_numbers = set(winning_numbers.split())
        self.own_numbers = set(own_numbers.split())

    def count_matches(self):
        return len(self.winning_numbers.intersection(self.own_numbers))


def points_computation(win_cartes, own_cards):
    win_cards = win_cartes.split(" ")
    own_cards = own_cards.split(" ")
    points = 0
    for card in win_cards:
        if card in own_cards:
            points += 1
    print(f"total_points = {points}")
    return points



def game_4(file_path):
    with open(file_path, 'r') as file:
        total_scratchcards = {}
        match = 0
        run = 0
        for index, line in enumerate(file):
            line = ' '.join(line.split())
            line = line.split(":")[1].strip()
            line = line.split("|")
            print(line)
            match = points_computation(line[0].strip(), line[1].strip())
            total_scratchcards.append(index, match, run)
            print(total_scratchcards)
            for card in total_scratchcards:
                print(card)
                total_scratchcards

start = time.time()
file_path = '../../Input/puzzle_4.txt'
print(f"Total Gear Ratio Sum: {game_4(file_path)}")
end = time.time()
elapsed = end - start
print(f"time spent = {elapsed} seconds")
