def main():
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    print("Please enter", NUMBER_OF_ENTRIES, " numbers: ")
    for i in range(0, NUMBER_OF_ENTRIES):
        num = float(input("Enter number " + str(i) + ": "))
        sum += num 
    print("Average:", sum/NUMBER_OF_ENTRIES)


main()
