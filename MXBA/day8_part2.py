# import numpy as np
# from collections import Counter
# import functools
import os
import itertools
import re
from dataclasses import dataclass
from pprint import pprint as pp

infile = "data_day8.txt"
infile = "exemple.txt"


@dataclass()
class Node:
    node_name: str
    left: str
    right: str

    def move(self, direction):
        if direction == "L":
            return self.left
        else:
            return self.right

    def is_start(self):
        return self.node_name[-1] == "A"

    def is_end(self):
        return self.node_name[-1] == "Z"


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # first line: directionx
    directions = lines[0]

    # nodes
    nodes = {}
    for line in lines[2:]:
        match = re.match("(...) = \((...), (...)\)", line)
        node_name, left, right = match.groups()
        node = Node(node_name, left, right)
        nodes[node.node_name] = node
        # print(node)

    # pp(nodes)

    nb_steps = 0
    current_nodes = [x for x in nodes.values() if x.is_start()]
    # print("\nSTART")
    pp(current_nodes)
    direction_it = itertools.cycle(directions)

    while False in [node.is_end() for node in current_nodes]:
        next_dir = next(direction_it)
        current_nodes = [nodes[node.move(next_dir)] for node in current_nodes]
    #     node = nodes[current_node]
    #     new_node = node.move(next_dir)
        nb_steps += 1
        # print(f"\n{next_dir}")
        # pp(current_nodes)
    #     current_node = new_node
        if (nb_steps % 100_000) == 0:
            print(f"=> {nb_steps}")

    print(f"\n{nb_steps=}")
