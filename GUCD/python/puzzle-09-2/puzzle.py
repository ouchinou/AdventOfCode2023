import numpy as np

result = []
acc = 0


def recursive(data, length):
    global result
    result.append(data[0])

    # Je shift a gauche l'array et je soustrais (permet de savoir l'intervalle en place)
    shifted_array = np.roll(data, -1)
    shifted_array[length - 1] = 0
    tutu = shifted_array - data

    # Fin de la fonction recursive
    if np.all(tutu[:-1] == 0):
        result.reverse()
        return
    # Tant que j'ai pas que des zeros je m'auto appelle
    else:
        recursive(tutu[:-1], len(tutu) - 1)


def main():
    # Parse the file
    jaquie = np.genfromtxt('input.txt', delimiter=" ", dtype='int64')
    # Store the sample size
    size = len(jaquie[0])

    for michel in jaquie:
        global acc
        result.clear()
        recursive(michel, size)
        for i in range(len(result) - 1):
            result[0] = result[i + 1] - result[0]
        acc += result[0]

    print(acc)


if '__main__' == __name__:
    main()
