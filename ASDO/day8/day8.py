import time
import numpy as np

def day8(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0

        # LRLRLR sequence
        LR_seq = lines[0]
        LR_seq = LR_seq.replace('L', '0')
        LR_seq = LR_seq.replace('R', '1')

        # node dict {'ABD': ['AAA', 'BBB']}
        node_dict = {line.split()[0]: [line.split()[2][1:-1], line.split()[3][0:-1]] for line in lines[2:]}

        current_node = 'AAA'
        LR_index = 0

        while(current_node != 'ZZZ'):
            current_node = node_dict[current_node][int(LR_seq[LR_index])]
            LR_index = (LR_index + 1) % len(LR_seq)
            result+=1
        print("Result : " + str(result))


start_time = time.time()
file_path = 'input'
day8(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
