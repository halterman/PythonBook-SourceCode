#  Computes the greatest common divisor of m and n
def gcd(m, n):
    # Determine the smaller of m and n
    min = m if m < n else n
    # 1 is definitely a common factor to all ints
    largest_factor = 1  
    for i in range(1, min + 1):
        if m % i == 0 and n % i == 0:
            largest_factor = i   # Found larger factor
    return largest_factor


#  Get an integer from the user
def get_int():
    return int(input("Please enter an integer: "))


#  Main code to execute
def main():
    n1 = get_int()
    n2 = get_int()
    print("gcd(", n1, ",",  n2, ") = ", gcd(n1, n2), sep="")


# Run the program
main()
