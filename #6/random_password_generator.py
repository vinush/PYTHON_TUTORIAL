"""
project: random password generator

password: adbXYZ-69-96
"""

import random
import string

LETTER = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


# print PUNCTUATION
def password_generator(length=8):
    printable = f"{LETTER}{NUMBERS}{PUNCTUATION}"

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = "".join(random_password)
    return random_password


def get_password_length():
    pwd_length = int(input("How long do you want your password: "))
    return pwd_length


def main():
    pwd_length = get_password_length()
    password = password_generator(pwd_length)
    print(password)


if __name__ == "__main__":
    main()
