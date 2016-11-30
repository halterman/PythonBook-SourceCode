class FunctionTester:
    """ Provides support for testing simple Python functions. """

    def __init__(self):
        """ Creates a FunctionTester object.  Resets the counts to zero.  """
        self.__error_count = self.__total_count = 0
        print("+---------------------------------------")
        print("|  Testing                         ")
        print("+---------------------------------------")

    def check(self, msg, expected, func, *args):
        """ Clients pass a human-readable message (msg) to uniquely
            identify the test case, the expected value that a
            correct test would produce (expected), the function to
            test (func), and any arguments that the function under
            test requires (*args).
            Provides immediate printed feedback about the test's 
            success or failure and adjusts error count accordingly. 
            Returns True if the function passed the test;
            otherwise, returns False. """
        result = True  # Test passed unless we determine otherwise
        print("   ", msg, " ", end=" ")
        self.__total_count += 1      #  Count this test
        try:
            actual = func(*args)       #  Apply function to arguments
            if expected == actual:
                print("OK")
            else:
                self.__error_count += 1  #  Count this failed test
                print("*** Failed!  Expected:", expected, 
                      "actual:", actual)
                result = False  # Test failed
        except Exception as e:
            self.__error_count += 1  #  Count this failed test
            print("****** Exception", e)
            result = False  # Test failed
        return result  # Notify client of test result


    def report_results(self):
        """ Prints the testing statistics. """
        print("+--------------------------------------")
        print("|", self.__total_count, "tests run")
        print("|", self.__total_count - self.__error_count, " passed")
        print("|", self.__error_count, " failed")
        print("+--------------------------------------")
