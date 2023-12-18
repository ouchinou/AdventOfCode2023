import time

# This solution is almost a duplicated from day10

# south = 0, north = 1, west = 2, east = 3
# [(i_offset, j_offset, direction),(i_offset, j_offset, direction)]
direction_from_south = {'.': [(-1, 0, 0)], '/': [(0, 1, 2)], '\\': [(0, -1, 3)], '|': [(-1, 0, 0)], '-': [(0, -1, 3), (0, 1, 2)]}
direction_from_north = {'.': [(1, 0, 1)], '/': [(0, -1, 3)], '\\': [(0, 1, 2)], '|': [(1, 0, 1)], '-': [(0, -1, 3), (0, 1, 2)]}
direction_from_west = {'.': [(0, 1, 2)], '/': [(-1, 0, 0)], '\\': [(1, 0, 1)], '|': [(-1, 0, 0), (1, 0, 1)], '-': [(0, 1, 2)]}
direction_from_east = {'.': [(0, -1, 3)], '/': [(1, 0, 1)], '\\': [(-1, 0, 0)], '|': [(-1, 0, 0), (1, 0, 1)], '-': [(0, -1, 3)]}

directions = [direction_from_south, direction_from_north, direction_from_west, direction_from_east]


def day16(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        nb_lines = len(lines)
        nb_columns = len(lines[0])

        # start with 1 beam, index 0,0 and comes from west
        beam_to_analyze = [(0, 0, 2)]
        beam_position_set = set()

        while len(beam_to_analyze) != 0:
            (curr_beam_i, curr_beam_j, curr_beam_dir) = beam_to_analyze.pop()
            current_beam = (curr_beam_i, curr_beam_j, curr_beam_dir)
            while (current_beam not in beam_position_set) and 0 <= curr_beam_i < nb_lines and 0 <= curr_beam_j < nb_columns: # TODO find stop condition
                # save current beam
                beam_position_set.add(current_beam)

                dir_dict = directions[curr_beam_dir]
                beam_status = dir_dict[lines[curr_beam_i][curr_beam_j]]
                for i in range(1, len(beam_status)):
                    # save those beam for later
                    beam_to_analyze.append((curr_beam_i + beam_status[i][0], curr_beam_j + beam_status[i][1], beam_status[i][2]))

                # compute new position of the beam
                curr_beam_dir = beam_status[0][2]
                curr_beam_i = curr_beam_i + beam_status[0][0]
                curr_beam_j = curr_beam_j + beam_status[0][1]
                current_beam = (curr_beam_i, curr_beam_j, curr_beam_dir)

        # build a set with the coordinates only, as beam_position_set contains also direction,
        # so it duplicated the number of elements to count
        unique_coord = set([(beam[0], beam[1]) for beam in beam_position_set])

        print("Result : " + str(len(unique_coord)))


start_time = time.time()
file_path = "input.txt"
day16(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
