from stopwatch import Stopwatch

class DigitalStopwatch(Stopwatch):
    def digital_time(self):
        """  Returns a string representation of the elapsed time
             in hours : minutes : seconds.  """
        # Compute time in hours, minutes, and seconds
        seconds = round(self.elapsed())
        hours = seconds // 3600    # Compute total hours
        seconds %= 3600            # Update seconds remaining
        minutes = seconds // 60    # Compute minutes 
        seconds %= 60              # Update seconds remaining
        # Each digit occupies two spaces; pad with leading zeros, if necessary
        return "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)
