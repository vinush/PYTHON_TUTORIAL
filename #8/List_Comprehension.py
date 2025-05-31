"""
Topic #7: List trong Python - một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ
liệu khác nhau trong nó, và chũng ta có thể truy xuất đến các phần tử bên trong
nó thông qua vị trí của phần tử đó trong list

Ngôn Ngữ Khác: C/C++, Java, List trong Python = Mảng (Array)

"""

word = "Hello world"

print([char for char in word])

even_number = [i for i in range(0, 10) if i % 2 == 0]

print(even_number)

transaction = [100, 200, 300, 150, 80]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07


def get_price_tax_service(bill):
    return bill * (1 + TAX_RATE + SERVICE_CHARGE)


final_price = [get_price_tax_service(bill) for bill in transaction]
print(final_price)

# Advance function

# list() --> convert string => list
my_string = "Welcome to my channel"
list_of_chars = list(my_string)
print(list_of_chars)

# sum()
print(f"sum is: {sum([1, 2, 3, 4, 5, 7, 7])}")

# zip() looping through two list simultaneously
wizards = ["Harry Porter", "RON", "Hermione"]

pets = ["Hedwig", "Scabber", "Crookshank"]

for wiz, pet in zip(wizards, pets):
    print(f"{wiz} has {pet}")

for index, (wiz, pet) in enumerate(zip(wizards, pets)):
    print(f"{index + 1}. {wiz} has {pet}")

# sorted()

sorted_by_first = sorted(
    ["hi", "hello", "you", "codeExplore"],
)
print(sorted_by_first)


sorted_by_second = sorted(["hi", "hello", "you", "codeExplore"], key=lambda el: el[1])
print(sorted_by_second)

sorted_by_key = sorted(
    [
        {"name": "codeExplore", "age": 18},
        {"name": "Andy", "age": 70},
        {"name": "zoey", "age": 55},
    ],
    key=lambda el: el["age"],
    reverse=True,
)

print(sorted_by_key)

"""
5. 2D Array/List = Matrix: Mảng 2 Chiều
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1][2])

for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])
# Transform Matrix in list
list_converted = [
    matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))
]
print(list_converted)

# combine colums with zip and *:
print([x for x in zip(*matrix)])
