import numpy as np

x = np.random.randint(0, 11, 3)

# (a) Xác định giá trị của biến ngẫu nhiên X và lưu trữ trong biến X
X = np.unique(x)

# (b) Tính hàm phân phối xác suất của biến ngẫu nhiên X và lưu trữ trong biến P (kiểu danh sách)
P = []
for value in X:
    probability = np.count_nonzero(x == value) / len(x)
    P.append(probability)

# (c) Tính các tham số đặc trưng của biến ngẫu nhiên X
mean = np.mean(x)  # trung bình
variance = np.var(x)  # phương sai
std_dev = np.std(x)  # độ lệch chuẩn

# Lựa chọn tuỳ chọn: Bạn có thể làm tròn giá trị đến số thập phân nhất định
mean = round(mean, 2)
variance = round(variance, 2)
std_dev = round(std_dev, 2)

print("Biến ngẫu nhiên X:", X)
print("Hàm phân phối xác suất P:", P)
print("Trung bình:", mean)
print("Phương sai:", variance)
print("Độ lệch chuẩn:", std_dev)

