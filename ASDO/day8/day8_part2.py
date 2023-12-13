import time
import numpy as np
from math import gcd


def check_current_nodes(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return True
    return False


def day8(file_path):
    with (open(file_path, 'r') as file):
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0

        # LRLRLR sequence
        LR_seq = lines[0]
        LR_seq = LR_seq.replace('L', '0')
        LR_seq = LR_seq.replace('R', '1')

        # node dict {'ABD': ['AAA', 'BBB']}
        node_dict = {line.split()[0]: [line.split()[2][1:-1], line.split()[3][0:-1]] for line in lines[2:]}

        # Find starting nodes
        all_nodes = np.array([line.split()[0] for line in lines[2:]])
        current_nodes = []
        for node in all_nodes:
            if node[2] == 'A':
                current_nodes = current_nodes + [node]

        results = []

        for i in range(len(current_nodes)):
            tmp_res = 0
            LR_index = 0
            while (current_nodes[i][2] != 'Z'):
                current_nodes[i] = node_dict[current_nodes[i]][int(LR_seq[LR_index])]
                LR_index = (LR_index + 1) % len(LR_seq)
                tmp_res += 1
            results = results + [tmp_res]

        # Find common multiplier as it seems that once we reach Z dest we just loop apparently (empirical observation)
        lcm = 1
        for i in results:
            lcm = lcm * i // gcd(lcm, i)

        print("Result : " + str(lcm))


start_time = time.time()
file_path = 'input'
day8(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
