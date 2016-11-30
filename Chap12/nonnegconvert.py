def non_neg_int(n):
    result = int(n)
    if result < 0:
        raise ValueError(result)
    return result


while True:
    x = non_neg_int(input('Please enter a nonnegative integer:'))
    if x == 999:   # Secret number exits loop
        break
    print('You entered', x)
