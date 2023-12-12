import time


def parse_game_description(description):
    # Splitting the description to separate the game number and the cube data
    _, cube_data = description.split(':', 1)
    parts = cube_data.split('; ')
    total_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for part in parts:
        current_subset = {'red': 0, 'green': 0, 'blue': 0}
        cubes = part.split(', ')
        for cube in cubes:
            amount, color = cube.strip().split(' ')
            color = color.strip()
            amount = int(amount.strip())
            current_subset[color] += amount
        for color in total_cubes:
            total_cubes[color] = max(total_cubes[color], current_subset[color])
    return total_cubes

def calculate_power_of_minimum_set(file_path):
    total_power = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:  # Check if line is not empty
                min_cubes_in_game = parse_game_description(line)
                power = min_cubes_in_game['red'] * min_cubes_in_game['green'] * min_cubes_in_game['blue']
                total_power += power
    return total_power

start = time.time()
file_path = '../../Input/puzzle_2.txt'
print(calculate_power_of_minimum_set(file_path))
end = time.time()
elapsed = end - start
print(f"elapsed time is {elapsed}")