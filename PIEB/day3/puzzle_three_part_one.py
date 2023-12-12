def sum_part_numbers_from_file(file_path):
    # Symbols to consider (excluding '.')
    #symbols = set('/$=#&+*%@-')

    def find_symbols_in_file(file_path):
        find_symbols = set()
        with open(file_path, 'r') as file:
            for line in file:
                for char in line:
                    if not char.isdigit() and char != '.' and char != '\n':
                        find_symbols.add(char)
        return find_symbols

    symbols = find_symbols_in_file(file_path)

    # Function to check if a cell is adjacent to a symbol
    def is_adjacent_to_symbol(grid, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] in symbols:
                    return True
        return False

    # Read the file and convert it into a 2D list
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    # Summing part numbers
    total = 0
    for i, row in enumerate(grid):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                num = row[j]
                k = j + 1
                while k < len(row) and row[k].isdigit():
                    num += row[k]
                    k += 1
                if any(is_adjacent_to_symbol(grid, i, jj) for jj in range(j, k)):
                    total += int(num)
                    print(f"Adding: {num}")  # Print each number being added
                j = k
            else:
                j += 1

    return total

file_path = '../../Repository/AdventOfCode2023/Input/puzzle_three.txt'
print(sum_part_numbers_from_file(file_path))
