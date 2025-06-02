# LOOP: For & While

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {"a": 1, "b": 2, "c": 3}

for num in my_list:
    print(num)

for k, v in my_dict.items():
    print(k, v)

for tup in my_tuple:
    print(tup)

# while <condition that evaluates to boolean>:
#   # action
#   if <condition that evaluates to boolean>:
#     break # break out of while loop
#   if <condition that evaluates to boolean>:
#     continue #continue to the next line in the block

msg = ""

while msg != "quit":
    msg = input("please give me an input: ")
    print(msg)
