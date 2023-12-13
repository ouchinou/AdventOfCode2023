import time
import numpy as np


def compute_diff(input):
    delta_tab = np.subtract(input[1:len(input)], input[0:len(input)-1])
    if np.count_nonzero(delta_tab) != 0:
        return input[-1] + compute_diff(delta_tab)
    else:
        return input[-1]


def day9(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0
        for line in lines:
            prediction = compute_diff([int(i) for i in line.split()])
            result += prediction

        print("Result : " + str(result))


start_time = time.time()
file_path = 'input'
day9(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
