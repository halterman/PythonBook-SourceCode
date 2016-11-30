#  File timeconvcond1.py

#  Some useful conversion factors
seconds_per_minute = 60
seconds_per_hour   = 60*seconds_per_minute  # 3600

#  Get user input in seconds
seconds = int(input("Please enter the number of seconds:"))

#  First, compute the number of hours in the given number of seconds
hours = seconds // seconds_per_hour  # 3600 seconds = 1 hour
#  Compute the remaining seconds after the hours are accounted for
seconds = seconds % seconds_per_hour
#  Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // seconds_per_minute  # 60 seconds = 1 minute
#  Compute the remaining seconds after the minutes are  accounted for
seconds = seconds % seconds_per_minute
#  Report the results
print(hours, end='')
# Decide between singular and plural form of hours
if hours == 1:
    print(" hour ", end='')
else:
   print(" hours ", end='')
print(minutes, end='')
# Decide between singular and plural form of minutes
if minutes == 1:
    print(" minute ", end='')
else:
    print(" minutes ", end='')
print(seconds, end='')
# Decide between singular and plural form of seconds
if seconds == 1:
    print(" second")
else:
    print(" seconds")
