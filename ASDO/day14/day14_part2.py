import time
import numpy as np
import re


def write_to_file(file_path, content):
    try:
        # Open the file in write mode ('w')
        with open(file_path, 'w') as file:
            # Write the content to the file
            for line in content:
                file.write(line + "\n")
        print(f"Content successfully written to {file_path}")
    except IOError as e:
        print(f"Error writing to file: {e}")


memoize = dict()
round_rocks_position_history = dict()


class LineColumn:
    """
    class to specify 1 line or 1 column of the input pattern
    """
    def __init__(self, pattern):
        # extract indexes of the fixed rocks in the line/column
        self.fixed_rock_idx = [c.start() for c in re.finditer('#', pattern)]

        # build zones. A zone is a part of the line/column that is between two fixed rocks
        # each element of zones contains the min and the max index for the zone
        self.zones = []
        if len(self.fixed_rock_idx) != 0:
            if self.fixed_rock_idx[0] != 0:
                # add the first zone before first fixed rock
                self.zones += [(0, self.fixed_rock_idx[0]-1)]

            for i in range(len(self.fixed_rock_idx)-1):
                if self.fixed_rock_idx[i] != self.fixed_rock_idx[i+1]-1:
                    self.zones += [(self.fixed_rock_idx[i]+1, self.fixed_rock_idx[i+1]-1)]

            if self.fixed_rock_idx[-1] != len(pattern)-1:
                # add the last zone after last fixed rock
                self.zones += [(self.fixed_rock_idx[-1]+1, len(pattern)-1)]
        else:
            # no rock in line/column, only one big zone
            self.zones = [(0, len(pattern)-1)]

    def tilt_left(self, round_rock_index):
        # used to tilt to west or north
        # round_rock_index is the index in the current line/column
        key = str(self) + str(round_rock_index) + 'l'
        if key in memoize:
            return memoize[key]
        else:
            for zone in self.zones:
                if zone[0] <= round_rock_index <= zone[1]:
                    memoize[key] = zone[0]
                    return zone[0]

    def tilt_right(self, round_rock_index):
        # used to tilt to east or south
        # round_rock_index is index in the current line/column
        key = str(self) + str(round_rock_index) + 'r'
        if key in memoize:
            return memoize[key]
        else:
            for zone in self.zones:
                if zone[0] <= round_rock_index <= zone[1]:
                    memoize[key] = zone[1]
                    return zone[1]


def day14(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        nb_lines = len(lines)
        nb_columns = len(lines[0])
        result = 0
        number_cycles = 1000000000

        # Two arrays, one containing a description of all the lines and one for the description of the columns
        lines_mapping = []
        column_mapping = []
        # list of the round rock indexes
        round_rock_indexes = []
        for line_idx in range(nb_lines):
            lines_mapping = lines_mapping + [LineColumn(lines[line_idx])]
            round_rock_col_index = [c.start() for c in re.finditer('O', lines[line_idx])]
            round_rock_indexes += [(line_idx, col_idx) for col_idx in round_rock_col_index]

        for column_idx in range(nb_columns):
            column_mapping = column_mapping + [LineColumn("".join([line[column_idx] for line in lines]))]

        cycle = 0
        last_runs = False
        while cycle < number_cycles:
            # Perform a cycle of tilts:
            
            # 1 - compute the position of each rock after turning north
            position_index_set = set()
            for i in range(len(round_rock_indexes)):
                [line_rock_idx, colum_rock_idx] = round_rock_indexes[i]
                new_pos = (column_mapping[colum_rock_idx].tilt_left(line_rock_idx), colum_rock_idx)
                # if the position is already taken by a rock, the rock should stack
                while new_pos in position_index_set:
                    new_pos = (new_pos[0] + 1, new_pos[1])
                position_index_set.add(new_pos)
                round_rock_indexes[i] = new_pos

            # 2 - compute the position of each rock after turning west
            position_index_set = set()
            for i in range(len(round_rock_indexes)):
                [line_rock_idx, colum_rock_idx] = round_rock_indexes[i]
                new_pos = (line_rock_idx, lines_mapping[line_rock_idx].tilt_left(colum_rock_idx))
                # if the position is already taken by a rock, the rock should stack
                while new_pos in position_index_set:
                    new_pos = (new_pos[0], new_pos[1] + 1)
                position_index_set.add(new_pos)
                round_rock_indexes[i] = new_pos

            # 3 - compute the position of each rock after turning south
            position_index_set = set()
            for i in range(len(round_rock_indexes)):
                [line_rock_idx, colum_rock_idx] = round_rock_indexes[i]
                new_pos = (column_mapping[colum_rock_idx].tilt_right(line_rock_idx), colum_rock_idx)
                # if the position is already taken by a rock, the rock should stack
                while new_pos in position_index_set:
                    new_pos = (new_pos[0] - 1, new_pos[1])
                position_index_set.add(new_pos)
                round_rock_indexes[i] = new_pos

            # 4 - compute the position of each rock after turning east
            position_index_set = set()
            for i in range(len(round_rock_indexes)):
                [line_rock_idx, colum_rock_idx] = round_rock_indexes[i]
                new_pos = (line_rock_idx, lines_mapping[line_rock_idx].tilt_right(colum_rock_idx))
                # if the position is already taken by a rock, the rock should stack
                while new_pos in position_index_set:
                    new_pos = (new_pos[0], new_pos[1] - 1)
                position_index_set.add(new_pos)
                round_rock_indexes[i] = new_pos

            # Check for early stopping if a repeating pattern is found
            if not last_runs:
                sum_coord = np.sum(np.array(round_rock_indexes), axis=0)
                key = str(sum_coord[0] + 10000*sum_coord[1])
                if key in round_rocks_position_history:
                    print("Stopping process, loop detected at " + str(cycle) + " same as " +
                          str(round_rocks_position_history[key]))
                    # If a pattern is detected,
                    # we can skip a lot of simulations and run the last simulations cycle up to the target cycles
                    cycle = number_cycles - ((number_cycles-cycle) % (cycle-round_rocks_position_history[key]))
                    last_runs = True
                else:
                    # Add position of all the round rock in the dict
                    round_rocks_position_history[key] = cycle
            cycle += 1

        # Post process, once we know the position of the round rocks after the number of target cycles
        for rock in round_rock_indexes:
            result += (nb_lines - rock[0])
        print("Result : " + str(result))

        # Uncomment to visualize output
        # for i in range(nb_lines):
        #     lines[i] = lines[i].replace('O', '.')
        #
        # for rock_idx in round_rock_indexes:
        #     lines[rock_idx[0]] = lines[rock_idx[0]][:rock_idx[1]] + 'O' + lines[rock_idx[0]][rock_idx[1]+1:]
        # write_to_file("output.txt", lines)


start_time = time.time()
file_path = "input.txt"
day14(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
