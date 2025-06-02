"""
Ham An Danh - Lamdba trong Python
lambda arguments: expression
"""

# A lambda function is a small (one line) anonymous function
# that is defined without a name.

# a lambda function that adds 69 to the input argument

codexplore = lambda x, y, z: x + y - z

print(codexplore(10, 5, 5))


"""
Custom sorting using a lambda function as key parameter
"""

coordinate2d = [(6, 9), (9, 6), (-1, 3), (2, 10)]
# default sort by x value
print(sorted(coordinate2d))

# sort by y value
print(sorted(coordinate2d, key=lambda point: point[1]))

number_list = [5, 3, -2, 4, 1, -1, -3, 4, 5]
print(sorted(number_list))
print(sorted(number_list, key=lambda x: abs(x)))

"""
Use lambda for map function
"""
# map(func, seq), transforms each element with the function.
list_keyword = ["codeplore", "welcome", "cac ban"]
print(list(map(lambda x: x.title(), list_keyword)))

# su dung list comprehension
new_list = [keyword.title() for keyword in list_keyword]
print(new_list)

# filter(func, seq), returns all elements for which func evaluates to True.
lst_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"cac so le: {list(filter(lambda x: x % 2 != 0, lst_number))}")

new_list = [x for x in lst_number if x % 2 != 0]
print(f"so le comprehension: {new_list}")


"""
Use lambda for reduce function
"""
# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.
from functools import reduce

sequence = [1, 3, 5, 9, 6, 2, 8]
# print(reduce(lambda a, b: a + b, sequence))
print(f"max number: {reduce(lambda a, b: a if a > b else b, sequence)}")

# done
