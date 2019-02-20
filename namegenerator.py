import random, string


def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)

    letter_input_1 = raw_input('choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter: ')
    letter_input_2 = raw_input('choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter: ')
    letter_input_3 = raw_input('choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter: ')
    letter_input_4 = raw_input('choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter: ')
    letter_input_5 = raw_input('choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter: ')

    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    letter = random.choice(string.ascii_lowercase)

    if letter_input_1 == 'v':
        letter1 = random.choice(vowels).capitalize()
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants).capitalize()
    else:
        letter1 = random.choice(letter).capitalize()

    if letter_input_2 == 'v':
        letter2 = random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    else:
        letter2 = random.choice(letter)

    if letter_input_3 == 'v':
        letter3 = random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    else:
        letter3 = random.choice(letter)
    
    if letter_input_4 == 'v':
        letter4 = random.choice(vowels)
    elif letter_input_4 == 'c':
        letter4 = random.choice(consonants)
    else:
        letter4 = random.choice(letter)

    if letter_input_5 == 'v':
        letter5 = random.choice(vowels)
    elif letter_input_5 == 'c':
        letter5 = random.choice(consonants)
    else:
        letter5 = random.choice(letter)


    name = letter1 + letter2 + letter3 + letter4 + letter5
    return(name)



print(generator())