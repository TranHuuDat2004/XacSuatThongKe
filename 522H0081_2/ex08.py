import math

# Define the number of balls in each color
white_balls = 8
blue_balls = 6
red_balls = 9

# Define the total number of balls
total_balls = white_balls + blue_balls + red_balls

# Define the number of balls to be selected
selected_balls = 6

# Calculate the probability
probability = (math.comb(white_balls, 2) * math.comb(blue_balls, 2) * math.comb(red_balls, 2)) / math.comb(total_balls, selected_balls) # tinh to hop

print("Xác suất lấy được hai quả mỗi loại là:", round(probability, 5))
