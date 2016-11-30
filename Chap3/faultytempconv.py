#  File faultytempconv.py

#  Establish some variables
degreesF, degreesC = 0, 0
#  Define the relationship between F and C
degreesC = 5/9*(degreesF - 32)
#  Prompt user for degrees F
degreesF = float(input('Enter the temperature in degrees F: '))
#  Report the result
print(degreesF, "degrees F =', degreesC, 'degrees C')
