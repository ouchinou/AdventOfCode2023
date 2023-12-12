import time

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
        all_lines = file.readlines()
        cards_copies = [1] * len(all_lines)

        for line_idx, line in enumerate(all_lines):
            line = ' '.join(line.split())
            line = line.split(":")[1].strip()
            line = line.split("|")
            print(line)
            match = points_computation(line[0].strip(), line[1].strip())

            copies_of_current = cards_copies[line_idx]
            for i in range(match):
                cards_copies[line_idx + 1 + i] += copies_of_current

            print(sum(cards_copies))
            print(f"Card {line_idx} => {cards_copies=}")
        return cards_copies

start = time.time()
file_path = 'puzzle_4.txt'
print(f"final result = {sum(game_4(file_path))}")
end = time.time()
elapsed = end - start
print(f"time spent = {elapsed} seconds")