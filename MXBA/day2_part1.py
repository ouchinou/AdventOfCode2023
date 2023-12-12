# import re

infile = "data_day2.txt"
# infile = "exemple.txt"

games_OK = []
max_for_colors = {"red": 12, "green": 13, "blue": 14}

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

        for rec in record_list:
            tmp = rec.split(",")
            OK = True

            # 3 blue, 4 red
            for dices in tmp:
                value, color = dices.split()
                value = int(value)
                if value > max_for_colors[color]:
                    OK = False
                    print(f"{color}:{value} > {max_for_colors[color]}")
                    break

            if not OK:
                break

        # all checks are OK
        if OK:
            print("OK")
            games_OK.append(game_number)
        else:
            print("NOPE")

        txt = f"{game_number} => {OK=}"
        print(txt, file=outfile)

    txt = f"\n{sum(games_OK)=}"
    print(txt)
    print(txt, file=outfile)
