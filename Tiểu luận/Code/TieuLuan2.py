import statistics

# Dữ liệu số
data = [8.0, 7.8, 10, 8.5]

# Trọng số tương ứng (được tính dựa trên phần trăm)
weights = [0.1, 0.2, 0.2, 0.5]

# Tính điểm trung bình nhanh chóng với hàm statistics.fmean()
weighted_average = statistics.fmean(data, weights)

# In kết quả
print("Điểm trung bình:", weighted_average)
