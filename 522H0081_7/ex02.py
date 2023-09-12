import random

# a/ Cả ba viên cùng màu
def calculate_probability_a(n):
    count = 0      
    
    for _ in range(n):
        urn = ['green', 'green', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white']
        selected_balls = random.sample(urn, 3)  # Lấy ngẫu nhiên 3 viên bi từ trong bình
        
        if len(set(selected_balls)) == 1: # Đây là hàm kiểm tra số màu, =1 chỉ có 1 màu
            count += 1
    
    probability = count / n
    return probability

# b/ Cả ba viên khác màu
def calculate_probability_b(n):
    count = 0  
    
    for _ in range(n):
        urn = ['green', 'green', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white']
        selected_balls = random.sample(urn, 3)  # Lấy ngẫu nhiên 3 viên bi từ trong bình
        
        if len(set(selected_balls)) == 3: # Đây là hàm kiểm tra số màu, =3 có 3 màu khác nhau
            count += 1
        
    probability = count / n
    return probability

# c/ Chỉ có hai viên cùng màu
def calculate_probability_c(n):
    count = 0  
    
    for _ in range(n):
        urn = ['green', 'green', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white']
        selected_balls = random.sample(urn, 3)  # Lấy ngẫu nhiên 3 viên bi từ trong bình
        
        # Đây là hàm kiểm tra số màu, =2 có 2 màu khác nhau => Chỉ có hai viên cùng màu
        if len(set(selected_balls)) == 2: 
            count += 1
            
    probability = count / n
    return probability

# d/ Được 2 bi đỏ và 1 bi trắng
def calculate_probability_d(n):
    count = 0  
    
    for _ in range(n):
        urn = ['green', 'green', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white']
        selected_balls = random.sample(urn, 3)  # Lấy ngẫu nhiên 3 viên bi từ trong bình
        
        if selected_balls.count('red') == 2 and selected_balls.count('white') == 1:
            count += 1
        
    probability = count / n
    return probability

# e/ Liệt kê các trường hợp 3 bi đều màu trắng.
def enumerate_cases():
    urn = ['green', 'green', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white']
    cases = []
    
    # Duyệt qua tất cả các trường hợp
    for ball1 in urn:
        for ball2 in urn:
            for ball3 in urn:
                if ball1 == 'white' and ball2 == 'white' and ball3 == 'white':
                    case = [ball1, ball2, ball3]
                    cases.append(case)
    
    return cases

cases = enumerate_cases()
print("e/ Liệt kê các trường hợp 3 bi đều màu trắng.")
for case in cases:
    print(case)

n = 1000
print("a/ Cả ba viên cùng màu:", calculate_probability_a(n))
print("b/ Cả ba viên đều khác màu nhau:", calculate_probability_b(n))
print("c/ Chỉ có hai viên cùng màu:", calculate_probability_c(n))
print("d/ Được 2 bi đỏ và 1 bi trắng:", calculate_probability_d(n))

