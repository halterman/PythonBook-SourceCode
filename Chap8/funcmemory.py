count = 0      # A global count variable

def remember():
    global count
    count += 1  # Count this invocation
    print('Calling remember (#' + str(count) + ')')


print('Beginning program')
remember()
remember()
remember()
remember()
remember()
print('Ending program')
