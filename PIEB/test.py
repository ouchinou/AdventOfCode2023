def compute_distance(time, time_hold):
    speed = 1 * time_hold
    distance = (time - time_hold) * speed
    return distance

def process_nb_way(file_path):
    results = []
    product_of_ways = 1  # Initialiser le produit à 1
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Supposer que la première ligne contient les temps et la deuxième les distances
        times = [int(t) for t in lines[0].split()[1:]]  # Ignorer le premier mot "Time:"
        distances = [int(d) for d in lines[1].split()[1:]]  # Ignorer le premier mot "Distance:"

        for time, travel_record in zip(times, distances):
            better = 0
            for i in range(0, time + 1):
                travel_distance = compute_distance(time, i)
                if travel_distance > travel_record:
                    better += 1
            results.append((time, better))
            product_of_ways *= better  # Multiplier par le nombre de façons pour chaque course

    return results, product_of_ways

file_path = '../../Repository/AdventOfCode2023/Input/puzzle_6.txt'
results, total_ways = process_nb_way(file_path)

for time, nb_beat_record in results:
    print(f"Pour une course de {time} millisecondes, le nombre de façons de battre le record est : {nb_beat_record}")

print(f"Le produit total des façons de battre les records pour toutes les courses est : {total_ways}")
