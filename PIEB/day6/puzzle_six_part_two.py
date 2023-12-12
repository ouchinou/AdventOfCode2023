def compute_distance(time, time_hold):
    speed = 1 * time_hold
    distance = (time - time_hold) * speed
    #print(f"\nHold the button for {time_hold} speed are: {speed}, so distance is: {distance}")
    return distance


def process_nb_way(file_path):
    product_of_ways = 1
    with open(file_path, 'r') as file:
        lines = file.readlines()

        times = [int(t) for t in lines[0].split()[1:]]
        times_str = ''.join(map(str, times))  # Convertit chaque entier en chaîne et les concatène sans espace
        times = int(times_str)
        print(times)

        distances = [int(d) for d in lines[1].split()[1:]]
        distances_str = ''.join(map(str, distances))  # Convertit chaque entier en chaîne et les concatène sans espace
        distances = int(distances_str)
        print(distances)
        better = 0
        for i in range(0, times + 1):
            travel_distance = compute_distance(times, i)
            if travel_distance > distances:
                better += 1
        product_of_ways *= better

    return  product_of_ways

file_path = '../../Repository/AdventOfCode2023/Input/puzzle_6.txt'
total_ways = process_nb_way(file_path)

print(f"Le total de possibilités des façons de battre les records pour la courses est : {total_ways}")