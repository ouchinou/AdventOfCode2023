import time
import numpy as np

card_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
nb_card_values = len(card_value)


def sort_hand_same_kind(hand, rank):
    out_hand = np.array([])
    if len(hand) <= 1:
        return hand
    for i in range(max(card_value.values()), min(card_value.values())-1, -1):
        out = sort_hand_same_kind(hand[hand[:, rank] == i], rank+1)
        if len(out) != 0:
            if len(out_hand) > 0:
                out_hand = np.vstack((out_hand, sort_hand_same_kind(hand[hand[:, rank] == i], rank+1)))
            else:
                out_hand = sort_hand_same_kind(hand[hand[:, rank] == i], rank + 1)
    return out_hand


def day7(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        num_lines = len(lines)
        result = 0

        # Create an array that contains all hands:
        # format: weight card 1 | weight card 2 | ... | weight card 5 | bid
        all_hands = np.array([[card_value[card] for card in line.split()[0]] + [int(line.split()[1])] for line in lines])
        all_hands_original = np.array([line.split()[0] for line in lines])

        # array each line is a hand fist element is the second maximum number of same card and second element is the
        # maximum number of same card for ex T55J5 gives | 1 | 3 |
        count_same_card = np.array([np.sort(np.array([hand.count(value) for value in card_value])[np.argpartition(
            np.array([hand.count(value) for value in card_value]), -2)[-2:]]) for hand in all_hands_original])

        # Concat two tables and sort according to max number of same card
        all_hands = np.hstack((all_hands, count_same_card))
        all_hands_sorted = np.zeros((1, np.shape(all_hands)[1]))

        for n_kind in range(5, 0, -1):
            same_kind_hands = all_hands[all_hands[:, -1] == n_kind]
            if n_kind > 3 or n_kind == 1:
                all_hands_sorted = np.vstack((all_hands_sorted, sort_hand_same_kind(same_kind_hands, 0)))
            else:
                # two pairs vs one pair and full vs three of a kind
                all_hands_sorted = np.vstack((all_hands_sorted, sort_hand_same_kind(same_kind_hands[same_kind_hands[:, -2] == 2],0)))
                all_hands_sorted = np.vstack((all_hands_sorted, sort_hand_same_kind(same_kind_hands[same_kind_hands[:, -2] == 1],0)))

        all_hands_sorted = all_hands_sorted[1:, :]
        for i in range(len(all_hands_sorted)):
            result += all_hands_sorted[i][-3]*(len(all_hands_sorted)-i)
        print("Result : " + str(result))


start_time = time.time()
file_path = 'input'
day7(file_path)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
