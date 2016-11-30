from stopwatch import Stopwatch

class CountingStopwatch(Stopwatch):
    def __init__(self):
        # Allow base class to do its initialization of the
        # inherited instance variables
        super().__init__()
        # Set number of starts to zero
        self._count = 0

    def start(self):
        # Count this start message unless the watch already is running
        if not self._running:
            self._count += 1
        # Let base class do its start code
        super().start()

    def reset(self):
        # Let base class reset the inherited instance variables
        super().reset()
        # Reset new instance variable that the base class method does not know about
        self._count = 0
        
    def count(self):
        return self._count
