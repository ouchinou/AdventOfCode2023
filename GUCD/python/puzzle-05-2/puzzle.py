# IMPORTS
import operator as ope
import time

def process(_data):
    print("process on going")
    isMapped = False
    isReached = False
    data = [0, 0, 0, 0, 0, 0, 0, 0]
    seed = [0, 0, 0, 0]
    n = 0
    location = 0
    while True:

        data[7] = location

        for step, my_list in sorted(_data.items(), reverse=True):
            isMapped = False
            if int(step[0]) == 0:
                seed = [ech for ech in my_list]
            else:
                for ech in my_list:
                    if ope.itemgetter(0)(ech) <= data[int(step[0])] < (ope.itemgetter(0)(ech) + ope.itemgetter(2)(ech)):
                        data[int(step[0])-1] = data[int(step[0])] + (ope.itemgetter(1)(ech) - ope.itemgetter(0)(ech))
                        isMapped = True
                    if not isMapped:
                        data[int(step[0])-1] = data[int(step[0])]


        for i in range(0, 4, 2):
            if seed[i] <= data[0] < (seed[i] + seed[i + 1]):
                isReached = True

        if isReached:
            break

        location = location + 1
        #print(location)

    return location


def main():
    start = time.time()
    data = {}
    key = None
    step = 0
    # Open the file in read mode ('r')
    with open('input.txt', 'r') as file:
        # Read a line
        line = file.readline()

        # Loop until the line is empty (which means we've read all lines)
        while line:
            # Process the line
            # print(line.strip())  # .strip() removes leading/trailing white spaces

            if line.strip():
                # If the line contains a colon, it's a key
                if ":" in line:
                    # The key is the part before the colon
                    key = (str(step) + line.split(":")[0]).strip()
                    # Initialize an empty list for this key in the dictionary
                    data[key] = []
                    if not step:
                        data[key].extend(list(map(int, line.split()[1:])))
                    step = step + 1
                else:
                    # Otherwise, the line is a list of numbers
                    # Convert the numbers to integers and add them to the current key's list
                    data[key].append(list(map(int, line.split())))

            # Read the next line
            line = file.readline()

        #print(data)
        print(process(data))
        end = time.time()
        elapsed = end - start
        print(elapsed)
        pass


if '__main__' == __name__:
    main()
