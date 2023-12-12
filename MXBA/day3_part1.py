import re
import numpy as np

infile = "data_day3.txt"
# infile = "exemple.txt"

bad_chars = ".abcdefghijklmnopqrstuvwxyz"
result = []

with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:
    all_lines = puzzle_input.readlines()

    for line_idx, line in enumerate(all_lines):
        line = line.strip()
        print(f"\n{line=}")

        # find numbers
        all_iterations_match = [m for m in re.finditer("\d+", line)]
        print(all_iterations_match)

        for number_found in all_iterations_match:
            # search special char just before and just after each number found
            value = int(number_found.group(0))
            beg_idx = number_found.start()
            end_idx = number_found.end() - 1
            print(f"*** {value} ***")

            previous_char_idx = beg_idx - 1
            if (previous_char_idx >= 0) and (line[previous_char_idx] not in bad_chars):
                print(f"Previous = YES ({line[previous_char_idx]})")
                result.append(int(value))
                print(f"{value} => char before", file=outfile)
                continue

            next_char_idx = end_idx + 1
            if (next_char_idx < len(line)) and (line[next_char_idx] not in bad_chars):
                print(f"NEXT = YES ({line[next_char_idx]})")
                result.append(int(value))
                print(f"{value} => char after", file=outfile)
                continue

            # search special char in previous line just above and diagonals
            if (line_idx - 1) > 0:
                beg_idx = max(0, number_found.start() - 1)
                end_idx = min(number_found.end() + 1, len(line))

                if (beg_idx >= 0) and (end_idx <= len(line)):
                    area = all_lines[line_idx - 1][beg_idx:end_idx]
                    print(f"ABOVE {area=}")
                    found = np.any([x not in bad_chars for x in area])
                    print(f"=> {found=}")
                    if found:
                        print(f"{value} => line above", file=outfile)
                        result.append(int(value))
                        continue

            # search special char in previous line just under and diagonals
            if (line_idx + 1) < (len(all_lines)):
                beg_idx = max(0, number_found.start() - 1)
                end_idx = min(number_found.end() + 1, len(line))

                if (beg_idx >= 0) and (end_idx <= len(line)):
                    area = all_lines[line_idx + 1][beg_idx:end_idx]
                    print(f"AFTER {area=}")
                    found = np.any([x not in bad_chars for x in area])
                    print(f"=> {found=}")
                    if found:
                        print(f"{value} => line under", file=outfile)
                        result.append(int(value))
                        continue

            print(f"{value} => NOT PART NUMBER", file=outfile)

    txt = f"\n{sum(result)=}"
    print(txt)
    print(txt, file=outfile)
