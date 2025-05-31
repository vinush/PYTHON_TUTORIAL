str_to_test = "A man, a plan, a canal: Panama"


def isPalidrome(s: str) -> bool:
    if s:
        result = []
        for c in s.lower():
            if c.isalnum():
                result.append(c)
        if result == result[::-1]:
            print(f"{str_to_test} is palidrome")
            return True
        else:
            print("not palidrome")
            return False

    else:
        print("is palidrome")
        return True


status = isPalidrome(str_to_test)
print(status)


# # -*- coding: utf-8 -*-
# def is_palindrome(s: str) -> bool:
#     """
#     Kiểm tra xem một chuỗi có phải là palindrome hay không,
#     sau khi đã loại bỏ các ký tự không phải chữ và số và chuyển thành chữ thường.
#     """
#     if not s:
#         return True  # Chuỗi rỗng được coi là palindrome

#     # Bước 1: Chuẩn bị chuỗi - loại bỏ ký tự đặc biệt, khoảng trắng và chuyển thành chữ thường
#     # Sử dụng isalnum() để chỉ giữ lại chữ cái và số
#     normalized_s = "".join(filter(str.isalnum, s)).lower()

#     # Bước 2: Kiểm tra palindrome
#     # So sánh chuỗi đã chuẩn hóa với phiên bản đảo ngược của nó
#     return normalized_s == normalized_s[::-1]


# # Chuỗi đầu vào để kiểm tra
# str_to_test = "A man, a plan, a canal: Panama"
# # str_to_test = "race a car"
# # str_to_test = "Was it a car or a cat I saw?"
# # str_to_test = "hello"
# # str_to_test = "" # Chuỗi rỗng
# # str_to_test = "Able was I, ere I saw Elba"

# # Gọi hàm và in kết quả
# result = is_palindrome(str_to_test)

# print(f"Chuỗi đầu vào: '{str_to_test}'")
# if result:
#     print("Đây LÀ một palindrome.")
# else:
#     print("Đây KHÔNG PHẢI là một palindrome.")

# # Cho phép người dùng nhập chuỗi từ console để kiểm tra
# print("\n--- Kiểm tra chuỗi tùy chỉnh ---")
# try:
#     user_input = input("Nhập một chuỗi để kiểm tra: ")
#     user_result = is_palindrome(user_input)
#     if user_result:
#         print(f"'{user_input}' LÀ một palindrome.")
#     else:
#         print(f"'{user_input}' KHÔNG PHẢI là một palindrome.")
# except KeyboardInterrupt:
#     print("\nĐã hủy nhập.")
# except Exception as e:
#     print(f"Đã xảy ra lỗi: {e}")
