# import numpy as np
# from collections import Counter
# import functools
import os
import itertools
import re
from pprint import pprint as pp
from dataclasses import dataclass
import multiprocessing as mp


infile = "data_day8.txt"
# infile = "exemple.txt"


@dataclass()
class Node:
    node_name: str
    left: str
    right: str

    def __post_init__(self):
        self.is_start = self.node_name[-1] == "A"
        self.is_end = self.node_name[-1] == "Z"

    def child(self, direction):
        if direction == "L":
            return self.left
        else:
            return self.right

    def update(self, left_node, right_node):
        self.left = left_node
        self.right = right_node


def find_end(task_number, starting_node, directions, queue):
    current_node = starting_node
    direction_it = itertools.cycle(directions)
    idx = 1
    while True:
        current_node = current_node.child(next(direction_it))
        if current_node.is_end:
            # print(f"Task_{task_number} => {idx}")
            # next "end" found: return the number of steps executed
            queue.put(idx)  # , block=True, timeout=None)
        idx += 1


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

        # split puzzle input into data and maps
        lines = [x.strip() for x in puzzle_input.readlines()]

        # first line: directionx
        directions = lines[0]

        # nodes
        print("Read nodes...")
        nodes = {}
        for line in lines[2:]:
            match = re.match("(...) = \((...), (...)\)", line)
            node_name, left, right = match.groups()
            node = Node(node_name, left, right)
            nodes[node.node_name] = node
            # print(node)
        # pp(nodes)

        # update Nodes with the real child nodes
        print("Update nodes...")
        for node in nodes.values():
            left_node = nodes[node.child("L")]
            right_node = nodes[node.child("R")]
            node.update(left_node, right_node)

        # nb_steps = 0
        current_nodes = [x for x in nodes.values() if x.is_start]
        queues = []
        tasks = []
        for idx, n in enumerate(current_nodes):
            q = mp.Queue(maxsize=3)
            p = mp.Process(target=find_end, args=(idx, n, directions, q,))
            p.start()
            queues.append(q)
            tasks.append(p)

        print("\nSTART")
        # all tasks are running and looking for the "next potential end node"
        end_steps = [q.get(block=True) for q in queues]
        step_max = max(end_steps)
        step_min = min(end_steps)
        found = (step_min == step_max)
        mx = 100_000

        while not found:
            # print(end_steps)
            # print(f"=> {step_max=}")
            for idx, i in enumerate(end_steps):
                if i != step_max:
                    end_steps[idx] = queues[idx].get(block=True)

            step_max = max(end_steps)
            step_min = min(end_steps)
            found = (step_min == step_max)
            # print(f"{min(end_steps)=}")
            # print(f"{max(end_steps)=}")
            # print(f"{found=}")

            if step_max >= mx:
                print(f"=> {step_max=:_}")
                mx += 1_000_000

        # STOP
        print(f"=> {step_max=:_}")
        print("\nSTOP")
        for task in tasks:
            task.kill()
