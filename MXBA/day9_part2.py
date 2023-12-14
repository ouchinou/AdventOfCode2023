# import alive_progress
import numpy as np
# from collections import Counter
import os
# import functools
# from pprint import pprint as pp

infile = "data_day9.txt"
# infile = "exemple.txt"


class History:
    def __init__(self, line):
        self.values = [int(x) for x in line.split()]

        # printp("*" * 20)
        # printp(self.values)

        # compute
        diff_history = [[0] + self.values]

        diffs = self.get_diff(self.values)
        diff_history.append([0] + diffs)

        # printp(diffs)
        while not all(n == 0 for n in diffs):
            diffs = self.get_diff(diffs)
            diff_history.append([0] + diffs)
            # printp(diffs)

        # printp("--- extrapolate ---")
        # extrapolate
        self.last_increase = 0
        for idx, hist_line in enumerate(diff_history[::-1]):
            if idx == 0:
                continue

            if self.last_increase == 0:
                self.last_increase = hist_line[1]
            else:
                self.last_increase = hist_line[1] - self.last_increase
            hist_line[0] = self.last_increase
            # printp(f"=> {hist_line}")

    def get_diff(self, lst):
        return [x for x in np.diff(np.asarray(lst, np.int64)).tolist()]

    def __str__(self):
        return str(self.values)


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # create hads of cards
    history_list = [History(x).last_increase for x in lines]
    # for h in history_list:
    #     # printp(h)

    # print(history_list)
    print(sum(history_list))
