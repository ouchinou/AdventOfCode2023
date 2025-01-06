import time

def calculate_differences(numbers):
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]


def extrapolate_new_value(sequences):
    # Calculer la nouvelle valeur à ajouter à la fin
    last_non_constant_sequence = sequences[-2]
    new_value_end = last_non_constant_sequence[-1] * 2 - last_non_constant_sequence[-2]
    last_non_constant_sequence.append(new_value_end)

    # Calculer la valeur qui précède la première valeur de la séquence
    first_non_constant_sequence = sequences[-2]
    new_value_start = first_non_constant_sequence[0] * 2 - first_non_constant_sequence[1]

    # Reconstruire les séquences avec les nouvelles valeurs
    for i in range(len(sequences) - 3, -1, -1):
        # Ajouter la nouvelle valeur à la fin
        new_value_end = sequences[i][-1] + sequences[i + 1][-1]
        sequences[i].append(new_value_end)

        # Ajouter la nouvelle valeur au début
        new_value_start = sequences[i][0] - sequences[i + 1][0]
        sequences[i].insert(0, new_value_start)

    return sequences

def extrapolated_value(line):
    numbers = [int(x) for x in line.split()]
    sequences = [numbers]

    while sequences[-1]:
        new_diffs = calculate_differences(sequences[-1])
        sequences.append(new_diffs)
        if all(diff == 0 for diff in new_diffs):
            break

    if len(sequences) > 1 and all(diff == 0 for diff in sequences[-1]):
        extrapolated_sequence = extrapolate_new_value(sequences)
        historical_value = extrapolated_sequence[0][0]  # Get the last element of the original sequence
        return historical_value

    return None

def Mirage_Maintenance(file_path):
    extrapolation_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            result = extrapolated_value(line.strip())
            if result is not None:
                extrapolation_sum += result
    return extrapolation_sum

start = time.time()
#file_path = '../test.txt'
file_path = 'puzzle_9.txt'
extrapolation_sum = Mirage_Maintenance(file_path)
print(f"La somme des extrapolations est : {extrapolation_sum}")

end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
