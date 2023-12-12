import time


def extract_last_digits(text):
    word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    current_word = ''
    for char in reversed(text):
        if char.isdigit():
            return (char)
        else:
            current_word = char.lower() + current_word  # Construire le mot à l'envers
            print(f'extract_last :{current_word}')
            res = [x in current_word for x in word_to_digit.keys()]
            if True in res:  # FOUND !
                idx = [x in current_word for x in word_to_digit.keys()].index(True)
                return idx


def extract_first_digits(text):
    word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    current_word = ''
    for char in text:
        if char.isdigit():
            return (char)
        else:
            current_word += char.lower()
            print(f'extract_first :{current_word}')
            res = [x in current_word for x in word_to_digit.keys()]
            if True in res:  # FOUND !
                idx = [x in current_word for x in word_to_digit.keys()].index(True)
                return idx


def extract_and_sum_calibration_values(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            print(line)
            first_digits = extract_first_digits(line)
            last_digits = extract_last_digits(line)
            print(int(f"{first_digits}{last_digits}"))
            total_sum += int(f"{first_digits}{last_digits}")
            print(total_sum)

    return total_sum


start = time.time()
file_path = '../../Input/puzzle_1.txt'
print(extract_and_sum_calibration_values(file_path))

end = time.time()
elapsed = end - start
print(f"elapsed time is {elapsed}")
