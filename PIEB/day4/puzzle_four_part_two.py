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
    line_points = []  # Liste pour stocker les points de chaque ligne
    additional_copies = []  # Liste pour garder une trace des copies supplémentaires

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(":")
            winning_numbers, own_numbers = parts[1].split("|")
            match = points_computation(winning_numbers.strip(), own_numbers.strip())
            line_points.append(match)

            # Mettre à jour les copies supplémentaires pour les lignes futures
            while len(additional_copies) < len(line_points):
                additional_copies.append(0)
            for i in range(1, match):
                if i < len(additional_copies):
                    additional_copies[i] += 1

    # Calculer le total des points en tenant compte des copies
    total_points = sum(points * (1 + additional_copies[i]) for i, points in enumerate(line_points))

    return total_points

start = time.time()
#file_path = '../../Input/puzzle_4.txt'
file_path = '../test.txt'
print(f"final result = {game_4(file_path)}")
end = time.time()
elapsed = end - start
print(f"time spent = {elapsed} seconds")
