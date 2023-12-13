# IMPORTS

def process(time, distance):
    print("process on going")
    acc = 1
    for i in range(len(time)):
        cpt = 0
        for hold_time in range(time[i]):
            left_time = time[i] - hold_time
            target = hold_time * left_time
            if target > distance[i]:
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
                time_list = [int(elt) for elt in my_list[1:]]
            elif my_list[0] == "Distance:":
                distance_list = [int(elt) for elt in my_list[1:]]

            # Read the next line
            line = file.readline()

        print(process(time_list, distance_list))
        pass


if '__main__' == __name__:
    main()
