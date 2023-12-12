import re

infile = "data_day1.txt"
numbers = []

to_find = "1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine".split()

numbers_value = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
                 "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:
    for line in puzzle_input.readlines():
        line = line.strip()
        print(f"{line=}")

        # find all indices of all elements to find
        positions = {}
        for num in to_find:
            all_iterations_idx = [m.start() for m in re.finditer(num, line)]

            # keep first and last
            if all_iterations_idx:
                positions[all_iterations_idx[0]] = num
                positions[all_iterations_idx[-1]] = num

        print(f"{positions=}")

        # get first and last
        keys = list(sorted(positions.keys()))
        print(f"{keys=}")
        calib_txt = numbers_value[positions[keys[0]]] + numbers_value[positions[keys[-1]]]
        calib_value = int(calib_txt)
        numbers.append(calib_value)
        print(calib_txt + "\n")

        txt = f"{line=} => {positions=} => {calib_txt=}"
        print(txt, file=outfile)

    txt = f"\n{sum(numbers)=}"
    print(txt)
    print(txt, file=outfile)
