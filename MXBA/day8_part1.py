# import numpy as np
# from collections import Counter
# import functools
import os
import itertools
import re
from dataclasses import dataclass
from pprint import pprint as pp

infile = "data_day8.txt"
# infile = "exemple.txt"


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

    pp(nodes)

    nb_steps = 0
    current_node = "AAA"
    direction_it = itertools.cycle(directions)

    while current_node != "ZZZ":
        node = nodes[current_node]
        next_dir = next(direction_it)
        new_node = node.move(next_dir)
        # print(f"{node} : {next_dir} => {new_node}")
        current_node = new_node
        nb_steps += 1

    print(f"\n{nb_steps=}")
