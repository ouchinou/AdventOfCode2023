infile = "data_day1.txt"

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = []

with open(infile, "r") as puzzle_input, open("results.txt", "w") as outfile:
    for line in puzzle_input.readlines():
        line = line.strip()

        # remove letters
        only_numbers = line
        for letter in alphabet:
            only_numbers = only_numbers.replace(letter, "")

        # get first and last
        calib_txt = only_numbers[0] + only_numbers[-1]
        calib_value = int(calib_txt)
        numbers.append(calib_value)

        txt = f"{line} => {only_numbers=} => {calib_txt}"
        print(txt)
        print(txt, file=outfile)

    txt = f"\n{sum(numbers)=}"
    print(txt)
    print(txt, file=outfile)
