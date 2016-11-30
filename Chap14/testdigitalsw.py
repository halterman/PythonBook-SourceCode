from digitalstopwatch import DigitalStopwatch
from time import sleep

dsw = DigitalStopwatch()
dsw.start()                # Start the timer
sleep(140)                 # Do noting for 2:20
dsw.stop()                 # Stop the timer
print(dsw.digital_time())  # Print elapsed time in digital format
