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
        # print(node)
    # pp(nodes)

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
    # pp(current_nodes)
    direction_it = itertools.cycle(directions)

    while False in [node.is_end for node in current_nodes]:
        next_dir = next(direction_it)
        current_nodes = [node.child(next_dir) for node in current_nodes]
        nb_steps += 1
        if (nb_steps % 100_000) == 0:
            print(f"=> {nb_steps:_}")

    print(f"\n{nb_steps=}")
