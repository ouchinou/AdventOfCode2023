import numpy as np
def parse_text_file(file_path):
    """
    Parse a text file and print each line.

    Parameters:
    - file_path (str): The path to the text file.
    """
  #  try:
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        line_idx = 0
        result = np.ones(num_lines)
        for line in lines:
            index_2_dot = line.find(':')
            index_separator = line.find('|')
            index_in_line = index_2_dot + 1

            # build set of result
            winning_set = set()
            while index_in_line < index_separator:
                if line[index_in_line].isnumeric():
                    number = line[index_in_line]
                    index_in_line += 1
                    while index_in_line < index_separator and line[index_in_line].isnumeric():
                        number += line[index_in_line]
                        index_in_line += 1
                    winning_set.add(number)
                else:
                    index_in_line += 1

            # build set of values
            number_set = set()
            index_in_line = index_separator + 1
            while index_in_line < len(line):
                if line[index_in_line].isnumeric():
                    number = line[index_in_line]
                    index_in_line += 1
                    while index_in_line < len(line) and line[index_in_line].isnumeric():
                        number += line[index_in_line]
                        index_in_line += 1
                    number_set.add(number)
                else:
                    index_in_line += 1

            weight_curr_card = result[line_idx]
            for i in range(line_idx+1,line_idx + len(number_set & winning_set) + 1):
                result[i] = result[i] + weight_curr_card

            line_idx += 1

        print("Result : " + str(np.sum(result)))



# Example usage:
file_path = 'input'
parse_text_file(file_path)