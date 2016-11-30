def make_adder():
    loc_val = 2   # Local variable definition
    return lambda x: x + loc_val   # Returns a function

 
def main():
    f = make_adder()
    print(f(10))
    print(f(2))


main()
