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
        out_lines = [line for line in lines]
        num_lines = len(lines)
        result = 0

        i = 0
        j = 0
        # Find start
        for k in range(num_lines):
            i = k
            j = lines[i].find('S')
            if j >= 0:
                break
        s_pos = [i,j]
        print("Found S at " + str(i) + " " + str(j))
        number_steps = 1

        # find starting point
        direction = 0 # south = 0, north = 1, west = 2, east = 3
        if i > 0 and (lines[i-1][j] in direction_from_south):
            # Check north
            i = i - 1
            direction = 0
        elif i < num_lines-1 and (lines[i+1][j] in direction_from_north):
            # Check south
            i = i + 1
            direction = 1
        elif j > 0 and (lines[i][j-1] in direction_from_east):
            # Check west
            j = j - 1
            direction = 2
        elif j < len(lines[0])-1 and (lines[i][j+1] in direction_from_west):
            # Check east
            j = j + 1
            direction = 3

        while not (i == s_pos[0] and j == s_pos[1]):
            #
            out_lines[i] = out_lines[i][:j] + '*' + out_lines[i][j+1:]
            dir_dict = directions[direction]
            if not (lines[i][j] in dir_dict):
                print("Error")
                print("direction is " + str(direction))
                print("i = " + str(i) + " j = " + str(j))
                break
            direction = dir_dict[lines[i][j]][2]
            old_i = i
            i = i + dir_dict[lines[i][j]][0]
            j = j + dir_dict[lines[old_i][j]][1]

            number_steps += 1

        print("Result : " + str(number_steps/2))
        write_to_file("output", out_lines)


start_time = time.time()
file_path = 'input'
day10(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
