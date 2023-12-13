# import numpy as np
# from collections import Counter
# import functools
import os
import itertools
import re
import math
from dataclasses import dataclass

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


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # first line: directions
    directions = lines[0]

    # nodes
    print("Read nodes...")
    nodes = {}
    for line in lines[2:]:
        match = re.match("(...) = \((...), (...)\)", line)
        node_name, left, right = match.groups()
        node = Node(node_name, left, right)
        nodes[node.node_name] = node

    # update Nodes with the real child nodes
    print("Update nodes...")
    for node in nodes.values():
        left_node = nodes[node.child("L")]
        right_node = nodes[node.child("R")]
        node.update(left_node, right_node)

    # now, all Node has Nodes as Left and Right children
    nb_steps = 0
    current_nodes = [x for x in nodes.values() if x.is_start]
    print("\nSTART")

    # look for the number of steps that are necessary to reach the END
    lcm = []
    for node in current_nodes:
        direction_it = itertools.cycle(directions)
        nb_steps = 0
        while not node.is_end:
            node = node.child(next(direction_it))
            nb_steps += 1

        node.necessary_steps_number = nb_steps
        lcm.append(nb_steps)
        print(f"{node.node_name} => {node.necessary_steps_number}")

    # find Lowes Common Multiple of all starting nodes
    print(math.lcm(*lcm))
