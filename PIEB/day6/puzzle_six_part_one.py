def compute_distance(time, time_hold):
    speed = 1 * time_hold
    distance = (time - time_hold) * speed
    #print(f"\nHold the button for {time_hold} speed are: {speed}, so distance is: {distance}")
    return distance


def process_nb_way(file_path):
    results = []
    product_of_ways = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()

        times = [int(t) for t in lines[0].split()[1:]]
        distances = [int(d) for d in lines[1].split()[1:]]
        for time, travel_record in zip(times, distances):
            better = 0
            for i in range(0, time + 1):
                travel_distance = compute_distance(time, i)
                if travel_distance > travel_record:
                    better += 1
            results.append((time, better))
            product_of_ways *= better

    return results, product_of_ways

file_path = '../../Repository/AdventOfCode2023/Input/puzzle_6.txt'
results, total_ways = process_nb_way(file_path)

for time, nb_beat_record in results:
    print(f"Pour une course de {time} millisecondes, le nombre de façons de battre le record est : {nb_beat_record}")

print(f"Le produit total des façons de battre les records pour toutes les courses est : {total_ways}")