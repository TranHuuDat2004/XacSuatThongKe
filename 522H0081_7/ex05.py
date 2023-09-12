import random
suits = ["♠", "♣", "♦", "♥"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def check_straight_flush(hand):
    suits = set(card[1] for card in hand)
    if len(suits) == 1:
        ranks = sorted([int(card[0]) if card[0].isdigit() else 10 if card[0] == "T" else 11 if card[0] == "J" else 12 if card[0] == "Q" else 13 for card in hand])
        if max(ranks) - min(ranks) == 4:
            return True
    return False

def calculate_theoretical_probability():
    total_straight_flushes = 40  # Số sảnh có thể tạo thành
    total_possible_hands = 52 * 51 * 50 * 49 * 48 // (5 * 4 * 3 * 2 * 1)  # Tổng số cách chọn ngẫu nhiên 5 lá bài
    theoretical_probability = total_straight_flushes / total_possible_hands
    return theoretical_probability

def calculate_practical_probability(num_trials):
    count_straight_flushes = 0
    for _ in range(num_trials):
        deck = [rank + suit for rank in ranks for suit in suits]
        hand = random.sample(deck, 5)
        if check_straight_flush(hand):
            count_straight_flushes += 1
    practical_probability = count_straight_flushes / num_trials
    return practical_probability

# Tính xác suất lý thuyết
theoretical_prob = calculate_theoretical_probability()
print("a/ Xác suất lý thuyết (theoretical probability):", theoretical_prob)

# Tính xác suất thực nghiệm
num_trials = 1000000  # Số lần thí nghiệm
practical_prob = calculate_practical_probability(num_trials)
print("b/ Xác suất thực nghiệm (practical probability):", practical_prob)
