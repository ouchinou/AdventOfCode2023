# import alive_progress
# import numpy as np
import os
import time
import collections
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

        # dictionnaries of results
        boxes = [collections.OrderedDict() for _ in range(256)]

        for sequence in sequences:

            # operation
            if "=" in sequence:
                label, lens = sequence.split("=")
                box_number = compute_hash(label)

                # print(f"Add '{sequence}' to box {box_number}")
                boxes[box_number][label] = lens

            else:
                label = sequence.split("-")[0]
                box_number = compute_hash(label)

                # print(f"Remove '{label}' from box {box_number}")
                if label in boxes[box_number].keys():
                    boxes[box_number].pop(label)

            # print(f"{boxes=}\n")

        # compute the focusing power
        # print(f"\n{boxes=}")
        for box_idx, box in enumerate(boxes):
            # print(f"\n{box=}")
            for slot_idx, [label, lens] in enumerate(box.items()):
                power = (1 + box_idx) * (slot_idx + 1) * int(lens)
                # print(f"{box_idx=} => {slot_idx+1=} -> {label=} : {lens=} ===> {power=}")
                result += power

    print(f"{result=}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
