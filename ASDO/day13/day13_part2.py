import time
import numpy as np
import collections


def day13(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0
        line_idx = 0
        cnt_pattern = 1
        while line_idx < num_lines:
            print("pattern " + str(cnt_pattern))
            nb_col = len(lines[line_idx])
            nb_lines = line_idx
            # extract current pattern
            pattern = np.array([])
            while line_idx < num_lines and len(lines[line_idx]) > 0:
                pattern = np.concatenate((pattern, [c for c in lines[line_idx]]))
                line_idx += 1
            nb_lines = line_idx - nb_lines
            pattern = np.reshape(pattern, (nb_lines, nb_col))

            check_line_needed = True
            smudge_found = False
            # check columns
            for pattern_j in range(nb_col - 1):
                col_to_check = min(pattern_j + 1, nb_col - 1 - pattern_j)
                column_is_mirror = True
                smudge_found = False
                for offset in range(col_to_check):
                    comparison = np.equal(pattern[:, pattern_j - offset], pattern[:, pattern_j + 1 + offset])
                    if (not smudge_found) and collections.Counter(comparison)[False] == 1:
                        smudge_found = True
                    elif not comparison.all():
                        column_is_mirror = False
                        break

                if column_is_mirror and smudge_found:
                    #print("pattern " + str(cnt_pattern) + " colum " + str(pattern_j))
                    result += pattern_j + 1
                    check_line_needed = False
                    break

            # check lines
            if check_line_needed:
                for pattern_i in range(nb_lines - 1):
                    line_to_check = min(pattern_i + 1, nb_lines - 1 - pattern_i)
                    line_is_mirror = True
                    smudge_found = False
                    for offset in range(line_to_check):
                        comparison = np.equal(pattern[pattern_i - offset, :], pattern[pattern_i + 1 + offset, :])
                        if (not smudge_found) and collections.Counter(comparison)[False] == 1:
                            smudge_found = True
                        elif not comparison.all():
                            line_is_mirror = False
                            break

                    if line_is_mirror and smudge_found:
                        #print("pattern " + str(cnt_pattern) + " line " + str(pattern_i))
                        result += (pattern_i + 1) * 100
                        break

            line_idx += 1
            cnt_pattern += 1

        print("Result : " + str(result))


start_time = time.time()
file_path = "input.txt"
day13(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
