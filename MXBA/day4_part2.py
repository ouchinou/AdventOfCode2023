import re

infile = "data_day4.txt"
# infile = "exemple.txt"


with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:

    all_lines = puzzle_input.readlines()
    cards_copies = [1] * len(all_lines)

    for line_idx, line in enumerate(all_lines):
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

        # compute number of copies of the next cards
        nb_copies_of_current_card = cards_copies[line_idx]
        for i in range(nb_winners):
            cards_copies[line_idx + 1 + i] += nb_copies_of_current_card

        print(f"Card {card_number} => {cards_copies=}", file=outfile)

    txt = f"\n{sum(cards_copies)=}"
    print(txt)
    print(txt, file=outfile)
