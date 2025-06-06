# Tuple các màu sắc
mau_sac = ("đỏ", "xanh lá", "xanh dương", "vàng")

print("Các màu sắc trong tuple:")
for mau in mau_sac:
    print(mau)

# Tuple các số
so_nguyen = (10, 20, 30, 40, 50)
tong = 0
for so in so_nguyen:
    tong += so
print(f"\nTổng các số trong tuple: {tong}")

# Lặp qua tuple chứa các tuple khác (unpacking)
toa_do = ((1, 2), (3, 4), (5, 6))
print("\nCác tọa độ (x, y):")
for x, y in toa_do:  # Unpacking trực tiếp các phần tử của tuple con
    print(f"x = {x}, y = {y}")


# Các cấu hình cho ứng dụng
DATABASE_CONFIG = ("localhost", "mydatabase", "user123", "password123")
# (host, db_name, username, password)

API_ENDPOINTS = (
    "https://api.example.com/users",
    "https://api.example.com/products",
    "https://api.example.com/orders",
)

DEFAULT_WINDOW_SIZE = (800, 600)  # (width, height)

# Sử dụng trong code
db_host, db_name, _, _ = DATABASE_CONFIG  # Lấy giá trị cụ thể nếu cần
print(f"Kết nối tới database host: {db_host} với database name là {db_name}")

if API_ENDPOINTS[0].startswith("https://"):
    print("Sử dụng kết nối an toàn cho API người dùng.")

# Các phép toán tập hợp
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print("-" * 30)

"""
union - phép hợp
"""
# Sử dụng toán tử |
hop_toan_tu = set_A | set_B
print(f"Hợp (dùng toán tử |): {hop_toan_tu}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Sử dụng phương thức .union()
hop_phuong_thuc = set_A.union(set_B)
print(
    f"Hợp (dùng phương thức .union()): {hop_phuong_thuc}"
)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# .union() có thể nhận nhiều đối số là các set khác
set_C = {8, 9, 10}
hop_nhieu_set = set_A.union(set_B, set_C)
print(f"Hợp của A, B, và C: {hop_nhieu_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("-" * 30)

"""
intersection - phép giao
"""
# Sử dụng toán tử &
giao_toan_tu = set_A & set_B
print(f"Giao (dùng toán tử &): {giao_toan_tu}")  # Output: {4, 5}

# Sử dụng phương thức .intersection()
giao_phuong_thuc = set_A.intersection(set_B)
print(f"Giao (dùng phương thức .intersection()): {giao_phuong_thuc}")  # Output: {4, 5}

# .intersection() cũng có thể nhận nhiều đối số
# set_C đã được định nghĩa ở trên: {8, 9, 10}
set_D = {4, 5, 8}
giao_nhieu_set = set_A.intersection(set_B, set_D)  # sẽ là {4, 5}
print(f"Giao của A, B, và D: {giao_nhieu_set}")

print("-" * 30)
"""
different - phép hiệu
"""
# Hiệu của set_A và set_B (A - B)
hieu_A_tru_B_toan_tu = set_A - set_B
print(f"Hiệu A - B (dùng toán tử -): {hieu_A_tru_B_toan_tu}")  # Output: {1, 2, 3}

hieu_A_tru_B_phuong_thuc = set_A.difference(set_B)
print(
    f"Hiệu A - B (dùng .difference()): {hieu_A_tru_B_phuong_thuc}"
)  # Output: {1, 2, 3}

# Hiệu của set_B và set_A (B - A)
hieu_B_tru_A_toan_tu = set_B - set_A
print(
    f"Hiệu B - A (dùng toán tử -): {hieu_B_tru_A_toan_tu}"
)  # Output: {8, 6, 7} (thứ tự có thể khác)

hieu_B_tru_A_phuong_thuc = set_B.difference(set_A)
print(
    f"Hiệu B - A (dùng .difference()): {hieu_B_tru_A_phuong_thuc}"
)  # Output: {8, 6, 7}
