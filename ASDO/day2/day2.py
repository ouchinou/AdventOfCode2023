import numpy as np
def parse_text_file(file_path):
    """
    Parse a text file and print each line.

    Parameters:
    - file_path (str): The path to the text file.
    """
    try:
        with open(file_path, 'r') as file:
            colors = ["blue", "red", "green"]
            colors_true_max = [14, 12, 13]
            line_index = 0
            total_possible_games = 0
            total_power = 0
            for line in file:
                max_values = [0, 0, 0]
                list_run = line[line.find(":")+2:len(line)-1].split("; ")
                for run in list_run:
                    for i in range(len(colors)):
                        color_nb = ''
                        color_idx = run.find(colors[i]) - 2
                        if (color_idx > -1):
                            while (run[color_idx].isnumeric()):
                                color_nb = run[color_idx] + color_nb
                                color_idx-=1
                        else:
                            color_nb = '0'
                        max_values[i] = max(max_values[i], int(color_nb))

                compare_values = np.greater(max_values, colors_true_max)
                game_is_possible = compare_values[0] or compare_values[1] or compare_values[2]
                total_power += (max_values[0] * max_values[1] * max_values[2])
                print("Game " + str(line_index+1) + " is possible :" + str(not game_is_possible))
                print("Power of the game = " + str(max_values[0] * max_values[1] * max_values[2]))
                if not game_is_possible:
                    total_possible_games = total_possible_games + line_index+1
                # Process each line here
                line_index+=1
            print("result " + str(total_power))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
file_path = 'input'
parse_text_file(file_path)