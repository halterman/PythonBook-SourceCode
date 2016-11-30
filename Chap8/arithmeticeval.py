def add(x, y):
    """
    Adds the parameters x and y and returns the result
    """
    return x + y


def multiply(x, y):
    """
    Multiplies the parameters x and y and returns the result
    """
    return x * y


def evaluate(f, x, y):
    """
    Calls the function f with parameters x and y:
    f(x, y)
    """
    return f(x, y)


def main():
    """
    Tests the add, multiply, and evaluate functions
    """
    print(add(2, 3))
    print(multiply(2, 3))
    print(evaluate(add, 2, 3))
    print(evaluate(multiply, 2, 3))


main()  # Call main
