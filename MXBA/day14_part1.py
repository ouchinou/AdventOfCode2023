# import alive_progress
import numpy as np
import os
import time
import helpers


infile = "data_day14.txt"
# infile = "exemple.txt"


def main():

    result = 0

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        # read puzzle input
        platform = []

        for line in puzzle_input:
            line = line.strip()
            platform.append([x for x in line])

        platform = np.asarray(platform)
        helpers.write_to_file("result", platform)

        # Roll rocks ("O") to north !
        for i in range(1, platform.shape[0], 1):
            for j in range(platform.shape[1]):
                if platform[i, j] == "O":
                    # move rock until (end of board) or (a rounded rock "O") or (a cube-shaped rock "#")
                    next_position = i
                    while True:
                        current_position = next_position
                        next_position = next_position - 1

                        # end of board ?
                        if next_position < 0:
                            break

                        # rounded or cube-shaped rock ?
                        if platform[next_position, j] in ["O", "#"]:
                            break

                        # nothing stops the rocks, let it move
                        platform[next_position, j] = "O"
                        platform[current_position, j] = "."

            # helpers.write_to_file(f"result_{i}_{j}", platform)
        helpers.write_to_file("result", platform)

        # count load
        result = 0
        for i in range(0, platform.shape[0]):
            row = platform[i]
            # print(row)
            load = (platform.shape[0] - i) * len(row[row == "O"])
            print(load)
            result += load

        print(f"{result=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
