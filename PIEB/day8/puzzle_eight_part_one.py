import time


def navigate(instructions, map, start):
    current_position = start
    i = 0
    step_count = 0
    #print(instructions,map,start)
    while current_position != 'ZZZ':
        direction = instructions[i % len(instructions)]
        #print(direction)
        if direction == 'L':
            current_position = map[current_position]['left']
            #print(current_position)
        elif direction == 'R':
            current_position = map[current_position]['right']
            #print(current_position)
        i += 1
        step_count += 1

    return step_count


def Haunted_Wasteland(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    result = 0

    instructions = list(lines[0].strip())
    print(f'{instructions =}')
    map = {}

    for line in lines[2:]:
        #print(line)
        node, destinations = [part.strip() for part in line.split('=')]
        left, right = [part.strip() for part in destinations.strip('()').split(',')]
        map[node] = {'left': left, 'right': right}
        #print(f'{map=}')

    result = navigate(instructions, map, 'AAA')

    return result


start = time.time()
#file_path = '../test.txt'
file_path = 'puzzle_8.txt'
total_steps = Haunted_Wasteland(file_path)
print(f"Le total_winnings est : {total_steps}")

end = time.time()
elapsed = end - start
print(f"Time elapsed: {elapsed} seconds")
