import time


def day4(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 1

        time_table = lines[0].split()[1:]
        dist_table = lines[1].split()[1:]

        for i in range(len(time_table)):
            # For each time/distance couple:
            available_time = int(time_table[i])
            distance_to_beat = int(dist_table[i])
            nb_possible_combination = 0
            for press_duration in range(1, available_time):
                if (available_time-press_duration)*press_duration > distance_to_beat:
                    nb_possible_combination += 1
            result *=nb_possible_combination

        print("Result : " + str(result))


start_time = time.time()
file_path = 'input'
day4(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
