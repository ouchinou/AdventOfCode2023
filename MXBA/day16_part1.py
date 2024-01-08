# import alive_progress
import numpy as np
import os
import time
import helpers
import sys


infile = "data_day16.txt"
# infile = "exemple.txt"


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

    # reverse direction: stop beam
    if (symbol == "<") and (direction == "R"):
        return ">"
    if (symbol == ">") and (direction == "L"):
        return "<"
    if (symbol == "^") and (direction == "D"):
        return "v"
    if (symbol == "v") and (direction == "U"):
        return "^"


def move_beam(board, energized_board, x, y, going_to):

    current_x = x
    current_y = y
    current_direction = going_to

    while True:
        # print(f"{current_x=} {current_y=} {going_to=}")
        # helpers.write_to_file("debug", board)
        # helpers.write_to_file("result_energized", energized_board)
        # input("continue...")

        # STOP CONDITION : out of board
        if (current_x < 0) or (current_x >= board.shape[0]) or (current_y < 0) or (current_y >= board.shape[1]):
            # print("STOP CONDITION : out of board")
            break

        # check symbol on current
        current_symbol = board[current_x, current_y]

        # STOP CONDITION : same beam already in the same direction
        if (board[current_x, current_y] == "2") or (current_symbol == get_new_symbol(".", current_direction)):
            # print("STOP CONDITION : same beam already in the same direction")
            break

        # Beam continues its path :)
        if current_symbol == ".":
            # print("Beam continues its path :)")
            # If the beam encounters empty space (.), it continues in the same direction.
            board[current_x, current_y] = get_new_symbol(current_symbol, current_direction)
            energized_board[current_x, current_y] = "#"
            current_x, current_y = get_next_position(current_x, current_y, current_direction)

        elif current_symbol in ["/", "\\"]:
            # print("mirrors / \\")
            new_dir = mirrors[f"{current_direction}{current_symbol}"]
            energized_board[current_x, current_y] = "#"
            current_x, current_y = get_next_position(current_x, current_y, new_dir)
            current_direction = new_dir

        elif current_symbol in ["-", "|"]:
            energized_board[current_x, current_y] = "#"

            # same direction as beam
            if (current_symbol == "-" and current_direction in ["L", "R"]) or\
                    (current_symbol == "|" and current_direction in ["U", "D"]):
                # continue in the same direction
                # print("mirrors -| : continue in the same direction")
                current_x, current_y = get_next_position(current_x, current_y, current_direction)
            else:
                # the beam is split into two beams
                if current_symbol == "-":
                    # print("mirrors - : split")
                    move_beam(board, energized_board, current_x, current_y - 1, "L")
                    move_beam(board, energized_board, current_x, current_y + 1, "R")
                    break
                else:
                    # print("mirrors | : split")
                    move_beam(board, energized_board, current_x - 1, current_y, "U")
                    move_beam(board, energized_board, current_x + 1, current_y, "D")
                    break
        else:
            # Beam are crossing, continue in the same direction :)
            # print("Beam are crossing, continue in the same direction :)")
            new_symbol = get_new_symbol(current_symbol, current_direction)
            if new_symbol == "?":
                # stop here in case the beam goes backward
                break

            board[current_x, current_y] = new_symbol
            energized_board[current_x, current_y] = "#"
            current_x, current_y = get_next_position(current_x, current_y, current_direction)


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
        move_beam(board=board, energized_board=energized_board, x=0, y=0, going_to="R")
        # helpers.write_to_file("result", board)

    # count energized tiles
    result = np.count_nonzero(energized_board == "#")

    # DEBUG: save results
    helpers.write_to_file("result", board)
    helpers.write_to_file("result_energized", energized_board)
    print(f"{result=}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
