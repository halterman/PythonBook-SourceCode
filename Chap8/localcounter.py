def create_counter(n):
    """  Creates a counting function that counts up to n """
    count = 0

    def counter():     # Local function
        """  Increments the outer variable unless it
             has reached its limit  """
        nonlocal count
        if count < n:
            count += 1
        return count

    return counter   # Returns a function


ctr = create_counter(4)
print(ctr())
print(ctr())
print(ctr())
print(ctr())
print(ctr())
print(ctr())
