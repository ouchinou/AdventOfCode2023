import alive_progress
# import numpy as np
import os
# import sys
import time
# import itertools

# from helpers import write_to_file


infile = "data_day12.txt"
# infile = "exemple.txt"


def get_arrangements(record):
    # print(f"Processing '{record}'...")

    if "?" not in record:
        # print("DONE")
        return [record]

    results = []
    next_unknown_idx = record.index("?")
    # print(f"=> {next_unknown_idx=}")

    # OPERATIONAL
    new_record = record[:]  # copy
    new_record[next_unknown_idx] = "."
    results.extend(get_arrangements(new_record))

    # DAMAGED
    new_record = record[:]  # copy
    new_record[next_unknown_idx] = "#"
    results.extend(get_arrangements(new_record))

    return results


def check_groups(arrangement, broken_groups):
    # print(f"=> {''.join(arrangement)} | {broken_groups}")

    groups = "".join(arrangement).split(".")
    # print(f"=> groups with empty elements: {groups}")
    groups = [x for x in groups if len(x)]
    # print(f"=> groups 'clean': {groups}")
    groups_size = [len(x) for x in groups]
    # print(f"=> groups 'size': {groups_size}")

    return groups_size == broken_groups


def main():

    result = 0

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        lines = puzzle_input.readlines()
        # read puzzle input
        with alive_progress.alive_bar(len(lines), spinner="classic", bar="squares") as bar:
            for line in lines:
                records, broken_groups = line.strip().split(" ")
                records = [x for x in records]
                broken_groups = [int(x) for x in broken_groups.split(",")]

                # print(f"\n{records=} -> {broken_groups=}")
                arrangements = get_arrangements(records)

                for i in arrangements:
                    is_correct = check_groups(i, broken_groups)
                    # print(f"=> {is_correct}\n")
                    if is_correct:
                        result += 1
                bar()

        print(f"{result=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
