# Required Parameter & Default Parameter
def print_name(name, greeting="Welcome Cac Ban"):
    print(f"{name}, {greeting} ")


def codexplore(a, b, c):
    print(a, b, c)


# Variable-length parameters (*args and **kwargs)


# If you mark a parameter with one asterisk (*),
# you can pass any number of positional arguments to your function (Typically called *args)
# If you mark a parameter with two asterisks (**),
# you can pass any number of keyword arguments to this function (Typically called **kwargs).
def variableLengthArgExample(a, b, *args, **initkwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key, value in initkwargs.items():
        print(key, value)


def main():
    print_name("Sulley", "Welcome to my Channel")

    # positional Arguments
    codexplore(1, 2, 3)

    # KEYWORD argument
    codexplore(a="hello", c="you", b="to")

    # *args:
    # variableLengthArgExample("a", "b", "Hello world", 1, 2, 3)

    # **kwargs
    variableLengthArgExample("a", 2, "Helloword", 1, size="up size", age="NG")


if __name__ == "__main__":
    main()
