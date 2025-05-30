my_string = 'New My world\'s "Hello World"'
print(my_string, type(my_string))

"""
Access character and substring
"""
char = my_string[0]

print(char)

sub_string = my_string[1:5]
print(sub_string)

"""
concatenate two or more string
"""

greeting = "Hell, welcome to "
channel = "Sulley Channel"

sentence = greeting + "My channel" + channel

# join element of a list in to string .join()
my_list = ["How", "are", "you", "doing"]
sentence2 = " * ".join(my_list)
print(sentence2)

"""
ieterating
"""

my_string2 = "Hello xin chao cac ban"

for char in my_string2:
    print(char)

# strip()

print("  I am alone   ".strip())
print("On an island".strip("O"))

# split()
print("but life is good".split())
print("but, very boring".split(","))

# replace
print("Help me".replace("me", "you"))

# %, .format(), f-string

name = "Sulley Nguyen"
my_string3 = "Welcome to %s" % name
print(my_string3)

pi = 3.14355
s = "pi number"
my_string4 = "Variable is %.2f from %s" % (pi, s)
print(my_string4)

age = 24
heigh = 170.5
my_string5 = "I am {} year old; {:.3f} cm".format(age, heigh)
print(my_string5)

my_string6 = f"Pi is {pi:.2f} and my name is {name}; {age} years old"
print(my_string6)

# done
