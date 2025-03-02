from collections import defaultdict

# Dữ liệu đầu vào
data = [
    "name=Alice;age=30;score=85.5",
    "name=Bob;age=25;score=90",
    "name=Alice;age=30;score=92",
    "city=NewYork;name=Eve;age=35;score=88",
    "city=London;name=Alice;age=30;score=85.5"
]

# Phân tích dữ liệu thành dictionary lớn
dict_data = defaultdict(list)

# Tách từng chuỗi trong danh sách
for entry in data:
    pairs = entry.split(';')
    for pair in pairs:
        key, value = pair.split('=')
        # Xử lý kiểu dữ liệu cho value
        if value.isdigit():  # Số nguyên
            value = int(value)
        else:
            try:
                value = float(value)  # Số thực
            except ValueError:
                pass  # Chuỗi ký tự giữ nguyên
        dict_data[key].append(value)

# Tính toán kết quả
result = {}

for key, values in dict_data.items():
    unique_values = set(values)
    unique_count = len(unique_values)

    # Tìm giá trị lớn nhất nếu là số
    max_value = max((v for v in values if isinstance(v, (int, float))), default=None)

    # Tìm độ dài chuỗi lớn nhất nếu là chuỗi
    max_length = max((len(v) for v in values if isinstance(v, str)), default=None)

    result[key] = {
        "unique_count": unique_count,
        "max_value": max_value,
        "max_length": max_length
    }

# In kết quả
print("dict =", dict(dict_data))
print("result =", result)