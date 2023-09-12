import docx
import re
import matplotlib.pyplot as plt
from collections import Counter

# Đọc nội dung từ tập tin "Ex03.docx"
doc = docx.Document("ex04.docx")
full_text = ""
for para in doc.paragraphs:
    full_text += para.text + " "

# Xử lý và tách từ văn bản
words = re.findall(r'\b\w+\b', full_text.lower())

# Đếm tần suất xuất hiện của từng từ
word_frequency = Counter(words)

# Chọn ra 30 từ phổ biến nhất
most_common_words = word_frequency.most_common(30)

# Tạo danh sách các từ và số lần xuất hiện để vẽ biểu đồ
common_words = [word[0] for word in most_common_words]
frequencies = [word[1] for word in most_common_words]

# Vẽ biểu đồ đường
plt.figure(figsize=(12, 6))
plt.plot(common_words, frequencies)
plt.xlabel("Từ")
plt.ylabel("Số lẩn xuất hiện")
plt.title("30 từ xuất hiện phổ biến trong file: Lời cảm ơn")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
