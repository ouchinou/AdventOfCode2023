import time
import numpy as np
import re


def compute_hash(box_identification):
    current_val = 0
    for c in box_identification:
        current_val += ord(c)
        current_val *= 17
        current_val %= 256
    return current_val


def day15(file_path):
    with open(file_path, 'r') as file:
        line = file.read().splitlines()
        init_seq = line[0].split(',')
        result = 0

        number_box = 256
        # Each box contains a dict. Thanks to Python the dict can act to ordered dict :)
        boxes = [dict() for i in range(number_box)]

        for seq in init_seq:
            if '-' in seq:
                # Remove the element from the dict of the box identified with box_id
                box_id = seq.split('-')[0]
                boxes[compute_hash(box_id)].pop(box_id, None)
            else:
                # Add or update lens value
                [box_id, lens_value] = seq.split('=')
                box_dict = boxes[compute_hash(box_id)]
                if box_id in box_dict:
                    box_dict[box_id] = int(lens_value)  # update value, it keeps position
                else:
                    # Add new lens in the box
                    box_dict[box_id] = int(lens_value)

        # At this point we have all the boxes filled with the lens in order.
        for box_index in range(number_box):
            if len(boxes[box_index]) != 0:
                for i in range(len(boxes[box_index])):
                    # pop the first element of the dictionary (FIFO behaviour)
                    result += (box_index+1)*(i+1)*(k := next(iter(boxes[box_index])), boxes[box_index].pop(k))[1]

        print("Result : " + str(result))


start_time = time.time()
file_path = "input.txt"
day15(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
