import numpy as np
import math

def map_parser(line_idx, lines, num_lines):
    map_original = np.array([],int)
    while line_idx < num_lines and len(lines[line_idx]) > 0 and (not lines[line_idx][0].isnumeric()):
        line_idx += 1

    cnt = 0
    while line_idx < num_lines and len(lines[line_idx]) > 0 and lines[line_idx][0].isnumeric():
        line = lines[line_idx].split(' ')
        for i in range(len(line)):
            line[i] = int(line[i])
        map_original = np.append(map_original, line)
        line_idx += 1
        cnt += 1
    map_original = map_original.reshape(cnt, 3)
    map_original = map_original[np.argsort(map_original[:, 1])]

    map_original_improved = np.array([],int)
    starting_value = 0
    for i in range(cnt):
        if map_original[i][1] > starting_value:
            map_original_improved = np.append(map_original_improved, [starting_value, 0])
        map_original_improved = np.append(map_original_improved,
                                         [map_original[i][1], map_original[i][0] - map_original[i][1]])
        starting_value = map_original[i][1] + map_original[i][2]

    map_original_improved = np.append(map_original_improved, [starting_value, 0])
    map_original_improved = map_original_improved.reshape(int(len(map_original_improved) / 2), 2)
    return map_original_improved, line_idx


def compute_conversion(map, input_val):
    i = 0
    while i < len(map) and map[i][0] <= input_val:
        i += 1
    output_val = input_val + map[i-1][1]
    return output_val


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

        # extract seed list:
        seed_set = []
        seed_line = lines[0]
        index_in_line = seed_line.find(':') + 1
        while index_in_line < len(seed_line):
            if seed_line[index_in_line].isnumeric():
                number = seed_line[index_in_line]
                index_in_line += 1
                while index_in_line < len(seed_line) and seed_line[index_in_line].isnumeric():
                    number += seed_line[index_in_line]
                    index_in_line += 1
                seed_set.append(int(number))
            else:
                index_in_line += 1
        line_idx = 2

        # create the 7 maps
        [seed_2_soil, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [soil_2_fertilizer, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [fertilizer_2_water, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [water_2_light, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [light_2_temp, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [temp_2_humid, line_idx] = map_parser(line_idx, lines, num_lines)
        line_idx += 2
        [humid_to_location, line_idx] = map_parser(line_idx, lines, num_lines)

        result = math.inf
        for seed in range(len(seed_set)):
            conversion = compute_conversion(seed_2_soil, seed_set[seed])
            conversion = compute_conversion(soil_2_fertilizer, conversion)
            conversion = compute_conversion(fertilizer_2_water, conversion)
            conversion = compute_conversion(water_2_light, conversion)
            conversion = compute_conversion(light_2_temp, conversion)
            conversion = compute_conversion(temp_2_humid, conversion)
            conversion = compute_conversion(humid_to_location, conversion)
            result = min(result, conversion)

            print("seed : " + str(seed) + " gives " + str(conversion))
        print("Result : " + str(result))


# Example usage:
file_path = 'input'
parse_text_file(file_path)
