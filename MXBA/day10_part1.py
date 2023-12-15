# import alive_progress
# import numpy as np
# from collections import Counter
import os
import sys
import time
# import functools
from pprint import pprint as pp

infile = "data_day10.txt"
# infile = "exemple.txt"


directions = {"N": [-1, 0],
              "S": [1, 0],
              "E": [0, 1],
              "W": [0, -1],
              }

neighbours = {"|": ["N", "S"],              # is a vertical pipe connecting north and south.
              "-": ["W", "E"],              # is a horizontal pipe connecting east and west.
              "L": ["N", "E"],              # is a 90 - degree bend connecting north and east.
              "J": ["N", "W"],              # is a 90 - degree bend connecting north and west.
              "7": ["W", "S"],              # is a 90 - degree bend connecting south and west.
              "F": ["E", "S"],              # is a 90 - degree bend connecting south and east.
              ".": [],                      # is ground there is no pipe in this tile.
              "S": ["N", "S", "W", "E"],    # is the starting position of the animal there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.}
              }


def recursive_find_path(nb_steps, current_position, board, from_symbol=None, from_direction=None):

    # get symbol of current position
    x = current_position[0]
    y = current_position[1]
    current_symbol = board[x][y]

    # stop if this cell has already been processed: i.e an INTEGER is in the cell
    if isinstance(current_symbol, int):
        if (current_symbol == 0) and (nb_steps > 2):
            return nb_steps
        else:
            # print(f"{current_symbol} => STOP")
            return -1

    # stop if no pipe
    if current_symbol == ".":
        # print(f"{current_symbol} => STOP")
        return -1

    # check impossible connections
    if from_symbol is not None:
        # print(f"{neighbours[current_symbol]=}")
        if (from_direction == "N") and ("S" not in neighbours[current_symbol]):
            return -1
        elif (from_direction == "S") and ("N" not in neighbours[current_symbol]):
            return -1
        elif (from_direction == "W") and ("E" not in neighbours[current_symbol]):
            return -1
        elif (from_direction == "E") and ("W" not in neighbours[current_symbol]):
            return -1
        else:  # accepted move
            pass

        # override current position to avoid re-processing this cell
    board[x][y] = nb_steps

    # explore all possible neighbours
    max_steps = -1
    for neighbour in neighbours[current_symbol]:
        # print(f"{current_symbol} => {neighbour}")
        n_x = directions[neighbour][0]
        n_y = directions[neighbour][1]
        # nb_steps = recursive_find_path(nb_steps + 1, [x + n_x, y + n_y], board, current_symbol, neighbour)
        max_steps = max(recursive_find_path(nb_steps + 1, [x + n_x, y + n_y], board, current_symbol, neighbour), max_steps)
        # nodes_length.append(nodes_length)

    # path to dead-end -> erase it
    if max_steps == -1:
        # clear symbol
        board[x][y] = "."

    return max_steps


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        # read puzzle input
        lines = [[a for a in x.strip()] for x in puzzle_input.readlines()]
        # pp(lines)

        # find the head of the animal
        animal_pos = []
        for row_idx, line in enumerate(lines):
            if "S" in line:
                animal_pos = [row_idx, line.index("S")]

        # #print(history_list)
        # print(f"{animal_pos=}")

        # FORCE HIGHER recursion depth (defaut is 1_000)
        sys.setrecursionlimit(1_000_000)

        pipe_length = recursive_find_path(0, animal_pos, lines, )
        # pp(lines)
        # print(f"{pipe_length=}")
        print(f" max distance = {(pipe_length)//2}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
