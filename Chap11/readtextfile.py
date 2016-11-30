def readfile(filename):
    """ Read the comma-separated integer data from the text file
        named filename and return the data in a list. """
    result = []   # List initially empty
    with open(filename, "r") as f:
        for line in f:
            # Remove any trailing spaces, comma, and newline
            result += [int(x.strip()) for x in line.rstrip(" ,\n").split(",")]
    return result
        

def main():
    lst = readfile("monitor.data")
    print(lst)


if __name__ == "__main__":
    main()
