import time


def extract_calibration_values_from_file(file_path):
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            digits = [int(d) for d in line if d.isdigit()]

            if digits:
                value = int(f"{digits[0]}{digits[-1]}")
                values.append(value)
    print(values)
    return values


def somme_des_elements(liste):
    return sum(liste)


start = time.time()
file_path = '../../Input/puzzle_2.txt'
all_sum = sum(extract_calibration_values_from_file(file_path))
print(all_sum)

end = time.time()
elapsed = end - start
print(f"elapsed time is {elapsed}")