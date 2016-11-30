def help_screen():
    """
    Displays information about how the program works.
    Accepts no parameters.
    Returns nothing.
    """
    print("Add:  Adds two numbers")
    print("Subtract:  Subtracts two numbers")
    print("Print:  Displays the result of the latest operation") 
    print("Help:  Displays this help screen")
    print("Quit:  Exits the program")


def menu(): 
     """
     Display a menu.
     Accepts no parameters.
     Returns the string entered by the user.
     """
     # Display a menu
    return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")


# Global variables used by several functions
result = 0.0 
arg1 = 0.0
arg2 = 0.0

def get_input():
   """
   Assigns the globals arg1 and arg2 from user keyboard input.
   """
   global arg1, arg2  # arg1 and arg2 are globals
   arg1 = float(input("Enter argument #1: "))
   arg2 = float(input("Enter argument #2: "))


def report():
    """ Reports the value of the global result """
    # Not assigning to result, global keyword not needed 
    print(result)


def add():
    """
    Assigns the sum of the globals arg1 and arg2
    to the global variable result.
    """
    global result   # Assigning to result, global keyword needed
    result = arg1 + arg2


def subtract():
    """
    Assigns the difference of the globals arg1 and arg2 
    to the global variable result
    """
    global result   # Assigning to result, global keyword needed
    result = arg1 - arg2


def main():
    """
    Runs a command loop that allows users to
    perform simple arithmetic.
    """
    done = False   # Initially not done
    while not done:
        choice = menu()     # Get user's choice
        
        if choice == "A" or choice == "a":   # Addition
            get_input()
            add()
            report()
        elif choice == "S" or choice == "s": # Subtraction
            get_input()
            subtract()
            report()
        elif choice == "P" or choice == "p": # Print
            report()
        elif choice == "H" or choice == "h": # Help
            help_screen()
        elif choice == "Q" or choice == "q": # Quit
            done = True


main()
