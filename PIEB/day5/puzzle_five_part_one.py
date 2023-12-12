import time


def parse_map_section(lines):
    mapping = []
    for line in lines:
        dest_start, src_start, length = map(int, line.split())
        mapping.append((src_start, src_start + length, dest_start))
    return mapping

def apply_mapping(number, mappings):
    for src_start, src_end, dest_start in mappings:
        if src_start <= number < src_end:
            return dest_start + (number - src_start)
    return number

def process_almanac(file_path):
    maps = []
    current_map_lines = []
    seeds_info = []
    lowest_location = float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('seeds:'):
                seeds = list(map(int, line.split(":")[1].strip().split()))
            elif line.endswith('map:'):
                if current_map_lines:
                    maps.append(parse_map_section(current_map_lines))
                    current_map_lines = []
            elif line:
                current_map_lines.append(line)

        if current_map_lines:
            maps.append(parse_map_section(current_map_lines))

    map_names = ["Soil", "Fertilizer", "Water", "Light", "Temperature", "Humidity", "Location"]
    for seed in seeds:
        seed_info = {'Seed': seed}
        for map_name, mapping in zip(map_names, maps):
            seed = apply_mapping(seed, mapping)
            seed_info[map_name] = seed
        seeds_info.append(seed_info)
        lowest_location = min(lowest_location, seed_info["Location"])

    return seeds_info, lowest_location


start = time.time()
file_path = '../../Input/puzzle_5.txt'
seeds_info, lowest_location = process_almanac(file_path)

for info in seeds_info:
    print(info)
print(f"\nThe lowest location is: {lowest_location}")
end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")