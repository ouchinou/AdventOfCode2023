# IMPORTS

def process(time, distance):
    print("process on going")
    acc = 1
    cpt = 0
    for hold_time in range(time):
        left_time = time - hold_time
        target = hold_time * left_time
        if target > distance:
            cpt = cpt + 1
    acc = acc * cpt
    return acc


def main():
    time_list = []
    distance_list = []
    # Open the file in read mode ('r')
    with open('input.txt', 'r') as file:
        # Read a line
        line = file.readline()

        # Loop until the line is empty (which means we've read all lines)
        while line:
            # Process the line
            # print(line.strip())  # .strip() removes leading/trailing white spaces
            my_list = line.split()
            if my_list[0] == "Time:":
                time_list = [elt for elt in my_list[1:]]
                time_list = int("".join(time_list))
            elif my_list[0] == "Distance:":
                distance_list = [elt for elt in my_list[1:]]
                distance_list = int("".join(distance_list))

            # Read the next line
            line = file.readline()
        #print(time_list, distance_list)
        print(process(time_list, distance_list))
        pass


if '__main__' == __name__:
    main()
