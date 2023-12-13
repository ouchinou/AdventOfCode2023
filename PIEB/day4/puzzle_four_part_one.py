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

def game_4(file_path):
    with open(file_path, 'r') as file:
        result = 0
        for line in file:
            line = ' '.join(line.split())
            line = line.split(":")[1].strip()
            line = line.split("|")
            print(line)

            result += points_computation(line[0].strip(), line[1].strip())


start = time.time()
file_path = 'puzzle_4.txt'
print(f"Total Gear Ratio Sum: {game_4(file_path)}")
end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")