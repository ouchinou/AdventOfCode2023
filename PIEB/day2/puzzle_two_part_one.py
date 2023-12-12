import time

POSSIBLE_CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_game_possible(line: str) -> bool:
    subgames = line.split(":")[1].split(";")
    for subgame in subgames:
        for num_cubes in subgame.split(','):
            num, color = num_cubes.strip().split()
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True

def game_2(file_path):
    total_game_id = 0
    with open(file_path, 'r') as file:
        for line in file:
            if is_game_possible(line):
                game_id = int(line.split(":")[0].replace("Game", "").strip())
                print(f"Game {game_id} is possible")
                total_game_id += game_id

    return total_game_id

start = time.time()
file_path = '../../Input/puzzle_2.txt'
result = game_2(file_path)
print(result)
end = time.time()
elapsed = end - start
print(f"elapsed time is {elapsed}")
