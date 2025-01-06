import copy
import time


def find_start(maze):
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 'S':
                print(f'start at {x=} et {y=}')
                return x, y
    return None


def parse_maze(maze):
    for y in range(len(maze)):
        state = 'O'  # Commencer en supposant qu'on est à l'extérieur
        for x in range(len(maze[y])):
            tile = maze[y][x]
            if tile in ['L', 'F', '|'] and state == 'O':
                state = 'I'  # Passer à l'intérieur
            elif tile in ['7', 'J', '|'] and state == 'I':
                state = 'O'  # Passer à l'extérieur
            if tile == '.':
                maze[y][x] = state  # Marquer la case avec l'état actuel

def count_interior(maze):
    interior_count = 0
    for row in maze:
        for tile in row:
            if tile == 'I':
                interior_count += 1
    return interior_count

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

def transform_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] not in ['S', '*']:
                maze[y][x] = '.'

def retransform_maze(maze, maze_copy):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '*':
                maze[y][x] = maze_copy[y][x]

def Pipe_Maze(file_path):
    maze = []
    result = 0
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file]

    # Créer une copie profonde du labyrinthe
    maze_copy = copy.deepcopy(maze)

    origin = find_start(maze)
    if origin:
        result = navigate(maze, origin) / 2
        transform_maze(maze)  # Transformer le labyrinthe après la navigation
        retransform_maze(maze, maze_copy)  # Retransformer les '*'
        parse_maze(maze)
        write_to_file(maze)  # Écrire le labyrinthe transformé dans un fichier

        interior_count = count_interior(maze)
        print(f"Nombre de cases intérieures : {interior_count}")

    else:
        print("Starting point not found.")

    return interior_count


start = time.time()
#file_path = '../test.txt'  # Update this to your file path
file_path = 'puzzle_10.txt'  # Update this to your file path

output_file_path = 'puzzle_10_out.txt'  # Update this to your file path

max_step = Pipe_Maze(file_path)
print(f'final result is {max_step=}')
end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
