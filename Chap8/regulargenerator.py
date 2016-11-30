def generate_multiples(m, n):
    count = 0
    while count < n:
        yield m * count
        count += 1


def main():
    for mult in generate_multiples(3, 6):
        print(mult, end=' ')
    print()


if __name__ == '__main__':
    main()
