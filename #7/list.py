"""
Topic #7: List mot dang du lieu cho phep luu tru nhieu kieu du lieu khac nhau
trong no,va chung ta cung co the truy xuat den phan tuy ben trong thong qua
vi tri cua no trong list

List trong python = mang (Array)
"""

"""
1. creating list
"""
list_1 = ["banana", "cherry", "apple"]
list_2 = [5, "code exlore", False, None]

print(list_2)

"""
2. access elements: truy cap den gia tri trong list
"""
my_list = [1, 2, 3, 3, 3, "3", "3", True]

print(my_list[0])
print(my_list.index("3"))
print(my_list.count(3))

# python built in enumerate function
president = [
    "washington",
    "Adams",
    "Jefferson",
    "Madison",
    "Monnoe",
    "Adams",
    "Jackson",
]

for index, president in enumerate(president, start=1):
    print(f"president #{index}: {president}")

# slicing
# is called slicing and
# has the format [start : end : step]

my_list2 = [1, 2, "3", True]

print(my_list2[::-1])

"""
3. List operations & useful methods

3.1 add to list
"""
print(my_list2 + [100, "code explore"])
print(my_list2.append(100))
print(my_list2)
print(my_list2.extend([100, "code explore"]))
print(my_list2)

print(my_list2.insert(3, 4))
print(my_list2)

"""
3.2 remove from list
"""
print(my_list2.pop())
print(my_list2)

print(my_list2.pop(1))
print(my_list2)

my_list2.remove(1)
print(my_list2)

del my_list2[2]
print(my_list2)

"""
3.3 sorting
"""
my_list3 = [1, 2, 8, 4, 5, 7]
my_list3.sort(reverse=True)
print(my_list3)

my_list3.reverse()
print(my_list3)

"""
3.4 usefull operation
"""
my_list4 = [1, 2, 8, 4, 5, 7]
print(sum(my_list4))
