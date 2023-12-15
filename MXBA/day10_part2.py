import os
import sys
import time
import copy

from helpers import write_to_file

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


def recursive_find_path(nb_steps, current_position, board, lines, from_symbol=None, from_direction=None):

    # get symbol of current position on the BOARD ('.' and integers)
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
        max_steps = max(recursive_find_path(nb_steps + 1, [x + n_x, y + n_y], board, lines, current_symbol, neighbour), max_steps)

    # path to dead-end -> erase it
    if max_steps == -1:
        # clear symbol
        board[x][y] = "."
        lines[x][y] = "."

    return max_steps


def extrapolate_board_height(board):

    board_size = len(board)
    new_size = board_size * 2 - 1
    # print(f"{new_size=}")

    new_board = [[]] * new_size

    # copy old data
    for line_idx in range(len(board)):
        new_board[2 * line_idx] = board[line_idx]

    # interpolate data between known nodes
    for line_idx in range(len(board) - 1):
        before = board[line_idx]
        after = board[line_idx + 1]

        new_line = []
        for up, down in zip(before, after):
            connection = f"{up}{down}"

            if connection in ["||", "|L", "|J", "|S",
                              "7|", "7L", "7J", "7S",
                              "F|", "FL", "FJ", "FS",
                              "S|", "SL", "SJ"]:
                new_symbol = "|"
            else:
                new_symbol = "."

            new_line.append(new_symbol)

        new_board[2 * line_idx + 1] = new_line

    return new_board


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

        print(f"{animal_pos=}")

        # FORCE HIGHER recursion depth (defaut is 1_000)
        sys.setrecursionlimit(1_000_000)

        board = copy.deepcopy(lines)
        recursive_find_path(0, animal_pos, board, lines)

        # write_to_file("orig_table_with_symbols", lines)
        # write_to_file("orig_table_with_path_length", board)

        # clear tiles not on path
        for x in range(len(board)):
            for y in range(len(board[x])):
                if not isinstance(board[x][y], int):
                    lines[x][y] = "."
                    board[x][y] = "."

        # write_to_file("orig_table_with_symbols_clean", lines)
        # write_to_file("orig_table_with_path_length_clean", board)

        new_board = extrapolate_board_height(lines)
        write_to_file("enlarged_input", new_board)

        # visual : replace all non "." with "*"
        clean_board = []
        for line in new_board:
            clean_board.append(["." if x == "." else "*" for x in line])
        write_to_file("enlarged_input_clean", clean_board)

        # count the number of nest
        nb_nests = 0
        # Parse only the enlarged lines, they do not contain horizontal pipes, so it helps to count
        for line_idx in range(1, len(clean_board) - 2, 2):
            outside = True

            for col_idx in range(len(clean_board[line_idx]) - 1):
                if clean_board[line_idx][col_idx] == '*':
                    # switch inside/outside
                    outside = not outside
                else:
                    if not outside:
                        # count as a nest if and only if there are two superposed dots
                        # (due to enlargements, there are many lines of 1 dot that did not exist before)
                        if clean_board[line_idx + 1][col_idx] == '.':
                            nb_nests += 1
                            # Replace element by $ to visualize results
                            clean_board[line_idx][col_idx] = '$'

        write_to_file("final_table", clean_board)
        print(f"{nb_nests=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
