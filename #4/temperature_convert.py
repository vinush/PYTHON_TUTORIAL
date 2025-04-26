def cToFConverter():
    while True:
        cTemp = input("Enter the temperature in Celsius: ")

        if cTemp:
            cTemp = float(cTemp)
            fahrenheit = round((cTemp * 9 / 5) + 32, 1)
            print(f"{cTemp} Celsius is equal to {fahrenheit} Fahrenheit")

            break
        else:
            print("Input is not a number")
            continue


def main():
    cToFConverter()


if __name__ == "__main__":
    main()
