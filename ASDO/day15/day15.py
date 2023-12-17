import time
import numpy as np
import re


def compute_hash(current_val, c):
    current_val += ord(c)
    current_val *= 17
    current_val %= 256
    return current_val


def day15(file_path):
    with open(file_path, 'r') as file:
        line = file.read().splitlines()
        init_seq = line[0].split(',')
        result = 0
        for seq in init_seq:
            current_val = 0
            for c in seq:
                current_val = compute_hash(current_val, c)
            result += current_val
        print("Result : " + str(result))


start_time = time.time()
file_path = "input.txt"
day15(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
