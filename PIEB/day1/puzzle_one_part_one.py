def extract_calibration_values_from_file(file_path):
    values = []
    with open(file_path, 'r') as file:
        for line in file:
            # Trouver tous les chiffres dans la ligne actuelle
            digits = [int(d) for d in line if d.isdigit()]

            if digits:
                # Combiner le premier et le dernier chiffre
                value = int(f"{digits[0]}{digits[-1]}")
                values.append(value)
    print(values)
    return values


def somme_des_elements(liste):
    return sum(liste)


# Utilisation de l'exemple
file_path = '../../Repository/AdventOfCode2023/Input/puzzle_two.txt'
print(extract_calibration_values_from_file(file_path))
all_sum = sum(extract_calibration_values_from_file(file_path))
print(all_sum)
