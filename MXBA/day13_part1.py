import alive_progress
import numpy as np
import os
# import sys
import time
# import itertools


infile = "data_day13.txt"
# infile = "exemple.txt"


def main():

    result = 0

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        # read puzzle input
        patterns = []

        current_pattern = ""
        nb_cols = 0
        nb_rows = 0

        for line in puzzle_input:
            line = line.strip()
            if not line:
                patterns.append(np.asarray([x for x in current_pattern]).reshape(nb_rows, nb_cols))
                nb_rows = 0
                current_pattern = []
            else:
                nb_rows += 1
                nb_cols = len(line)
                current_pattern += line
                # print(f"{current_pattern=}")

        # last pattern
        patterns.append(np.asarray(current_pattern).reshape(nb_rows, nb_cols))

        with alive_progress.alive_bar(len(patterns), spinner="classic", bar="squares") as bar:
            rows = []
            columns = []
            for p in patterns:
                # print(p)

                # look for mirror in ROWS
                for i in range(1, p.shape[0]):
                    # print(f"\n{'*' * 10} ROW_{i:02d} {'*' * 10}\n")
                    up = p[:i]
                    down = p[i:]
                    # print(up)
                    # print("-" * up.shape[0])
                    # print(down)
                    # print()

                    # flip the "UP" list vertically
                    up_flipped = np.flipud(up)
                    # print(up_flipped)
                    # print("-" * up.shape[0])
                    # print(down)
                    # print()

                    # keep the same number as rows only
                    min_size = min(up_flipped.shape[0], down.shape[0])
                    final_up = up_flipped[:min_size]
                    final_down = down[:min_size]
                    # print(final_up)
                    # print("-" * len(up))
                    # print(final_down)
                    # print()

                    mirror_row = (final_up == final_down).all()
                    # print(f" OK ? {mirror_row}")
                    if mirror_row:
                        rows.append(i)
                        break

                # look for mirror in COLUMNS
                for i in range(1, p.shape[1]):
                    # print(f"\n{'*' * 10} COL_{i:02d} {'*' * 10}\n")
                    left = p[:, :i]
                    right = p[:, i:]
                    # print(left)
                    # print("-" * 10)
                    # print(right)
                    # print()

                    # flip the "LEFT" list horizontally
                    left_flipped = np.fliplr(left)
                    # print(left_flipped)
                    # print("-" * 10)
                    # print(right)
                    # print()

                    # keep the same number as rows only
                    min_size = min(left_flipped.shape[1], right.shape[1])
                    final_left = left_flipped[:, :min_size]
                    final_right = right[:, :min_size]
                    # print(final_left)
                    # print("-" * 10)
                    # print(final_right)
                    # print()

                    mirror_col = (final_left == final_right).all()
                    # print(f" OK ? {mirror_col}")
                    if mirror_col:
                        columns.append(i)
                        break

                bar()

        print(f"{rows=} {columns=}")

        # compute result
        result = np.sum(columns) + np.sum(rows * 100)
        print(f"{result=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
