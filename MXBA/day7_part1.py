# import alive_progress
# import numpy as np
from collections import Counter
import os
import functools

infile = "data_day7.txt"
# infile = "exemple.txt"

CARDS_STRENGTH = [x for x in "AKQJT98765432"]

HAND_VALUES = {"Five of a kind": 6,
               "Four of a kind": 5,
               "Full house": 4,
               "Three of a kind": 3,
               "Two pair": 2,
               "One pair": 1,
               "High card": 0
               }
HAND_TYPES = {v: k for k, v in HAND_VALUES.items()}


@functools.total_ordering
class Hand:
    def __init__(self, line):
        line = line.strip().split()

        self.cards = [x for x in line[0]]
        self.ordered_cards = list(sorted([x for x in line[0]]))
        self.bid = int(line[1])

        # compute type
        tmp = Counter(self.cards)

        counts = list(tmp.values())
        if max(counts) == 5:
            self.hand_type = "Five of a kind"
        elif max(counts) == 4:
            self.hand_type = "Four of a kind"
        elif max(counts) == 3:
            # FULL ? THREE of a kind ???
            if sorted(counts) == [2, 3]:
                self.hand_type = "Full house"
            else:
                self.hand_type = "Three of a kind"
        elif max(counts) == 2:
            # one or two pairs
            nb_pairs = counts.count(2)
            if nb_pairs == 2:
                self.hand_type = "Two pair"
            else:
                self.hand_type = "One pair"
        else:
            self.hand_type = "High card"

    def __str__(self):
        return f"'{''.join(self.cards)}' - {self.bid} ({self.hand_type})"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        # compare hand type value
        me = HAND_VALUES[self.hand_type]
        you = HAND_VALUES[other.hand_type]

        if me < you:
            # print(f"LT {self=} < {other=} : {me} < {you}")
            return True
        if me > you:
            # print(f"LT {self=} > {other=} : {me} > {you}")
            return False

        # same type : compare cards strength IN THE ORDER OF CARDS !
        for my_card, your_card in zip(self.cards, other.cards):
            # warning : order is inverted in the CONSTANT (higert card at lower index)
            if CARDS_STRENGTH.index(my_card) > CARDS_STRENGTH.index(your_card):
                # print(f"LT {self=} < {other=} : {CARDS_STRENGTH.index(my_card)} < {CARDS_STRENGTH.index(your_card)}")
                return True
            elif CARDS_STRENGTH.index(my_card) < CARDS_STRENGTH.index(your_card):
                # print(f"LT {self=} > {other=} : {CARDS_STRENGTH.index(my_card)} > {CARDS_STRENGTH.index(your_card)}")
                return False

        # same hand
        return False

    def __eq__(self, other):

        if HAND_VALUES[self.hand_type] != HAND_VALUES[other.hand_type]:
            # print(f"EQ {self=} != {other=}")
            return False

        # same cards ?
        if self.ordered_cards == other.ordered_cards:
            # print(f"EQ {self=} == {other=}")
            return True
        else:
            return False


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), infile), "r") as puzzle_input, open("results.txt", "w") as out:

    # split puzzle input into data and maps
    lines = [x.strip() for x in puzzle_input.readlines()]

    # create hads of cards
    hands = [Hand(x) for x in lines]
    for h in hands:
        print(h)

    print("*" * 20)
    sorted_hands = sorted(hands)
    for h in sorted_hands:
        print(h)
        # print(h, file=out)

    total = 0
    # compute total winnigs : sum(bid*rank)
    for rank, hand in enumerate(sorted_hands):
        value = (rank + 1) * hand.bid
        print(f"{value=}")
        print(f"RANK {rank + 1:4d} : {hand} -> {rank + 1} * {hand.bid} = {value}", file=out)
        total += value

    print(f"\n{total=}")
