import itertools

URN = {'W1', 'W2', 'B1', 'B2', 'B3', 'R1', 'R2', 'R3', 'R4'}

U3 = list(itertools.combinations(URN, 3))

white1blue1red1 = []
for combo in U3:
    colors = [ball[0] for ball in combo]
    if colors.count('W') == 1 and colors.count('B') == 1 and colors.count('R') == 1:
        white1blue1red1.append(combo)

P = len(white1blue1red1) / len(U3)

print("c/ Các trường hợp 3 quả banh có một quả banh màu trắng, một quả banh màu xanh dương và một quả banh màu đỏ:")
for print_ball in white1blue1red1:
    print(print_ball)

print("d/ Xác suất chọn ngẫu nhiên 3 quả banh có một quả banh màu trắng, một quả banh màu xanh dương và một quả banh màu đỏ:", P)
