def parse_text_file(file_path):
    """
    Parse a text file and print each line.

    Parameters:
    - file_path (str): The path to the text file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
            num_lines = len(lines)
            line_idx = 0
            total_sum = 0
            for line in lines:
                index_in_line = 0
                while(index_in_line<len(line)):
                    if line[index_in_line].isnumeric():
                        first_index = index_in_line
                        number = line[index_in_line]
                        last_index = index_in_line
                        index_in_line +=1
                        while index_in_line<len(line) and line[index_in_line].isnumeric():
                            number += line[index_in_line]
                            last_index = index_in_line
                            index_in_line += 1
                        # check if it has adjacent symbols:
                        is_part = False

                        if first_index > 0 and line[first_index-1] != '.': #in the same line before
                            is_part = True
                        else:
                            if last_index < len(line)-1: #in the same line after
                                if (line[last_index + 1] != '.'):
                                    is_part = True
                            #line above
                            if(line_idx > 0):
                                line_above = lines[line_idx - 1]
                                line_above = line_above[max(0, first_index-1):min(len(line_above), last_index+2)]
                                if line_above.count('.') != len(line_above):
                                    for i in range(len(line_above)):
                                        if (not line_above[i].isnumeric()) and line_above[i] != '.':
                                            is_part = True

                            if (line_idx < (num_lines-1)):
                                line_below = lines[line_idx + 1]
                                line_below = line_below[
                                             max(0, first_index - 1):min(len(line_below), last_index + 2)]
                                if line_below.count('.') != len(line_below):
                                    for i in range(len(line_below)):
                                        if (not line_below[i].isnumeric()) and line_below[i] != '.':
                                            is_part = True
                        print(" Number " + str(number) + " is part is " + str(is_part))
                        if (is_part):
                            total_sum += int(number)
                    else:
                        index_in_line+=1


                # Process each line here
                line_idx +=1
            print("Result : " + str(total_sum))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = 'input'
parse_text_file(file_path)