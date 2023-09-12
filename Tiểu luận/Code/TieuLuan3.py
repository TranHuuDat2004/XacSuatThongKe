import statistics

# Dữ liệu số
data = [2, 4, 8, 16, 32]

# Tính trung bình hình học với hàm statistics.geometric_mean()
geometric_mean = statistics.geometric_mean(data)

# In kết quả
print("Geometric Mean:", round(geometric_mean))
