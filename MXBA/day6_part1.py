import numpy as np

infile = "data_day6.txt"
# infile = "exemple.txt"


with open(infile, "r") as puzzle_input:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # Time:        56     97
    # Distance:   546   1927
    times = [int(x) for x in lines[0].split(":")[1].split() if x]
    distances = [int(x) for x in lines[1].split(":")[1].split() if x]
    # print(f"{times=}")
    # print(f"{distances=}")
    runs = [[t, d] for t, d in zip(times, distances)]
    print(f"{runs=}")

    # proces each run
    total_wins = []
    for (time, record_distance) in runs:
        print("*" * 20)

        wins = 0
        # test all durations of "button press"
        for press_duration in range(1, time):  # skip first and last, as no distance covered
            move_duration = time - press_duration

            distance = press_duration * move_duration
            print(f"{press_duration=} {move_duration=} {distance=}")

            if distance > record_distance:
                wins += 1

        print(f"{wins=}")
        total_wins.append(wins)

    print(f"\n{total_wins=}")
    prod = np.prod(total_wins)
    print(f"\n{prod=}")
