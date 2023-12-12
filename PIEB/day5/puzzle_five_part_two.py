class BaseMapping:
    def __init__(self):
        self.ranges = []

    def add_range(self, src_start, length, dest_start):
        self.ranges.append((dest_start, src_start, length))

    def get_source_for_destination(self, destination):
        for dest_start, src_start, length in self.ranges:
            if dest_start <= destination < dest_start + length:
                delta = destination - dest_start
                return src_start + delta
        return destination

    def display(self):
        for dest_start, src_start, length in self.ranges:
            print(f"Destination: {dest_start}-{dest_start + length - 1}, Source: {src_start}-{src_start + length - 1}")


def create_mapping_class(name):
    class_name = ''.join(word.capitalize() for word in name.split('-'))
    return type(name, (BaseMapping,), {})


def parse_map_section(lines, mapping):
    for line in lines:
        dest_start, src_start, length = map(int, line.split())
        mapping.add_range(src_start, length, dest_start)


def is_seed_in_range(seed, seed_ranges):
    for start, length in seed_ranges:
        if start <= seed < start + length:
            return True
    return False


def process_almanac(file_path):
    mappings = {}
    current_map = None
    seed_ranges = []
    mapping_order = [
        'Humidity2location',
        'Temperature2humidity',
        'Light2temperature',
        'Water2light',
        'Fertilizer2water',
        'Soil2fertilizer',
        'Seed2soil'
    ]

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('seeds:'):
                seed_values = line.split(":")[1].strip().split()
                seed_ranges = [(int(seed_values[i]), int(seed_values[i + 1])) for i in range(0, len(seed_values), 2)]
                print(seed_ranges)
            elif 'map:' in line:
                if current_map is not None:
                    mappings[current_map_name] = current_map
                current_map_name = line.split(':')[0].replace('-to-', '2').replace(' map', '').capitalize()
                current_map = create_mapping_class(current_map_name)()
            elif line and current_map is not None:
                parse_map_section([line], current_map)

        if current_map is not None:
            mappings[current_map_name] = current_map

    min_location = 0
    for location in range(min_location, 1000000000):
        original_seed = location
        for map_name in mapping_order:
            original_seed = mappings[map_name].get_source_for_destination(original_seed)
        if is_seed_in_range(original_seed, seed_ranges):
            return location
    return None


file_path = '../../Repository/AdventOfCode2023/Input/puzzle_5.txt'
lowest_location = process_almanac(file_path)
print(f"The lowest location is: {lowest_location}")
