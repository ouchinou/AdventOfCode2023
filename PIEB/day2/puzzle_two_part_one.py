POSSIBLE_CUBE_COUNT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

RESULT = 0

def is_game_possible(line: str) -> bool:
    subgames = line.split(":")[1].split(";")
    for subgame in subgames:
        for num_cubes in subgame.split(','):
            num, color = num_cubes.strip().split()
            if int(num) > POSSIBLE_CUBE_COUNT[color]:
                return False
    return True


with open('../../Repository/AdventOfCode2023/Input/puzzle_two.txt', 'r') as file:
    for index, line in enumerate(file):
        if is_game_possible(line):
            game_id = int(line.split(":")[0].replace("Game", "").strip())
            print(f"Game {game_id} is possible")
            RESULT += game_id

print(RESULT)
