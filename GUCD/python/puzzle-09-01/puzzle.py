import numpy as np

acc = 0


def recursive(data, length):
    global acc
    acc = acc + data[-1]
    shifted_array = np.roll(data, -1)
    shifted_array[length - 1] = 0
    tutu = shifted_array - data
    #print(tutu[:-1])
    if np.all(tutu[:-1] == 0):
        return acc
    else:
        recursive(tutu[:-1], len(tutu) - 1)


def main():
    old = 0
    tmp = []
    # Parse the file
    tata = np.genfromtxt('input.txt', delimiter=" ", dtype='int64')
    # Store the sample number
    laine = len(tata)
    # Store the sample size
    size = len(tata[0])

    for toto in tata:
        result = recursive(toto, size)
        #print(result)

    print(acc)


if '__main__' == __name__:
    main()
