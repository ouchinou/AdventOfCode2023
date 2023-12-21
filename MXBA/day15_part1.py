# import alive_progress
# import numpy as np
import os
import time
# import helpers


infile = "data_day15.txt"
# infile = "exemple.txt"


def compute_hash(msg):
    current_value = 0

    for char in msg:

        # Determine the ASCII code for the current character of the string.
        ascii_code = ord(char)

        # Increase the current value by the ASCII code you just determined.
        current_value += ascii_code

        # Set the current value to itself multiplied by 17.
        current_value *= 17

        # Set the current value to the remainder of dividing itself by 256.
        current_value = current_value % 256

        # print(f"'{char=} => {current_value=}")

    # print(f"{current_value=}")

    return current_value


def main():

    result = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        # read puzzle input
        full_input = ""
        for line in puzzle_input:
            line = line.strip()
            full_input += line

        # puzzle input is a comma-separated list
        sequences = full_input.split(",")
        for sequence in sequences:
            res = compute_hash(sequence)
            # print(f"{res=}")
            result += res

    print(f"{result=}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
