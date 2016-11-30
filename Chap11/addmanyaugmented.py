def sum(*nums):
    print(nums)       # See what nums really is
    s = 0             # Initialize sum to zero
    for num in nums:  # Consider each argument passed to the function
        s += num      # Accumulate their values 
    return s          # Return the sum


print(sum(3, 4))
print(sum(3, 4, 5))
print(sum(3, 3, 3, 3, 4, 1, 9, 44, -2, 8, 8))
