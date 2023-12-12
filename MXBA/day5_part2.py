import os

infile = "data_day5.txt"
# infile = "exemple.txt"


class MyMap:
    def __init__(self, lines_to_process):
        self.conversions = []
        self.reverse_conversions = []

        for line in lines_to_process:
            line = line.strip()
            if line:
                dest, src, number = [int(x) for x in line.split()]
                self.conversions.append([range(src, src + number), dest])  # [source range, dest_start]
                self.reverse_conversions.append([range(dest, dest + number), src])  # [dest range, source_start]

    def convert(self, x):
        # return converted value if found
        for src_range, dest in self.conversions:
            if x in src_range:
                offset = x - src_range.start
                result = dest + offset
                # print(f"{x} in {src_range} with {offset=} + {dest=} => {result}")
                return result

        # else current value
        # print(f"{x} not in range => {x}")
        return x

    def reverse_convert(self, x):
        # return converted value if found
        for dst_range, src in self.reverse_conversions:
            if x in dst_range:
                offset = x - dst_range.start
                result = src + offset
                # print(f"{x} in {dst_range} with {offset=} + {src=} => {result}")
                return result

        # else current value
        # print(f"{x} not in range => {x}")
        return x


def seed_to_location(seed, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map,
                     light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map):
    # print(f"\n{seed=}")
    soil = seed_to_soil_map.convert(seed)
    # print(f"{soil=}")
    fertilizer = soil_to_fertilizer_map.convert(soil)
    # print(f"{fertilizer=}")
    water = fertilizer_to_water_map.convert(fertilizer)
    # print(f"{water=}")
    light = water_to_light_map.convert(water)
    # print(f"{light=}")
    temperature = light_to_temperature_map.convert(light)
    # print(f"{temperature=}")
    humidity = temperature_to_humidity_map.convert(temperature)
    # print(f"{humidity=}")
    location = humidity_to_location_map.convert(humidity)
    # print(f"{location=}")
    return location


def location_to_seed(location, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map,
                     light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map):
    # print(f"\n{location=}")
    humidity = humidity_to_location_map.reverse_convert(location)
    # print(f"{humidity=}")
    temperature = temperature_to_humidity_map.reverse_convert(humidity)
    # print(f"{temperature=}")
    light = light_to_temperature_map.reverse_convert(temperature)
    # print(f"{light=}")
    water = water_to_light_map.reverse_convert(light)
    # print(f"{water=}")
    fertilizer = fertilizer_to_water_map.reverse_convert(water)
    # print(f"{fertilizer=}")
    soil = soil_to_fertilizer_map.reverse_convert(fertilizer)
    # print(f"{soil=}")
    seed = seed_to_soil_map.reverse_convert(soil)
    # print(f"{seed=}")
    return seed


if __name__ == '__main__':

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        # split puzzle input into data and maps
        all_lines = [x.strip() for x in puzzle_input.readlines()]
        current_idx = 0

        def read_until(line_to_find):
            global current_idx

            data = []
            try:
                line = all_lines[current_idx].strip()
                while line_to_find not in line:
                    data.append(line)
                    current_idx += 1
                    line = all_lines[current_idx].strip()
            except Exception:
                pass

            return data

        # SEEDS
        line = all_lines[current_idx]
        seeds_ranges = []
        if "seeds:" in line:
            data = line.split(":")[1].strip()
            seeds = [int(x) for x in data.split()]
            # print(f"{seeds=}")

            # create ranges
            for start, number in zip(seeds[::2], seeds[1::2]):
                seed_range = range(start, start + number)
                # print(f"{start=} {number=} = {seed_range}")
                seeds_ranges.append(seed_range)
            current_idx += 1

        # skip useless lines
        _ = read_until("seed-to-soil map:")

        # SEED-TO-SOIL MAP
        current_idx += 1
        data = read_until("soil-to-fertilizer map:")
        seed_to_soil_map = MyMap(data)

        # SOIL-TO-FERTILIZER MAP
        current_idx += 1
        data = read_until("fertilizer-to-water map:")
        soil_to_fertilizer_map = MyMap(data)

        # FERTILIZER-TO-WATER MAP
        current_idx += 1
        data = read_until("water-to-light map:")
        fertilizer_to_water_map = MyMap(data)

        # WATER-TO-LIGHT MAP
        current_idx += 1
        data = read_until("light-to-temperature map:")
        water_to_light_map = MyMap(data)

        # LIGHT-TO-TEMPERATURE MAP
        current_idx += 1
        data = read_until("temperature-to-humidity map:")
        light_to_temperature_map = MyMap(data)

        # TEMPERATURE-TO-HUMIDITY MAP
        current_idx += 1
        data = read_until("humidity-to-location map:")
        temperature_to_humidity_map = MyMap(data)

        # HUMIDITY-TO-LOCATION MAP
        current_idx += 1
        data = read_until("END OF FILE DUDE")
        humidity_to_location_map = MyMap(data)

        min_location = -1
        # todo = 0

    def in_seed_ranges(seed):
        """check if the given seed is in the list of seeds given in the puzzle_input"""
        for seed_range in seeds_ranges:
            # print(f"{seed} in {seed_range=} ? => {seed in seed_range}")
            if seed in seed_range:
                return True
        return False

    # the end !
    location = 0
    seed = 0
    while not in_seed_ranges(seed):
        location += 1
        seed = location_to_seed(location, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)
        if (seed % 100_000) == 0:
            print(f"{location} -> {seed}")

    min_location = location

    txt = f"\n{min_location=} => {seed=}"
    print(txt)
