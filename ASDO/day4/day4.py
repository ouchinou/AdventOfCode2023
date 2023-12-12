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
        result = 0

        for line in lines:
            value = 0 #2^nb_elem_commun

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
#            firstSet & secondSet
            if len(number_set & winning_set) > 0:
                result = result + pow(2, (len(number_set & winning_set)-1))

            line_idx += 1

        print("Result : " + str(result))



# Example usage:
file_path = 'input'
parse_text_file(file_path)