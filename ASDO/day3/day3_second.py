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
        total_sum = 0

        for line in lines:
            index_in_line = 0
            while(index_in_line<len(line)):
                if line[index_in_line] == "*":
                    local_res = 1
                    # let's try to find numbers around
                    nb_found = 0
                    # before star
                    if index_in_line>0 and line[index_in_line-1].isnumeric():
                        number = line[index_in_line - 1]
                        local_index = index_in_line - 2
                        while local_index >= 0 and line[local_index].isnumeric():
                            number = line[local_index] + number
                            local_index -= 1
                        local_res = local_res * int(number)
                        nb_found+=1

                    # after star
                    if index_in_line<len(line)-1 and line[index_in_line+1].isnumeric():
                        number = line[index_in_line+1]
                        local_index = index_in_line + 2
                        while local_index<len(line) and line[local_index].isnumeric():
                            number += line[local_index]
                            local_index += 1
                        local_res = local_res * int(number)
                        nb_found += 1

                    # line above
                    if line_idx>0:
                        line_to_inspect = lines[line_idx-1]
                        line_to_inspect = line_to_inspect[max(0,index_in_line-3):min(len(line_to_inspect), index_in_line + 4)]
                        local_index = 0
                        while local_index < len(line_to_inspect):
                            if line_to_inspect[local_index].isnumeric():
                                first_index = local_index
                                number = line_to_inspect[local_index]
                                last_index = local_index
                                while local_index+1 < len(line_to_inspect) and line_to_inspect[local_index+1].isnumeric():
                                    number += line_to_inspect[local_index+1]
                                    last_index = local_index+1
                                    local_index += 1
                                # number has been found: check if it is in the range of the star
                                if first_index <= 4 and last_index >= 2:
                                    local_res = local_res * int(number)
                                    nb_found += 1
                            local_index += 1

                    #line below
                    if line_idx < (num_lines-1):
                        line_to_inspect = lines[line_idx+1]
                        line_to_inspect = line_to_inspect[max(0,index_in_line-3):min(len(line_to_inspect), index_in_line + 4)]
                        local_index = 0
                        while local_index < len(line_to_inspect):
                            if line_to_inspect[local_index].isnumeric():
                                first_index = local_index
                                number = line_to_inspect[local_index]
                                last_index = local_index
                                while local_index+1 < len(line_to_inspect) and line_to_inspect[local_index+1].isnumeric():
                                    number += line_to_inspect[local_index+1]
                                    last_index = local_index+1
                                    local_index += 1
                                # number has been found: check if it is in the range of the star
                                if first_index <= 4 and last_index >= 2:
                                    local_res = local_res * int(number)
                                    nb_found += 1
                            local_index += 1

                    if nb_found>=2:
                        if nb_found == 2:
                            total_sum += local_res
                        else:
                            print("Unexpected number of numbers ")

                index_in_line += 1

            # Process each line here
            line_idx +=1
        print("Result : " + str(total_sum))
    # except FileNotFoundError:
    #     print(f"File not found: {file_path}")
    # except Exception as e:
    #     print(f"An error occurred: {e}")


# Example usage:
file_path = 'input'
parse_text_file(file_path)