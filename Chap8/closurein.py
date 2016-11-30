def evaluate(f, x, y):     
    return f(x, y)


def main():
    a = int(input('Enter an integer:'))
    print(evaluate(lambda x, y: False if x == a else True, 2, 3))


main()
