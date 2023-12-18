# import alive_progress
import numpy as np
import os
import sys
import time
import itertools

from helpers import write_to_file


infile = "data_day11.txt"
# infile = "exemple.txt"


def get_rows_and_cols_in_expansion(board):

    #
    # check ROWS with no galaxies
    #
    empty_rows = []
    nb_rows = len(board)

    for row_idx in range(nb_rows):
        row = np.asarray(board[row_idx])
        row = row != '#'
        empty = np.all(row)
        if empty:
            empty_rows.append(row_idx)
    print(f"Rows to expand: {empty_rows}")

    #
    # check COLUMNS with no galaxies
    #
    empty_cols = []
    nb_columns = len(board[0])

    for col_idx in range(nb_columns):
        col = np.asarray(board[:, col_idx])
        col = col != '#'
        empty = np.all(col)
        if empty:
            empty_cols.append(col_idx)
    print(f"Columns to expand: {empty_cols}")

    return empty_rows, empty_cols


def order(p1, p2):
    if p1 < p2:
        return p1, p2
    else:
        return p2, p1


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        # read puzzle input
        lines = [[a for a in x.strip()] for x in puzzle_input.readlines()]
        # pp(lines)

        #
        board = np.concatenate(lines)
        board = board.reshape(len(lines), len(lines[0]))
        # print(board)

        empty_rows, empty_cols = get_rows_and_cols_in_expansion(board)

        # get coordinates of each galaxy
        galaxies = {}
        for idx, (x, y) in enumerate(np.argwhere(board == "#")):
            galaxies[idx + 1] = [x, y]
            board[x, y] = idx + 1
        write_to_file("identified_galaxies", board)

        # process pairs of galaxies
        path_sum = 0
        expanding_rows = np.asarray(empty_rows)
        expanding_cols = np.asarray(empty_cols)

        for idx, pair in enumerate(itertools.combinations(galaxies.keys(), 2)):
            # print(f"{idx}: {pair}")

            p1_idx, p2_idx = (pair)
            p1_x, p1_y = galaxies[p1_idx]
            p2_x, p2_y = galaxies[p2_idx]

            # print(f"=> {p1_idx} : ({p1_x} , {p1_y})")
            # print(f"=> {p2_idx} : ({p2_x} , {p2_y})")

            diff_x = abs(p2_x - p1_x)
            diff_y = abs(p2_y - p1_y)
            # print(f"=> {diff_x=} {diff_y=}")

            expansion = 1_000_000

            # count number of "rows in expansion"
            p1, p2 = order(p1_x, p2_x)
            # print(p1, p2)
            nb_x_exp = expanding_rows[p1 < expanding_rows] < p2
            nb_expanding_rows_crossed = np.count_nonzero(nb_x_exp == True)
            # print(f"=> {nb_expanding_rows_crossed=}")
            distance_x = diff_x - nb_expanding_rows_crossed + nb_expanding_rows_crossed * expansion

            # count number of "columns in expansion"
            p1, p2 = order(p1_y, p2_y)
            nb_y_exp = expanding_cols[p1 < expanding_cols] < p2
            nb_expanding_cols_crossed = np.count_nonzero(nb_y_exp == True)
            # print(f"=> {nb_expanding_cols_crossed=}")
            distance_y = diff_y - nb_expanding_cols_crossed + nb_expanding_cols_crossed * expansion
            # print(p1, p2)

            min_dist = distance_x + distance_y
            # print(f"=> {distance_x=}     {distance_y=}")
            # print(f"=> {min_dist=}\n")

            path_sum += min_dist

        print(f"{path_sum=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
