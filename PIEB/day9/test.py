import time
import numpy as np
from math import gcd

# Function to check if any node in the list does not end with 'Z'
def check_current_nodes(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return True
    return False

# Main function to process the puzzle
def day8(file_path):
    # Open and read the file
    with (open(file_path, 'r') as file):
        lines = file.read().splitlines()
        num_lines = len(lines)  # Number of lines in the file
        result = 0

        # Convert the L/R sequence to 0/1
        LR_seq = lines[0]
        LR_seq = LR_seq.replace('L', '0')
        LR_seq = LR_seq.replace('R', '1')
        print(LR_seq)

        # Create a dictionary of nodes with their corresponding left/right nodes
        node_dict = {line.split()[0]: [line.split()[2][1:-1], line.split()[3][0:-1]] for line in lines[2:]}

        # Find all starting nodes (nodes ending with 'A')
        all_nodes = np.array([line.split()[0] for line in lines[2:]])
        print(all_nodes)
        current_nodes = [node for node in all_nodes if node[2] == 'A']
        print(current_nodes)

        results = []

        # For each starting node, navigate through the map until reaching a node ending with 'Z'
        for i in range(len(current_nodes)):
            tmp_res = 0
            LR_index = 0
            while current_nodes[i][2] != 'Z':
                current_nodes[i] = node_dict[current_nodes[i]][int(LR_seq[LR_index])]
                LR_index = (LR_index + 1) % len(LR_seq)
                tmp_res += 1
            results.append(tmp_res)

        print(f'{results=}')
        # Calculate the least common multiple (LCM) of all results
        # This is based on the observation that once reaching 'Z', the pattern repeats
        lcm = 1
        for i in results:
            lcm = lcm * i // gcd(lcm, i)
            print(lcm)

        print("Result:", lcm)

# Measure the execution time of the script
start_time = time.time()
file_path = '../day8/puzzle_8.txt'
day8(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
