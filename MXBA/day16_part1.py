# import alive_progress
import numpy as np
import os
import time
import helpers
import sys


infile = "data_day16.txt"
infile = "exemple.txt"


directions = {"L": [0, -1],
              "R": [0, 1],
              "U": [-1, 0],
              "D": [1, 0]}

mirrors = {"L/": "D",
           "L\\": "U",
           "R/": "U",
           "R\\": "D",
           "U/": "R",
           "U\\": "L",
           "D/": "L",
           "D\\": "R",
           }


def get_next_position(x, y, direction):
    dx, dy = directions[direction]
    return x + dx, y + dy


def get_new_symbol(symbol, direction):
    if symbol == "." and direction == "L":
        return "<"
    if symbol == "." and direction == "R":
        return ">"
    if symbol == "." and direction == "U":
        return "^"
    if symbol == "." and direction == "D":
        return "v"
    if symbol in ["<", ">"] and direction in ["U", "D"]:
        return "2"
    if symbol in ["^", "v"] and direction in ["L", "R"]:
        return "2"

    # reverse direction... stop or continue ???
    if (symbol == "<") and (direction == "R"):
        return ">"
    if (symbol == ">") and (direction == "L"):
        return "<"
    if (symbol == "^") and (direction == "D"):
        return "v"
    if (symbol == "v") and (direction == "U"):
        return "^"

    print(f"TRUC CHELOU : {symbol=} {direction=} ")
    return "?"


def move_beam(board, energized_board, x, y, going_to, depth):
    # helpers.write_to_file("debug", board)
    # input("continue...")
    print(f"{x=} {y=} {going_to=} {depth=}")

    # STOP CONDITION : out of board
    if (x < 0) or (x >= board.shape[0]) or (y < 0) or (y >= board.shape[1]):
        # print("STOP CONDITION : out of board")
        return board

    # check symbol on current
    current_symbol = board[x, y]

    # STOP CONDITION : same beam already in the same direction
    if (board[x, y] == "2") or (current_symbol == get_new_symbol(".", going_to)):
        # print("STOP CONDITION : same beam already in the same direction")
        return board

    # Beam continues its path :)
    if current_symbol == ".":
        # print("Beam continues its path :)")
        # If the beam encounters empty space (.), it continues in the same direction.
        board[x, y] = get_new_symbol(current_symbol, going_to)
        energized_board[x, y] = "#"
        return move_beam(board, energized_board, *get_next_position(x, y, going_to), going_to, depth + 1)

    elif current_symbol in ["/", "\\"]:
        # print("mirrors / \\")
        new_dir = mirrors[f"{going_to}{current_symbol}"]
        energized_board[x, y] = "#"
        return move_beam(board, energized_board, *get_next_position(x, y, new_dir), new_dir, depth + 1)

    elif current_symbol in ["-", "|"]:
        energized_board[x, y] = "#"

        # same direction as beam
        if (current_symbol == "-" and going_to in ["L", "R"]) or\
                (current_symbol == "|" and going_to in ["U", "D"]):
            # continue in the same direction
            # print("mirrors -| : continue in the same direction")
            return move_beam(board, energized_board, *get_next_position(x, y, going_to), going_to, depth + 1)
        else:
            # the beam is split into two beams
            if current_symbol == "-":
                # print("mirrors - : split")
                board = move_beam(board, energized_board, x, y - 1, "L", depth + 1)
                board = move_beam(board, energized_board, x, y + 1, "R", depth + 1)
                return board
            else:
                # print("mirrors | : split")
                board = move_beam(board, energized_board, x - 1, y, "U", depth + 1)
                board = move_beam(board, energized_board, x + 1, y, "D", depth + 1)
                return board
    else:
        # Beam are crossing, continue in the same direction :)
        # print("Beam are crossing, continue in the same direction :)")
        new_symbol = get_new_symbol(current_symbol, going_to)
        if new_symbol == "?":
            # stop here in case the beam goes backward
            return board

        board[x, y] = new_symbol
        return move_beam(board, energized_board, *get_next_position(x, y, going_to), going_to, depth + 1)


def main():

    result = 0
    board = []
    energized_board = []

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        for line in puzzle_input:
            line = line.strip()
            board.append([x for x in line])

        board = np.asarray(board)
        energized_board = np.array(["."] * board.shape[0] * board.shape[1]).reshape(board.shape[0], board.shape[1])
        # helpers.write_to_file("result", board)

        # The beam enters in the top-left corner from the left and heading to the right
        move_beam(board=board, energized_board=energized_board, x=0, y=0, going_to="R", depth=0)
        # helpers.write_to_file("result", board)

    # count energized tiles
    result = np.count_nonzero(energized_board == "#")

    # DEBUG: save results
    helpers.write_to_file("result", board)
    helpers.write_to_file("result_energized", energized_board)
    print(f"{result=}")


# FORCE HIGHER recursion depth (defaut is 1_000)
sys.setrecursionlimit(100_000_000)

if __name__ == '__main__':
    start_time = time.time()

    main()

    print("--- %s seconds ---" % (time.time() - start_time))
