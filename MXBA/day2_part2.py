import numpy as np

infile = "data_day2.txt"
# infile = "exemple.txt"

result = []

with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:
    for line in puzzle_input.readlines():
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        line = line.strip()
        print(f"{line=}")

        # game number / records
        game_number, records_str = line.split(":")

        # clean game number - Game 1
        game_number = int(game_number.replace("Game", "").strip())
        print(f"{game_number=}")

        # extract records - 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        record_list = records_str.split(";")

        # get maximum number of dices of each color for each record
        max_for_colors = {"red": 0, "green": 0, "blue": 0}
        for rec in record_list:
            tmp = rec.split(",")

            # 3 blue, 4 red
            for dices in tmp:
                value, color = dices.split()
                value = int(value)

                # get max number for this color (compared with prevous records)
                max_for_colors[color] = max(max_for_colors[color], value)
            print(f"{max_for_colors}")

        print(f"=> {max_for_colors}")

        # compute power of colors
        power = np.prod(list(max_for_colors.values()))
        print(f"=> {power}")

        # add power to the sum
        result.append(power)

        txt = f"{game_number} => {max_for_colors} => {power}"
        print(txt, file=outfile)

    txt = f"\n{sum(result)=}"
    print(txt)
    print(txt, file=outfile)
