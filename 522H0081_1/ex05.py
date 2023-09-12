import itertools

suits = ["♠", "♣", "♦", "♥"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Generate all possible 5-card poker hands
poker_5 = list(itertools.combinations(itertools.product(ranks, suits), 5))
len_poker_5 = len(poker_5)

# Find "three of a kind" hands
three_of_a_kind = []
for hand in poker_5:
    rank_counts = {}
    for card in hand:
        rank = card[0]
        if rank not in rank_counts:
            rank_counts[rank] = 1
        else:
            rank_counts[rank] += 1
    if 3 in rank_counts.values() and len(rank_counts) == 3:
        three_of_a_kind.append(hand)

len_three_of_a_kind = len(three_of_a_kind)

print("List of all possible 5-card poker hands:")
for hand in poker_5:
    print(hand)

print("\nNumber of 5-card poker hands:", len_poker_5)
# Number of 5-card poker hands: 2598960

print("\nNumber of 'three of a kind' hands:", len_three_of_a_kind)
# Number of 'threae of a kind' hands: 54912