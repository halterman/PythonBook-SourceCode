#  File computesquareroot.py

#  Get value from the user
val = float(input('Enter number: '))
#  Compute a provisional square root
root = 1.0

#  How far off is our provisional root?
diff = root*root - val

#  Loop until the provisional root
#  is close enough to the actual root
while diff > 0.00000001 or diff < -0.00000001:
    print(root, 'squared is', root*root)  # Report how we are doing
    root = (root + val/root) / 2          # Compute new provisional root
    # How bad is our current approximation?
    diff = root*root - val

#  Report approximate square root
print('Square root of', val, '=', root)
