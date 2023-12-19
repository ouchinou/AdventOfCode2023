import alive_progress
# import numpy as np
import os
# import sys
import time
# import itertools


infile = "data_day12.txt"
# infile = "exemple.txt"


def process_arrangements(arrangement, broken_group):
    if "?" not in arrangement:
        return 1 if check_groups(arrangement, broken_group) else 0

    results = 0

    # OPERATIONAL
    new_record = arrangement.replace("?", ".", 1)
    results += process_arrangements(new_record, broken_group)

    # DAMAGED
    new_record = arrangement.replace("?", "#", 1)
    results += process_arrangements(new_record, broken_group)

    return results


def check_groups(arrangement, broken_group):
    group = arrangement.split(".")
    group = [x for x in group if len(x)]
    group_size = [len(x) for x in group]
    return group_size == broken_group


def main():

    result = 0

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        # read puzzle input
        lines = puzzle_input.readlines()

        with alive_progress.alive_bar(len(lines), spinner="classic", bar="squares") as bar:
            for line in lines:
                record, broken_group = line.strip().split(" ")
                broken_group = [int(x) for x in broken_group.split(",")]

                # print(f"\n{records=} -> {broken_groups=}")
                res = process_arrangements(record, broken_group)
                result += res

                bar()

        print(f"{result=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
