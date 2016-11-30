class Rational:
    """
    Represents a rational number (fraction)
    """
    def __init__(self, num, den):
        self.__numerator = num
        if den != 0:
            self.__denominator = den
        else:
            raise ValueError("Attempt to make an illegal rational number")
        
    def get_numerator(self):
        """  Returns the numerator of the fraction.  """
        return self.__numerator 

    def get_denominator(self):
        """  Returns the denominator of the fraction.  """
        return self.__denominator 

    def set_numerator(self, n):
        """  Sets the numerator of the fraction to n.  """
        self.__numerator = n

    def set_denominator(self, d):
        """  
        Sets the denominator of the fraction to d,
        unless d is zero.  If d is zero, the method
        terminates the program with an error meesage.
        """
        if d != 0:
            self.__denominator = d
        else:
            raise ValueError("Error: zero denominator!")

    def __mul__(self, other):
        """ 
        Returns the product of this rational number object with 
        the other rational object. 
        """
        return Rational(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)
        
    def __add__(self, other):
        """ 
        Returns the sum of this rational number object with 
        the other rational object. 
        """
        pass  # Not yet implemented

    def __str__(self):
        """
        Make a string representation of a Rational object
        """
        return str(self.get_numerator()) + "/" + str(self.get_denominator())

# Client code that uses Rational objects
def main():
    fract1 = Rational(1, 2)
    fract2 = Rational(2, 3)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(1)
    fract2.set_denominator(10)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract3 = Rational(1, 2)
    fract4 = Rational(3, 5)
    print(fract3, "*", fract4, "=", fract3 * fract4)

main()
