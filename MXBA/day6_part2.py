import alive_progress
import numpy as np
import os

infile = "data_day6.txt"
# infile = "exemple.txt"


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # Time:        56     97
    # Distance:   546   1927
    time = int(lines[0].split(":")[1].replace(" ", ""))
    record_distance = int(lines[1].split(":")[1].replace(" ", ""))
    print(f"{time=}")
    print(f"{record_distance=}")

    # proces each run
    total_wins = 0

    # test all durations of "button press"
    with alive_progress.alive_bar(time, spinner="classic", bar="squares") as bar:
        for press_duration in range(1, time):  # skip first and last, as no distance covered
            move_duration = time - press_duration

            distance = press_duration * move_duration
            # print(f"{press_duration=} {move_duration=} {distance=}")

            if distance > record_distance:
                total_wins += 1
            bar()

    print(f"\n{total_wins=}")
    prod = np.prod(total_wins)
    print(f"\n{prod=}")
