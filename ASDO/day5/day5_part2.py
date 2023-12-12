import numpy as np
import math
import time


# Create more exploitable maps
# from line_idx, finds the header of the next map and then creates a maps that looks like this:
# [source, offset]. Where source is the first value and offset is the transformation to create destination value
# Each range covered by each line are continuous
def map_parser(line_idx, lines, num_lines):
    map_original = np.array([], int)
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

    map_original_improved = np.array([], int)
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


def compute_conversion(map, input_val, input_range):
    i = 0
    output_val = np.array([], int)
    updated_range = input_range
    while updated_range>0:
        while i < len(map) and map[i][0] <= (input_val):
            i += 1

        if i < len(map) and input_val + updated_range >= map[i][0]:
            size_curr_range = map[i][0] - input_val
            output_val = np.append(output_val, [input_val + map[i - 1][1], size_curr_range])
            updated_range = updated_range - size_curr_range
            input_val += size_curr_range
        else:
            #range contains all the values
            size_curr_range = updated_range
            output_val = np.append(output_val, [input_val + map[i - 1][1], size_curr_range])
            updated_range = updated_range - size_curr_range
    return output_val


def day5_part2(file_path):
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

        # compute each seed to location map
        result = np.array([], int)
        # Can probably be done in a cleaner way
        for seed in range(int(len(seed_set) / 2)):
            conversion = compute_conversion(seed_2_soil, seed_set[2*seed], seed_set[2*seed+1])
            conversion2 = np.array([], int)
            for i in range(int(len(conversion)/2)):
                conversion2 = np.append(conversion2, compute_conversion(soil_2_fertilizer, conversion[2*i], conversion[2*i+1]))
            conversion3 = np.array([], int)
            for i in range(int(len(conversion2)/2)):
                conversion3 = np.append(conversion3, compute_conversion(fertilizer_2_water, conversion2[2*i], conversion2[2*i+1]))
            conversion4 = np.array([], int)
            for i in range(int(len(conversion3)/2)):
                conversion4 = np.append(conversion4, compute_conversion(water_2_light, conversion3[2*i], conversion3[2*i+1]))
            conversion5 = np.array([], int)
            for i in range(int(len(conversion4)/2)):
                conversion5 = np.append(conversion5, compute_conversion(light_2_temp, conversion4[2*i], conversion4[2*i+1]))
            conversion6 = np.array([], int)
            for i in range(int(len(conversion5)/2)):
                conversion6 = np.append(conversion6, compute_conversion(temp_2_humid, conversion5[2*i], conversion5[2*i+1]))
            conversion7 = np.array([], int)
            for i in range(int(len(conversion6)/2)):
                conversion7 = np.append(conversion7, compute_conversion(humid_to_location, conversion6[2*i], conversion6[2*i+1]))

            result = np.append(result, conversion7)
            #print("seed : " + str(seed) + " gives " + str(conversion7))

        # result is a list of couples: [location start, range] where location is the first value of the location group
        # and range is the size of this group.
        # for example: [10, 2] means that from some seeds we obtained location 10 and 11.
        result = result.reshape(int(len(result) / 2), 2)
        # We want the minimum location, so we just have to sort according to location start
        result = result[np.argsort(result[:, 0])]
        print("Result : " + str(result[0]))


start_time = time.time()
file_path = 'input'
day5_part2(file_path)
print("--- %s seconds ---" % (time.time() - start_time))
