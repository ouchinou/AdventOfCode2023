import time
import numpy as np
import re

def day14(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0
        nb_columns = len(lines[0])

        for col in range(nb_columns):
            current_column = "".join([line[col] for line in lines])
            #print(current_column)
            fixed_rock_idx = [c.start() for c in re.finditer('#', current_column)]
            splitted_round_rock = current_column.split('#')
            fixed_rock_idx = [-1] + fixed_rock_idx
            for i in range(len(splitted_round_rock)):
                fixed_rock_current_place = fixed_rock_idx[i]
                nb_round_rock = splitted_round_rock[i].count('O')
                for weight in range(nb_round_rock):
                    #print("rock number " + str(fixed_rock_current_place) + " weight " + str(num_lines - fixed_rock_current_place - weight - 1))
                    result += num_lines - fixed_rock_current_place - weight - 1

        print("Result : " + str(result))


start_time = time.time()
file_path = "input.txt"
day14(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
