f = open('data.dat')      # f is a file object
for line in f:            # Read each line as text
    print(line.strip())   # Remove trailing newline character
f.close()                 # Close the file
