import re
def parse_text_file(file_path):
    digit_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    """
    Parse a text file
    Parameters:
    - file_path (str): T
    he path to the text file.
    """
    try:
        with open(file_path, 'r') as file:
            total_sum = 0
            first_val=''
            second_val = ''
            for line in file:
                found_first_val = False
                found_last_val = False
                index_fval = len(line)-1
                index_lval = 0
                for i in range(len(line)):
                    if ((not found_first_val) and line[i].isnumeric()):
                        first_val = line[i]
                        found_first_val = True
                        index_fval = i
                    if ((not found_last_val) and line[-(i+1)].isnumeric()):
                        second_val = line[-(i+1)]
                        found_last_val = True
                        index_lval = len(line) - i - 1
                    if (found_last_val and found_first_val):
                        break

                if index_fval >= 2:
                    local_string = line[0:index_fval]
                    index_digits = [min([99999999] + [m.start() for m in re.finditer(digit, local_string)]) for digit in digit_list]
                    if min(index_digits)<99999999:
                        min_val_index = min([i for i in index_digits if i >= 0])
                        first_val = str(index_digits.index(min_val_index) + 1)

                if index_lval <= (len(line) - 3):
                    local_string = line[index_lval+1:len(line)-1]
                    index_digits = [max([-1] + [m.start() for m in re.finditer(digit, local_string)]) for digit in digit_list]
                    if max(index_digits) >= 0:
                        second_val = str(index_digits.index(max(index_digits)) + 1)
                print(first_val+second_val)
                total_sum += int(first_val+second_val)

            print(total_sum)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = 'input'
parse_text_file(file_path)