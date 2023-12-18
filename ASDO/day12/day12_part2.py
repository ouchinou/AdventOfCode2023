import time
import numpy as np


memoize_combinations = dict()


def place_elements(group_list, state_list):
    if state_list+",".join(group_list) in memoize_combinations:
        # Already evaluate this combination, it is available in the dict
        return memoize_combinations[state_list+",".join(group_list)]
    else:
        curr_group = int(group_list[0])
        count = 0
        for spring_idx in range(len(state_list)):
            # find the first # or ?
            placement_possible = True
            if state_list[spring_idx] == '?' or state_list[spring_idx] == '#':
                # See if it is possible to reserve N spring
                if curr_group <= len(state_list)-spring_idx:
                    for i in range(1, curr_group):
                        if state_list[spring_idx+i]==".":
                            placement_possible = False
                    if curr_group < len(state_list)-spring_idx and state_list[spring_idx+curr_group] == '#':
                        placement_possible = False
                    if spring_idx > 0 and '#' in state_list[:spring_idx]:
                        placement_possible = False
                else:
                    placement_possible = False
            else:
                placement_possible = False

            if len(group_list) > 1:
                # more group to be placed
                if placement_possible:
                    count += place_elements(group_list[1:], state_list[(spring_idx+curr_group)+1:])
            else:
                # no more group to be placed
                if placement_possible:
                    # check if there is no more "#" in the end of the state_list
                    if not ('#' in state_list[(spring_idx + curr_group):]):
                        count += 1
        # memoization
        memoize_combinations[state_list + ",".join(group_list)] = count
        return count


def day12(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0

        for line in lines:
            [state_list, group_list] = line.split(' ')
            state_list = (state_list + '?')*4 + state_list
            group_list = [group for group in group_list.split(',')]
            group_list = group_list*5
            # remove redundant .
            while('..' in state_list):
                state_list = str.replace(state_list, '..', '.')
            result += place_elements(group_list, state_list)


        print("Result : " + str(result))


start_time = time.time()
file_path = "input.txt"
day12(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
