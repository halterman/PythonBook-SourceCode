word = '*'  # Initial word to ensure loop entry
while word != '':  # Loop until user presses return by itself
    # Obtain word from the user
    word = input('Enter Spanish word:')
    if word == 'uno':
        print('one')
    elif word == 'dos':
        print('two')
    elif word == 'tres':
        print('three')
    elif word == 'cuatro':
        print('four')
    elif word == 'cinco':
        print('five')
    elif word == 'seis':
        print('six')
    elif word == 'siete':
        print('seven')
    elif word == 'ocho':
        print('eight')
    else:    # Unknown word
        print('???')
