translator = {'uno':'one',
              'dos':'two',
              'tres':'three',
              'cuatro':'four',
              'cinco':'five',
              'seis':'six',
              'siete':'seven',
              'ocho':'eight'}
word = '*'
while word != '':  # Loop until user presses return by itself
    # Obtain word from the user
    word = input('Enter Spanish word:')
    if word in translator:
        print(translator[word])
    else:
        print('???')   # Unknown word
