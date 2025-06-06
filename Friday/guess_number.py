import random

number = random.randint(1, 10)

count = 0
guess = 0

while guess != number:
    guess = int(input("please input your number (1-10)"))
    count += 1
    if guess < number:
        print("ban doan nho hon")
    elif guess > number:
        print("ban doan lon hon")
    else:
        print(f"ban doan dung so la {guess} sau {count} lan doan")
