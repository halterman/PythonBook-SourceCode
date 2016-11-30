from fractions import Fraction

f1 = Fraction(3, 4)     # Make the fraction 3/4
print(f1)               # Print it
print(f1.numerator)     # Print numerator
print(f1.denominator)   # Print denominator
print(float(f1))        # Floating-point equivalent
f2 = Fraction(1, 8)     # Make another fraction, 1/8
print(f2)               # Print the second fraction
f3 = f1 + f2            # Add the two fractions
print(f3)               # 3/4 + 1/8 = 6/8 + 1/8 = 7/8
