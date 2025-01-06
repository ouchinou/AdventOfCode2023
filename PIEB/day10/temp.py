import time


def find_start(maze):
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 'S':
                print(f'start at {x=} et {y=}')
                return x, y
    return None


def navigate(maze, start):
    x, y = start
    nb_mov = 0
    previous_pos = None
    current_pos = (y, x)

    while True:
        tile = maze[y][x]
        # print(f'{previous_pos=} and {current_pos=} and {y=} in {x=} , {tile=}')

        if previous_pos is None:
            direction = find_direction(maze, x, y)
            if direction:
                y, x = direction
            else:
                print("No valid direction found")
                break
        else:
            match tile:
                case '|':  # vertical pipe connecting north (+1) and south
                    maze[y][x] = "*"
                    y += 1 if previous_pos[1] == x and previous_pos[0] < y else -1

                case '-':  # horizontal pipe connecting east and west
                    maze[y][x] = "*"
                    x += 1 if previous_pos[0] == y and previous_pos[1] < x else -1

                case 'L':  # 90-degree bend connecting north (+1) and east (+1)
                    if previous_pos[1] == current_pos[1] and previous_pos[0] < current_pos[0]:
                        maze[y][x] = "*"
                        x = x + 1  # go east

                    else:  # Coming from east
                        maze[y][x] = "*"
                        y = y - 1  # go north

                case 'J':  # 90-degree bend connecting north (+1) and west (-1)
                    if previous_pos[1] == current_pos[1] and previous_pos[0] < current_pos[0]:
                        maze[y][x] = "*"
                        x = x - 1  # go west

                    else:  # Coming from west
                        maze[y][x] = "*"
                        y = y - 1  # go north

                case '7':  # 90-degree bend connecting south (-1) and west (-1)
                    if previous_pos[1] == current_pos[1] and previous_pos[0] > current_pos[0]:  # Coming from south
                        maze[y][x] = "*"
                        x = x - 1  # go west
                    else:  # Coming from west
                        maze[y][x] = "*"
                        y = y + 1  # go south

                case 'F':  # 90-degree bend connecting south (-1) and east (+1)
                    if previous_pos[1] == current_pos[1] and previous_pos[0] > current_pos[0]:  # Coming from south
                        maze[y][x] = "*"
                        x = x + 1
                    else:  # Coming from east
                        maze[y][x] = "*"
                        y = y + 1

                case '*':  # 90-degree bend connecting south (-1) and east (+1)
                    break

                case '.':  # 90-degree bend connecting south (-1) and east (+1)
                    print("point")
                    break

            if tile == 'S' and nb_mov != 0:
                print("Loop completed.")
                return nb_mov
            if y < 0 or y >= len(maze) or x < 0 or x >= len(maze[0]):
                print("Out of maze bounds.")
                break
        previous_pos = current_pos
        current_pos = (y, x)
        nb_mov += 1
    return nb_mov


def write_to_file(maze):
    try:
        # Open the file in write mode ('w')
        with open(output_file_path, 'w') as file:
            # Write the content to the file
            for row in maze:
                file.write(''.join(row) + "\n")
        print(f"Content successfully written to {output_file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")


def find_direction(maze, x, y):
    # Get the adjacent tiles (north, south, east, west)
    north = maze[y - 1][x] if y > 0 else '.'
    south = maze[y + 1][x] if y < len(maze) - 1 else '.'
    east = maze[y][x + 1] if x < len(maze[0]) - 1 else '.'
    west = maze[y][x - 1] if x > 0 else '.'

    if north in ['|', '7', 'F']:
        #print(f' find_first_direction: {north=}')
        return (y - 1, x)
    elif south in ['|', 'L', 'J']:
        #print(f' find_first_direction: {south=}')
        return (y + 1, x)
    elif east in ['-', 'L', 'F']:
        #print(f' find_first_direction: {east=}')
        return (y, x + 1)
    elif west in ['-', '7', 'J']:
        #print(f' find_first_direction: {west=}')
        return (y, x - 1)
    else:
        print("No valid direction found")
        return None


def mark_outside(maze):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(y, x):
        if y < 0 or y >= rows or x < 0 or x >= cols or visited[y][x] or maze[y][x] != '.':
            return
        visited[y][x] = True
        dfs(y + 1, x)
        dfs(y - 1, x)
        dfs(y, x + 1)
        dfs(y, x - 1)

    # Marquer les bords
    for x in range(cols):
        dfs(0, x)
        dfs(rows - 1, x)
    for y in range(rows):
        dfs(y, 0)
        dfs(y, cols - 1)

    return visited

def mark_maze(maze, outside):
    rows, cols = len(maze), len(maze[0])
    for y in range(rows):
        for x in range(cols):
#            if maze[y][x] == '.':
            if maze[y][x] in ['|', '-', '7', 'J', 'F', 'L', '.']:

                maze[y][x] = 'I' if not outside[y][x] else 'O'
            #else:
            #    maze[y][x] = '*'

def count_interior(maze, outside):
    interior_count = 0
    rows, cols = len(maze), len(maze[0])

    for y in range(rows):
        for x in range(cols):
            # Si la case n'est pas marquée comme extérieure et n'est pas un mur ou une partie de la boucle
            if not outside[y][x] and maze[y][x] == '.':
                interior_count += 1

    return interior_count


def Pipe_Maze(file_path):
    maze = []
    result = 0
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]

    origin = find_start(maze)
    if origin:
        result = navigate(maze, origin) / 2
    else:
        print("Starting point not found.")

    # find_IO
    #outside = mark_outside(maze)
    #mark_maze(maze, outside)
    write_to_file(maze)

    #interior_count = count_interior(maze, outside)
    #print(f"Nombre de cases intérieures : {interior_count}")
    return result


start = time.time()
#file_path = '../test.txt'  # Update this to your file path
file_path = 'puzzle_10.txt'  # Update this to your file path

output_file_path = 'puzzle_10_out.txt'  # Update this to your file path

max_step = Pipe_Maze(file_path)
print(f'final result is {max_step=}')
end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
