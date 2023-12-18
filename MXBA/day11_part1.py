# import alive_progress
import numpy as np
import os
import sys
import time
import itertools

from helpers import write_to_file


infile = "data_day11.txt"
# infile = "exemple.txt"


def expand(board):

    #
    # check ROWS with no galaxies
    #
    empty_rows = []
    nb_columns = len(board[0])

    for row_idx in range(len(board)):
        row = np.asarray(board[row_idx])
        # print(f"{row=}")
        row = row != '#'
        # print(f"{row=}")
        empty = np.all(row)
        if empty:
            empty_rows.append(row_idx)
    print(f"Rows to expand: {empty_rows}")

    # expand empty rows
    for i in empty_rows[::-1]:   # reverse order, to keep correct index
        # print(f"Expanding row {i}")
        board = np.insert(board, i, ["."] * nb_columns, axis=0)

    #
    # check COLUMNS with no galaxies
    #
    empty_cols = []
    nb_rows = len(board)

    for col_idx in range(len(board[0])):
        col = np.asarray(board[:, col_idx])
        # print(f"{col=}")
        col = col != '#'
        # print(f"{col=}")
        empty = np.all(col)
        if empty:
            empty_cols.append(col_idx)
    print(f"Columns to expand: {empty_cols}")

    # expand empty columns
    for i in empty_cols[::-1]:   # reverse order, to keep correct index
        # print(f"Expanding column {i}")
        board = np.insert(board, i, ["."] * nb_rows, axis=1)

    return board


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        # read puzzle input
        lines = [[a for a in x.strip()] for x in puzzle_input.readlines()]
        # pp(lines)

        #
        board = np.concatenate(lines)
        board = board.reshape(len(lines), len(lines[0]))
        # print(board)

        board = expand(board)
        write_to_file("expanded", board)

        # get coordinates of each galaxy
        galaxies = {}
        for idx, (x, y) in enumerate(np.argwhere(board == "#")):
            galaxies[idx + 1] = [x, y]
            board[x, y] = idx + 1
        write_to_file("expanded2", board)

        # process pairs of galaxies
        path_sum = 0
        for idx, pair in enumerate(itertools.combinations(galaxies.keys(), 2)):
            # print(f"{idx}: {pair=}")
            p1_idx, p2_idx = (pair)
            p1_x, p1_y = galaxies[p1_idx]
            p2_x, p2_y = galaxies[p2_idx]

            min_dist = abs(p2_x - p1_x) + abs(p2_y - p1_y)
            # print(f"=> {min_dist=}")

            path_sum += min_dist

        print(f"{path_sum=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
