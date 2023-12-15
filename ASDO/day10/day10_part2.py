import time
import numpy as np


def write_to_file(file_path, content):
    try:
        # Open the file in write mode ('w')
        with open(file_path, 'w') as file:
            # Write the content to the file
            for line in content:
                file.write(line + "\n")
        print(f"Content successfully written to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")


# south = 0, north = 1, west = 2, east = 3
direction_from_south = {'|': [-1, 0, 0], '7': [0, -1, 3], 'F': [0, 1, 2]}
direction_from_north = {'|': [1, 0, 1], 'L': [0, 1, 2], 'J': [0, -1, 3]}
direction_from_west = {'-': [0, 1, 2], 'J': [-1, 0, 0], '7': [1, 0, 1]}
direction_from_east = {'-': [0, -1, 3], 'L': [-1, 0, 0], 'F': [1, 0, 1]}
directions = [direction_from_south, direction_from_north, direction_from_west, direction_from_east]


def day10(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        len_str = len(lines[0])
        num_lines = len(lines)

        # create an enlarged maze
        enlarged_file = []
        for k in range(num_lines-1):
            enlarged_file = enlarged_file +[lines[k]]
            new_lines = ''
            for l in range(len_str):
                if lines[k][l] == '|' or lines[k][l] == 'F' or lines[k][l] == '7' or  lines[k][l] == 'S':
                    if lines[k+1][l] == '|' or lines[k+1][l] == 'L' or lines[k+1][l] == 'J' or lines[k+1][l] == 'S':
                        new_lines = new_lines + '|'
                    else:
                        new_lines = new_lines + '.'
                else:
                    new_lines = new_lines + '.'
            enlarged_file = enlarged_file + [new_lines]
        enlarged_file = enlarged_file + [lines[num_lines-1]]
        # To visualize enlarged input
        write_to_file("enlarged_input", enlarged_file)

        i = 0
        j = 0
        # Find start S
        for k in range(len(enlarged_file)):
            i = k
            j = enlarged_file[i].find('S')
            if j >= 0:
                break
        s_pos = [i, j]
        print("Found S at " + str(i) + " " + str(j))

        # find starting point
        direction = 0  # south = 0, north = 1, west = 2, east = 3
        if i > 0 and (enlarged_file[i - 1][j] in direction_from_south):
            # Check north
            i = i - 1
            direction = 0
            print("start to go north")
        elif i < num_lines - 1 and (enlarged_file[i + 1][j] in direction_from_north):
            # Check south
            i = i + 1
            direction = 1
            print("start to go south")
        elif j > 0 and (enlarged_file[i][j - 1] in direction_from_east):
            # Check west
            j = j - 1
            direction = 2
            print("start to go west")
        elif j < len(enlarged_file[0]) - 1 and (enlarged_file[i][j + 1] in direction_from_west):
            # Check east
            j = j + 1
            direction = 3
            print("start to go east")

        # Create an "empty" output to draw only the path of the maze, so every pipe that is not part of the maze
        # will be a dot
        dot_str = ''
        for k in range(len(enlarged_file[0])):
            dot_str += '.'
        out_lines = [dot_str for line in enlarged_file]
        out_lines[s_pos[0]] = out_lines[s_pos[0]][:s_pos[1]] + '*' + out_lines[s_pos[0]][s_pos[1] + 1:]

        # Follow the maze and draw * for each pipe taken
        while not (i == s_pos[0] and j == s_pos[1]):
            out_lines[i] = out_lines[i][:j] + '*' + out_lines[i][j+1:]
            dir_dict = directions[direction]
            if not (enlarged_file[i][j] in dir_dict):
                print("Error")
                print("direction is " + str(direction))
                print("i = " + str(i) + " j = " + str(j))
                break
            direction = dir_dict[enlarged_file[i][j]][2]
            old_i = i
            i = i + dir_dict[enlarged_file[i][j]][0]
            j = j + dir_dict[enlarged_file[old_i][j]][1]

        # Add last pipe in the maze
        out_lines[i] = out_lines[i][:j] + '*' + out_lines[i][j + 1:]
        
        # Let's count the number of nest possible
        nb_nests = 0
        for line_idx in range(1, len(out_lines)-2, 2):
            # Parse only the enlarged lines, they do not contain horizontal pipes, so it helps to count
            # what is inside and outside the maze
            inside = False
            for c_idx in range(len(out_lines[line_idx])-1):
                if out_lines[line_idx][c_idx] == '*':
                    # Alternate in/out boolean when we reach a maze pipe
                    inside = not inside
                else:
                    if inside:
                        # count as the nest if and only if there is two dots superposed (due to enlargements,
                        # there are many lines of 1 dot that did not exist before.
                        # Look at enlarged_input generated file to visualize)
                        if out_lines[line_idx+1][c_idx] == '.':
                            nb_nests += 1
                            # Replace element by $ to visualize result
                            out_lines[line_idx] = out_lines[line_idx][:c_idx] + '$' + out_lines[line_idx][c_idx + 1:]

        write_to_file("output", out_lines)
        print("Result : " + str(nb_nests))


start_time = time.time()
file_path = 'input'
day10(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
