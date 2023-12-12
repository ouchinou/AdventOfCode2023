import time


def points_computation(win_cartes, own_cards):
    win_cards = win_cartes.split(" ")
    own_cards = own_cards.split(" ")
    total_points = 0
    for card in win_cards:
        print(card)
        if card in own_cards:
            print("win card")
            if total_points >= 1:
                total_points = total_points * 2
            else:
                total_points = 1
            print(f"total_points = {total_points}")
    return total_points

start = time.time()
with open('../../Repository/AdventOfCode2023/Input/puzzle_4.txt', 'r') as file:
    RESULT = 0
    for line in file:
        line = ' '.join(line.split())
        line = line.split(":")[1].strip()
        line = line.split("|")
        print(line)

        RESULT += points_computation(line[0].strip(), line[1].strip())
print(f"final result = {RESULT}")
end = time.time()
elapsed = end - start
print(f"time spent = {elapsed} seconds")