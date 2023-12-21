import alive_progress
import numpy as np
import os
import time
import helpers

infile = "data_day14.txt"
# infile = "exemple.txt"


def apply_gravity(platform):
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


def cycle(platform):
    # Roll rocks ("O") to north !
    apply_gravity(platform)

    # Roll rocks ("O") to west !
    platform = np.rot90(platform, k=-1)     # rotate 90 clockwise
    apply_gravity(platform)

    # Roll rocks ("O") to south !
    platform = np.rot90(platform, k=-1)     # rotate 90 clockwise
    apply_gravity(platform)

    # Roll rocks ("O") to est !
    platform = np.rot90(platform, k=-1)     # rotate 90 clockwise
    apply_gravity(platform)

    # reset to original position
    platform = np.rot90(platform, k=-1)     # rotate 90 clockwise


def main():

    result = 0

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:
        # read puzzle input
        platform = []
        cycles_hash = []
        cycles_loads = {}   # {hash : load_on_north_support}

        for line in puzzle_input:
            line = line.strip()
            platform.append([x for x in line])

        platform = np.asarray(platform)
        helpers.write_to_file("result", platform)

        CYCLES = 1_000_000_000
        with alive_progress.alive_bar(CYCLES, spinner="classic", bar="squares") as bar:

            for nb_cycles in range(CYCLES):
                cycle(platform)
                # create hash of data, to check loops
                hash_value = "".join(["".join(line) for line in platform])

                if hash_value in cycles_loads:
                    print(f"LOOP !!! => STOP at {bar.current}")
                    first_idx_of_loop = cycles_hash.index(hash_value)
                    last_idx_of_loop = len(cycles_loads)
                    print(f"{range(first_idx_of_loop, last_idx_of_loop)=} len={len(range(first_idx_of_loop, last_idx_of_loop))}")
                    break
                else:
                    # count load
                    full_load = 0
                    for i in range(0, platform.shape[0]):
                        row = platform[i]
                        # print(row)
                        load = (platform.shape[0] - i) * len(row[row == "O"])
                        # print(load)
                        full_load += load

                    cycles_hash.append(hash_value)
                    cycles_loads[hash_value] = full_load
                bar()

        # compute index of last cycle, according to the loops
        loop_range = range(first_idx_of_loop, last_idx_of_loop)
        final_idx = ((CYCLES - (first_idx_of_loop + 1)) % len(loop_range)) + first_idx_of_loop
        print(f"{final_idx=}")

        # get load for the last cycle index
        result = cycles_loads[cycles_hash[final_idx]]
        print(f"{result=}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
