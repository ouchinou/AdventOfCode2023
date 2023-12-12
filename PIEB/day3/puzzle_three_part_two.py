import time


def calculate_gear_ratios_from_file(file_path):
    def is_digit(ch):
        return '0' <= ch <= '9'

    def get_adjacent_numbers(schematic, i, j):
        numbers = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(schematic) and 0 <= nj < len(schematic[ni]) and is_digit(schematic[ni][nj]):
                    num = ''
                    while nj < len(schematic[ni]) and is_digit(schematic[ni][nj]):
                        num += schematic[ni][nj]
                        nj += 1
                    numbers.append(int(num))
                    break  # Break after finding a number to move to the next adjacent cell
        return numbers

    with open(file_path, 'r') as file:
        schematic = [line.strip() for line in file]

    total_ratio = 0
    for i, row in enumerate(schematic):
        for j, ch in enumerate(row):
            if ch == '*':
                adjacent_numbers = get_adjacent_numbers(schematic, i, j)
                if len(adjacent_numbers) == 2:
                    print(f"Gear at ({i}, {j}) with numbers: {adjacent_numbers}")  # Print adjacent numbers
                    total_ratio += adjacent_numbers[0] * adjacent_numbers[1]

    return total_ratio

start = time.time()
file_path = '../../Input/puzzle_3.txt'
print(f"Total Gear Ratio Sum: {calculate_gear_ratios_from_file(file_path)}")

end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")