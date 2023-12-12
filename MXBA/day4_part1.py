import re

infile = "data_day4.txt"
# infile = "exemple.txt"

result = []

with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:

    for line in puzzle_input:
        line = line.strip()
        line = line.replace("  ", " ")
        print(f"\n{line=}")

        # Card x: winning numbers | numbers played
        tmp = re.match("Card\s*(\d+):(.*)\|(.*)", line).groups()
        print(f"{tmp=}")
        card_number = int(tmp[0].strip())
        print(f"{card_number=}")
        winning_numbers = [int(x) for x in tmp[1].strip().split()]
        print(f"{winning_numbers=}")
        played_numbers = [int(x) for x in tmp[2].strip().split()]
        print(f"{played_numbers=}")

        # get number of played number that are winning numbers
        found_numbers = [x in winning_numbers for x in played_numbers]
        nb_winners = found_numbers.count(True)
        print(f"{found_numbers=}")
        print(f"{nb_winners=}")

        # compute number of points
        if nb_winners > 0:
            points = pow(2, nb_winners - 1)
            result.append(points)
            print(f"=> {points=}")
        else:
            points = 0
        print(f"Card {card_number} => {points=}", file=outfile)

    txt = f"\n{sum(result)=}"
    print(txt)
    print(txt, file=outfile)
